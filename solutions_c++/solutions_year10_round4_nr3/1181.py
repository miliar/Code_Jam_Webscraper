////////////////////////////////////////
//
// Wei Zhang
// bugzzzzzz@gmail.com
//
////////////////////////////////////////

#include <iostream>
#include <fstream>
#include <sstream>
#include <list>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <sys/time.h>

using namespace std;



////////////////////////////////////////////////////////////////////////////////
// general libraries start from here
// need NO CHANGE for each problem
////////////////////////////////////////////////////////////////////////////////

class CommonTable {
public:
    #define MAX_TABLE_FACTORIAL     1000
    double Factorial[MAX_TABLE_FACTORIAL];
    void Init_Factorial() {
        double total = 1;
        Factorial[0] = 1;
        for (int i=1; i<=MAX_TABLE_FACTORIAL; i++) {
            total *= i;
            Factorial[i] = total;
            //cerr << "Factorial[" << i << "] = " << Factorial[i] << "\n";
        }
    }

    #define MAX_TABLE_FIBONACCI     2000
    double Fibonacci[MAX_TABLE_FIBONACCI];
    void Init_Fibonacci() {
        Fibonacci[0] = 0;
        Fibonacci[1] = 1;
        for (int i=2; i<=MAX_TABLE_FIBONACCI; i++) {
            Fibonacci[i] = Fibonacci[i-1] + Fibonacci[i-2];
            //cerr << "Fibonacci[" << i << "] = " << Fibonacci[i] << "\n";
        }
    }

    // Greatest common divisor
    long long GCD(long long a, long long b) {
        if (b == 0) {
            return a;
        }
        return GCD(b, a%b);
    }

    // Least common multiple
    long long LCM(long long a, long long b) {
        return (a/GCD(a,b))*b;
    }

    long long Hex2Int(string str) {
        stringstream ss(str);
        long long ret = 0;
        ss >> std::hex >> ret;
        return ret;
    }

    void Init() {
        Init_Factorial();
        Init_Fibonacci();
    }

} ct;

class FileInput {
public:
    ~FileInput() {
        // close file
        if (fs.is_open()) {
            fs.close();
        }
    }

    int Init(string file) {
        if (file.empty()) {
            cerr << "File name empty!\n";
            return 0;
        }

        // open file
        fs.open(file.c_str());
        if (! fs.is_open()) {
            cerr << "Unable to open file '" << file << "'!\n";
            return 0;
        }

        cerr << "Open file " << file << " successfully.\n";
        return 1;
    }

    template <class T> int GetLineToArray(T* array) {
        int i = 0;
        string line;
        if (ReadInputNextLine(line)) {
            char* str = strdup(line.c_str());
            char* t = strtok(str, " ");
            while (t != NULL) {
                stringstream ss(t);
                ss >> array[i++];
                t = strtok(NULL, " ");
            }
            free(str);
        }
        return i;
    }

private:
    ifstream fs;

    // read the next line of input
    int ReadInputNextLine(string& line) {
        if (! fs.eof()) {
            getline(fs, line);
            return 1;
        } else {
            return 0;
        }
    }

} fi;



////////////////////////////////////////////////////////////////////////////////
// core structures and algorithms start from here
////////////////////////////////////////////////////////////////////////////////

// save all temporary results to speed up computation if possible, NOT always required
class GCJDB {
public:
    // size of this database
    #define MAX_CACHE_SIZE          1000

    // cached items here
    struct CaseCache {
        // temp result
        long long result;
    } cc[MAX_CACHE_SIZE];

    // common tree structure
    #define MAX_TREE_DEGREE         100
    struct TreeNode {
        // add tree content here

        // children links
        TreeNode* children[MAX_TREE_DEGREE];
    } * root;

} db;

// all cases, ######################################## MODIFICATION FLAG ########################################
#define MAX_CASES               100
class GCJCase {
public:
    // input data
    #define NUM_PER_CASE        1000
    struct CaseInput {
        int R;
        int points[NUM_PER_CASE][4];
    } ci;

    // result data
    struct CaseResult {
        long long result;
    } cr;

    // return the input info we want to show for this case
    string ShowInput() {
        stringstream ret;
        ret << "R:" << ci.R;
        return ret.str();
    }

    // return the result as a string for this case
    string ShowResult() {
        stringstream ret;
        ret << " " << cr.result << "\n";
        return ret.str();
    }

    // function to read input for this case
    int ReadInput() {
        // get R first
        fi.GetLineToArray(&ci.R);

        // get R lines following
        for (int i=0; i<ci.R; i++) {
            fi.GetLineToArray(ci.points[i]);
        }

        return 1;
    }

    #define MAX_CELL    101
    int AllZero(char c[MAX_CELL][MAX_CELL]) {
        for (int i=0; i<MAX_CELL; i++) {
            for (int j=0; j<MAX_CELL; j++) {
                if (c[i][j]) {
                    return 0;
                }
            }
        }
        return 1;
    }

