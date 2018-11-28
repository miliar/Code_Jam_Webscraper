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

#define MAX_CASES           10000
#define NUM_PER_CASE        2

class CoreStruct {
public:
    int index_line;
    int num_cases;
    int cur_case;

    // core struct
    int cases[MAX_CASES][NUM_PER_CASE];

    CoreStruct() {
        index_line = 0;
        num_cases = 0;
        cur_case = 0;

        // initialize core variables
        memset(cases, -1, MAX_CASES*NUM_PER_CASE*sizeof(int));
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
        int i = 0;
        TOK_LOOP(line, " ") {
            cases[cur_case][i++] = atoi((*item).c_str());
        }
        cur_case ++;

        return 0;
    }

    void ShowCase(int index) {
        stringstream ss;
        ss << "## (N:" << cases[index][0] << " K:" << cases[index][1] << ")";
        cerr << format("%-32s") % ss.str();
    }

} cs;



////////////////////////////////////////
// algorithms start from here
////////////////////////////////////////
class GCJ {
private:
    int DoIt(int index_case) {
        int N = cs.cases[index_case][0];
        int K = cs.cases[index_case][1];

        int key = pow(2, N) - 1;

        cerr << "Key:" << key << "\n";
        if ((key & K) == key) {
            return 1;
        }

        return 0;
    }

    string Algo(int index_case) {
        cs.ShowCase(index_case);
        PerfMonitor(0);

        // here is the real algorithm entry
        int ret = DoIt(index_case);
        // end of algorithm

        PerfMonitor(1);

        // return result as a string
        string r = "OFF";
        if (ret) {
            r = "ON";
        }
        stringstream ss;
        ss << " ";
        ss << r;
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
