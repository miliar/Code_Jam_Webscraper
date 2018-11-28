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
#include <sys/time.h>
#include <math.h>
#include <stdlib.h>

using namespace std;



////////////////////////////////////////
// core structures start from here
////////////////////////////////////////

// core structures
class CoreStruct {
public:
    int index_line;
    int num_cases;
    int cur_case;

    // core structures, #################### MODIFICATION FLAG 1 ####################
    #define MAX_CASES           100
    #define NUM_PER_CASE        100
    struct Cases {
        // variables, sources
        int NM[2];
        string old_dirs[NUM_PER_CASE];
        string new_dirs[NUM_PER_CASE];

        // variables, results
        //int results[NUM_PER_CASE];
        long long results;

        // functions to show sources and results
        string StringCases() {
            stringstream ret;

            ret << "N:" << NM[0] << ", M:" << NM[1];

            return ret.str();
        }
        string StringResult() {
            stringstream ret;
            ret << " " << results << "\n";

            return ret.str();
        }

    } cases[MAX_CASES];
    // core structures, #################### MODIFICATION FLAG 1 ####################

    // constructor
    CoreStruct() {
        index_line = 0;
        num_cases = 0;
        cur_case = 0;
    }

    // save and convert the input
    int Save(string line) {
        if(line.empty()) {
            return 0;
        }
        index_line ++;

        // save total number of cases
        if (index_line == 1) {
            num_cases = atoi(line.c_str());
            if (num_cases > 0) {
                cerr << "Total cases: " << num_cases << "\n";
                cerr << "----------------------------------------\n";
                return 0;
            }
            return 1;
        }

        // save all cases, #################### MODIFICATION FLAG 2 ####################
        static int n = -1;
        static int m = -1;
        if (n == -1) {
            // the N M line
            TokGetLineOfInt32(line, cases[cur_case].NM);
            n = 0;
            m = 0;
        } else if (n < cases[cur_case].NM[0]) {
            // all N
            TokGetLineOfString(line, cases[cur_case].old_dirs + n);
            n ++;
        } else {
            if (m < cases[cur_case].NM[1]) {
                // all M
                TokGetLineOfString(line, cases[cur_case].new_dirs + m);
                m ++;
            }

            if (m >= cases[cur_case].NM[1]) {
                // end of this case
                cur_case ++;
                n = -1;
                m = -1;
            }
        }
        // save all cases, #################### MODIFICATION FLAG 2 ####################

        return 0;
    }

    void ShowCase(int index) {
        // show title
        stringstream ss;
        cerr << "#### [DEBUG #" << index + 1 << "] ";
        cerr << "(" << cases[index].StringCases() <<")";
    }

    string GetResult(int index) {
        return cases[index].StringResult();
    }

private:
    // here are the token functions
    void TokGetLineOfInt32(string line, int array[]) {
        int i = 0;
        char* str = strdup(line.c_str());
        char* t = strtok(str, " ");
        while (t != NULL) {
            array[i++] = atoi(t);
            t = strtok(NULL, " ");
        }
        free(str);
    }

    void TokGetLineOfInt64(string line, long long array[]) {
        int i = 0;
        char* str = strdup(line.c_str());
        char* t = strtok(str, " ");
        while (t != NULL) {
            array[i++] = atoll(t);
            t = strtok(NULL, " ");
        }
        free(str);
    }

    void TokGetLineOfString(string line, string array[]) {
        int i = 0;
        char* str = strdup(line.c_str());
        char* t = strtok(str, " ");
        while (t != NULL) {
            array[i++] = t;
            t = strtok(NULL, " ");
        }
        free(str);
    }

    void TokGetLineOfChar(string line, char array[]) {
        for (unsigned int i=0; i<line.length(); i++) {
            array[i] = line[i];
            if ((line[i] == '\n') || (line[i] == '\r')) {
                cerr << "Line has <ENTER> at the end?\n";
            }
        }
    }

} cs;



