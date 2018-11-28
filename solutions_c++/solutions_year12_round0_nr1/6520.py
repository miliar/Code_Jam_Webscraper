#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

// Class for each test case of the problem
class Instance {
    private:
        char *instr;
        string solution;
        stringstream ss;
        int case_len;
        
    public:
        Instance() {
            case_len = 101;
        }
        
        void readInput(ifstream &in) {
            instr = new char[case_len];
            in.getline(instr, case_len);
        }
        
        void solve(ifstream &in) {
            readInput(in);
            for(int i=0; instr[i] != '\0'; i++) {
                switch(instr[i]) {
                    case 'a':
                        ss << 'y';
                        break;
                    case 'b':
                        ss << 'h';
                        break;
                    case 'c':
                        ss << 'e';
                        break;
                    case 'd':
                        ss << 's';
                        break;
                    case 'e':
                        ss << 'o';
                        break;
                    case 'f':
                        ss << 'c';
                        break;
                    case 'g':
                        ss << 'v';
                        break;
                    case 'h':
                        ss << 'x';
                        break;
                    case 'i':
                        ss << 'd';
                        break;
                    case 'j':
                        ss << 'u';
                        break;
                    case 'k':
                        ss << 'i';
                        break;
                    case 'l':
                        ss << 'g';
                        break;
                    case 'm':
                        ss << 'l';
                        break;
                    case 'n':
                        ss << 'b';
                        break;
                    case 'o':
                        ss << 'k';
                        break;
                    case 'p':
                        ss << 'r';
                        break;
                    case 'q':
                        ss << 'z';
                        break;
                    case 'r':
                        ss << 't';
                        break;
                    case 's':
                        ss << 'n';
                        break;
                    case 't':
                        ss << 'w';
                        break;
                    case 'u':
                        ss << 'j';
                        break;
                    case 'v':
                        ss << 'p';
                        break;
                    case 'w':
                        ss << 'f';
                        break;
                    case 'x':
                        ss << 'm';
                        break;
                    case 'y':
                        ss << 'a';
                        break;
                    case 'z':
                        ss << 'q';
                        break;
                    default:
                        ss << instr[i];
                }
                solution = ss.str();
            }
        }
        
        string getSolution() {
            return solution;
        }
};

// Class for the main given problem
class Problem {
    private:
        Instance *instances;
        int cases, cases_max_digit;
        ifstream *in;        
        
    public:
        Problem(char *inpath) {
            cases_max_digit = 3;
            char *tmpStr = new char[cases_max_digit];            
            in = new ifstream(inpath, ios::in);
            in->getline(tmpStr, cases_max_digit);
            cases = atoi(tmpStr);
            instances = new Instance[cases];
        }
        
        void solve() {
            for (int i=0; i<cases; i++) {
                instances[i].solve(*in);
            }
        }
        
        void writeOutput(const char *outpath) {
            ofstream out(outpath);
            for (int i=0; i<cases; i++) {
                out << "Case #" << i+1 << ": " << instances[i].getSolution();
                if(i < cases-1) 
                    out << endl;
            }
            out.close();
        }
};

int main (int argc, char *argv[]) {
    if (argc > 2) {
        Problem problem(argv[1]);
        problem.solve();
        problem.writeOutput(argv[2]);
    }
    else {
        cout << "Incorrect number of arguments. Usage <prog name> <input file> <output file>" << endl;
    }
    
    return 0;
}