    // algorithm recur entry
    long long RunCell(char c[MAX_CELL][MAX_CELL]) {
        // if all 0, return 0
        if (AllZero(c)) {
            return 0;
        }

        // change cell
        for (int i=MAX_CELL-1; i>=0; i--) {
            for (int j=MAX_CELL-1; j>=0; j--) {
                if (c[i][j]) {
                // now it's 1
                    // check if it will die
                    int live = 0;
                    if ( (i > 0) && (c[i-1][j]) ) {
                        live = 1;
                    }
                    if ( (j > 0) && (c[i][j-1]) ) {
                        live = 1;
                    }
                    c[i][j] = live;
                } else {
                // now it's 0
                    // check if it get a new one
                    if ( (i > 0) && (c[i-1][j]) && (j > 0) && (c[i][j-1]) ) {
                        // get a new one
                        c[i][j] = 1;
                    }
                }
            }
        }

        return RunCell(c) + 1;
    }

    // algorithm main entry
    void Run() {
        // build matrix first
        char c[MAX_CELL][MAX_CELL];
        memset(c, 0, MAX_CELL*MAX_CELL);
        for (int i=0; i<ci.R; i++) {
            int x1 = ci.points[i][0];
            int y1 = ci.points[i][1];
            int x2 = ci.points[i][2];
            int y2 = ci.points[i][3];
            // build line of cells
            for (int j=y2; j>=y1; j--) {
                for (int k=x2; k>=x1; k--) {
                    // find the position
                    c[k][j] = 1;
                }
            }
        }

        // go to real count down
        long long total = RunCell(c);

        cr.result = total;
    }

} cases[MAX_CASES];
        /*
        struct Cell {
            int x1;
            int x2;
            Cell* next;
        } * c[MAX_CELL];

        for (int i=0; i<ci.R; i++) {
            int x1 = ci.points[i][0];
            int y1 = ci.points[i][1];
            int x2 = ci.points[i][2];
            int y2 = ci.points[i][3];
            // build line of cells
            for (int j=y2; j>=y1; j--) {
                // find the position
                Cell* pre = NULL;
                Cell* cur = c[j];
                while (cur) {
                    if (x2 >= (cur->x1 - 1)) {
                        // block in range
                        break;
                    }
                    // go to next
                    pre = cur;
                    cur = cur->next;
                }
            }
        }
        */
// all cases, ######################################## MODIFICATION FLAG ########################################



////////////////////////////////////////////////////////////////////////////////
// class to monitor core problems
////////////////////////////////////////////////////////////////////////////////
class GCJ {
private:
    int num_cases;

    // save total number of cases from the input
    int ReadNumCases() {
        if (fi.GetLineToArray(&num_cases) == 1) {
            if (num_cases > 0) {
                cerr << "Total cases: " << num_cases << "\n";
                cerr << "----------------------------------------\n";
                return num_cases;
            }
        }

        return 0;
    }

    void ShowCaseInfo(int index) {
        // show title
        stringstream ss;
        cerr << "#### [DEBUG #" << index+1 << "] ";
        cerr << "(" << cases[index].ShowInput() <<")";
    }

    void RunCase(int index) {
        // run the case
        cases[index].Run();
    }

    string GetResult(int index) {
        return cases[index].ShowResult();
    }

    // get the total number of cases
    int GetNumCases() {
        return num_cases;
    }

    // monitor the performance/time of each test case, need NO CHANGE for each problem
    void PerfMonitor(int type) {
        static timeval tv_begin;
        static timeval tv_end;
        static int total_time = 0;

        if (type == 1) {
            // timestamp of case begin
            gettimeofday(&tv_begin, NULL);
        } else if (type == 2) {
            // timestamp of case end, and print it out
            gettimeofday(&tv_end, NULL);
            int elapse = (tv_end.tv_sec-tv_begin.tv_sec)*1000 + (tv_end.tv_usec-tv_begin.tv_usec)/1000;
            total_time += elapse;
            fprintf(stderr, " (Takes %6d ms)\n", elapse);
        } else {
            // all over, calculate and print the total
            cerr << "----------------------------------------\n";
            cerr << "It takes " << total_time << " ms in total.\n";
        }
    }

public:
    // function to parse the input file
    int ParseInput(string file) {
        if (fi.Init(file)) {
            if (ReadNumCases()) {
                for (int i=0; i<num_cases; i++) {
                    if (! cases[i].ReadInput() ) {
                        cerr << "Read case " << i+1 << " error!\n";
                        return 0;
                    }
                }
                return 1;
            } else {
                cerr << "Read total number cases error!\n";
                return 0;
            }
        }

        return 0;
    }

    // run the cases one by one, need NO CHANGE for each problem
    int Run() {
        for (int i=0; i<num_cases; i++) {
            // print out case debug info
            ShowCaseInfo(i);

            // start performance monitor for this case
            PerfMonitor(1);

            // here is the real algorithm entry
            RunCase(i);

            // end of performance monitor
            PerfMonitor(2);

            // print result
            cout << "Case #" << i+1 << ":" << GetResult(i);
        }

        PerfMonitor(0);
        return 1;
    }

    void PrintUsage() {
        cerr << "Usage: gcj inputfile.\n";
    }

} gcj;

// main function goes here
int main(int argc, char** argv) {
    if (gcj.ParseInput(argv[1])) {
        ct.Init();
        return gcj.Run();
    } else {
        gcj.PrintUsage();
        return 0;
    }
}