////////////////////////////////////////
// algorithms start from here
////////////////////////////////////////
class GCJ {
private:
    // real algorithm functions, #################### MODIFICATION FLAG 3 ####################
    struct DirTree {
        struct TreeNode {
            string name;
            TreeNode* sub_dirs[NUM_PER_CASE];

            TreeNode(string str) {
                name = str;
                for (int i=0; i<NUM_PER_CASE; i++) {
                    sub_dirs[i] = NULL;
                }
            }

            ~TreeNode() {
                for (int i=0; i<NUM_PER_CASE; i++) {
                    if (sub_dirs[i]) {
                        delete sub_dirs[i];
                        sub_dirs[i] = NULL;
                    }
                }
            }

            TreeNode* Add(string dir, long long& total) {
                int i = 0;
                for (; i<NUM_PER_CASE; i++) {
                    if (sub_dirs[i]) {
                        if (dir.compare(sub_dirs[i]->name) == 0) {
                            // found it
                            return sub_dirs[i];
                        }
                    } else {
                        // empty now
                        break;
                    }
                }
                if (i == NUM_PER_CASE) {
                    // full?
                    cerr << "Array full!!! IMPOSSIBLE !!!\n";
                    return NULL;
                } else {
                    sub_dirs[i] = new TreeNode(dir);
                    total ++;
                    return sub_dirs[i];
                }
            }

        } * root;

        DirTree() {
            root = new TreeNode("/");
        }

        ~DirTree() {
        }

        TreeNode* AddToTree(string dir, TreeNode* node, long long& total) {
            if (node == NULL) {
                cerr << "IMPOSSIBLE !!!\n";
            }

            return node->Add(dir, total);
        }

        long long BuildTree(string dir) {
            long long total = 0;
            TreeNode* node = root;

            char* str = strdup(dir.c_str());
            char* t = strtok(str, "/");
            while (t != NULL) {
                node = AddToTree(t, node, total);
                t = strtok(NULL, "/");
            }
            free(str);

            return total;
        }

        long long BuildDirTrees(string dirs[]) {
            long long total = 0;
            for (int i=0; i<NUM_PER_CASE; i++) {
                if (dirs[i].empty()) {
                    break;
                }
                total += BuildTree(dirs[i]);
            }
            return total;
        }
    };

    // algorithm recur entry

    // algorithm main entry
    void DoIt(int index_case) {
        DirTree tree;
        tree.BuildDirTrees(cs.cases[index_case].old_dirs);
        cs.cases[index_case].results = tree.BuildDirTrees(cs.cases[index_case].new_dirs);
    }
    // real algorithm functions, #################### MODIFICATION FLAG 3 ####################



    ////////////////////////////////////////////////////////////////////////////////
    // general algorithm entry, need NO CHANGE for each problem
    string Algo(int index_case) {
        // print out case debug info
        cs.ShowCase(index_case);

        // start performance monitor for this case
        PerfMonitor(1);
        // here is the real algorithm entry
        DoIt(index_case);
        // end of performance monitor
        PerfMonitor(2);

        // return result as a string
        return cs.GetResult(index_case);
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
    // run the cases one by one, need NO CHANGE for each problem
    int Run() {
        for (int i=0; i<cs.num_cases; i++) {
            cout << "Case #" << i+1 << ":" << Algo(i);
        }

        PerfMonitor(0);
        return 1;
    }

} gcj;



////////////////////////////////////////
// general libraries start from here
// need NO CHANGE for each problem
////////////////////////////////////////

// function to read the input file
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
            cerr << "File name NULL!\n";
            return 0;
        }

        // open file
        fs.open(file);
        if (fs.is_open()) {
            cerr << "Open file " << file << " successfully.\n";
            return 1;
        } else {
            cerr << "Unable to open file '" << file << "'!\n";
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

// function to parse the input file
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

// main function goes here
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

