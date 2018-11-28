////////////////////////////////////////
//
// Wei Zhang
// bugzzzzzz@gmail.com
// This program requires boost C++ library which is commonly used. It can be found at http://www.boost.org/
//
////////////////////////////////////////

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <list>
#include <sys/time.h>
#include <boost/tokenizer.hpp>
#include <boost/format.hpp>
#include <math.h>

using namespace std;
using namespace boost;



////////////////////////////////////////
// core structures start from here
////////////////////////////////////////
#define TOK_LOOP(str, deli)     char_separator<char> sep(deli); \
                                tokenizer< char_separator<char> > tok(str, sep); \
                                for (tokenizer<char_separator<char> >::iterator item=tok.begin(); item!=tok.end(); item++)

#define MAX_CASES           50
#define NUM_PER_CASE        1000

class CoreStruct {
public:
    int index_line;
    int num_cases;
    int cur_case;

    // core struct
    unsigned long long cases[MAX_CASES][NUM_PER_CASE];
    unsigned long long arr_RkN[MAX_CASES][3];

    CoreStruct() {
        index_line = 0;
        num_cases = 0;
        cur_case = 0;

        // initialize core variables
        memset(cases, 0, MAX_CASES*NUM_PER_CASE*sizeof(unsigned long long));
        memset(arr_RkN, 0, MAX_CASES*3*sizeof(unsigned long long));
    }

    int Save(string line) {
        if(line.empty()) {
            return 0;
        }
        index_line ++;

        // save number of cases
        if (index_line == 1) {
            num_cases = atoi(line.c_str());
            if (num_cases > 0) {
                cerr << "Total cases: " << num_cases << "\n";
                cerr << "----------------------------------------\n";
                return 0;
            }

            return 1;
        }

        // save all cases
        if ((index_line) % 2) {
            int i = 0;
            TOK_LOOP(line, " ") {
                cases[cur_case][i++] = atoi((*item).c_str());
            }
            cur_case ++;
        } else {
            int i = 0;
            TOK_LOOP(line, " ") {
                arr_RkN[cur_case][i++] = atoi((*item).c_str());
            }
        }

        return 0;
    }

    void ShowCase(int index) {
        stringstream ss;
        ss << "## (R:" << arr_RkN[index][0] << " k:" << arr_RkN[index][1] << " N:" << arr_RkN[index][2] << ")";
        cerr << format("%-32s") % ss.str();
    }

} cs;



////////////////////////////////////////
// algorithms start from here
////////////////////////////////////////
class GCJ {
private:
    unsigned long long GoRide(int index_case, int& cur) {
        unsigned long long k = cs.arr_RkN[index_case][1];
        unsigned long long N = cs.arr_RkN[index_case][2];

        unsigned long long total = 0;
        unsigned long long num_groups = 0;
        while ( (num_groups < N) && ((total + cs.cases[index_case][cur]) <= k) ) {
            total += cs.cases[index_case][cur++];
            cur %= N;
            num_groups ++;
        }

        return total;
    }

    unsigned long long DoIt(int index_case) {
        unsigned long long R = cs.arr_RkN[index_case][0];

        unsigned long long Hash_total[NUM_PER_CASE];
        unsigned long long Hash_round[NUM_PER_CASE];
        memset(Hash_total, 0, NUM_PER_CASE*sizeof(unsigned long long));
        memset(Hash_round, 0, NUM_PER_CASE*sizeof(unsigned long long));

        int cur = 0;
        unsigned long long grand_total = 0;
        unsigned long long grand_round = 0;
        while (true) {
            grand_total += GoRide(index_case, cur);
            grand_round ++;
            // now `i' is the next one ready to add

            if (grand_round >= R) {
                // it's all over
                return grand_total;
            }

            if (cur == 0) {
                // very good, at the end, will loop then
                break;
            }
            if (Hash_total[cur] > 0) {
                // OK, we were here some time ago, will loop then
                break;
            }
            Hash_total[cur] = grand_total;
            Hash_round[cur] = grand_round;
        }

        if (cur == 0) {
            unsigned long long round_mul = R / grand_round;
            unsigned long long round_left = R % grand_round;

            grand_total *= round_mul;

            for (unsigned long long i=0; i<round_left; i++) {
                grand_total += GoRide(index_case, cur);
            }
        } else {
            unsigned long long fact_total = grand_total - Hash_total[cur];
            unsigned long long fact_round = grand_round - Hash_round[cur];

            unsigned long long round_mul = (R - Hash_round[cur]) / fact_round;
            unsigned long long round_left = (R - Hash_round[cur]) % fact_round;

            grand_total = fact_total * round_mul;
            grand_total += Hash_total[cur];

            for (unsigned long long i=0; i<round_left; i++) {
                grand_total += GoRide(index_case, cur);
            }
        }

        return grand_total;
    }

    string Algo(int index_case) {
        cs.ShowCase(index_case);
        PerfMonitor(0);

        // here is the real algorithm entry
        unsigned long long ret = DoIt(index_case);
        // end of algorithm

        PerfMonitor(1);

        // return result as a string
        stringstream ss;
        ss << " ";
        ss << ret;
        ss << "\n";
        return ss.str();
    }

    void PerfMonitor(int type) {
        static timeval tv_begin;
        static timeval tv_end;
        static int total_time = 0;

        if (type == 1) {
            gettimeofday(&tv_end, NULL);
            int elapse = (tv_end.tv_sec-tv_begin.tv_sec)*1000 + (tv_end.tv_usec-tv_begin.tv_usec)/1000;
            total_time += elapse;
            cerr << format("%s%6d%-8s\n") % " (Takes " % elapse % " ms)";
        } else if (type == 2) {
            cerr << "----------------------------------------\n";
            cerr << "It takes " << total_time << " ms in total.\n";
        } else {
            gettimeofday(&tv_begin, NULL);
        }
    }

public:
    int Run() {
        for (int i=0; i<cs.num_cases; i++) {
            cout << "Case #" << i+1 << ":" << Algo(i);
        }

        PerfMonitor(2);
        return 1;
    }

} gcj;



////////////////////////////////////////
// general libraries start from here
////////////////////////////////////////
class FileReader {
public:
    ~FileReader() {
        // close file
        if (fs.is_open()) {
            fs.close();
        }
    }

    int Init(char* file) {
        if (file == NULL) {
            cerr << "File name NULL.\n";
            return 0;
        }

        // open file
        fs.open(file);
        if (fs.is_open()) {
            return 1;
        } else {
            cerr << "Unable to open file.\n";
            return 0;
        }
    }

    int ReadNextLine(string& line) {
        if (! fs.eof()) {
            getline(fs, line);
            return 1;
        } else {
            return 0;
        }
    }

    void PrintUsage() {
        cerr << "Usage: gcj inputfile.\n";
    }

private:
    ifstream fs;

} fr;

class InputParser {
public:
    InputParser() {
        num_errors = 0;
    }

    int Parse() {
        string line;
        while (fr.ReadNextLine(line)) {
            num_errors += cs.Save(line);
        }
        if (num_errors) {
            return 0;
        }

        return 1;
    }

private:
    int num_errors;

} ip;

int main(int argc, char** argv) {
    if (! fr.Init(argv[1])) {
        fr.PrintUsage();
        return 0;
    }

    if (ip.Parse()) {
        return gcj.Run();
    }

    return 0;
}
