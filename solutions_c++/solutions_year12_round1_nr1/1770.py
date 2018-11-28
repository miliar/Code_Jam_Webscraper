#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <map>
//#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

int main (int argc, char * argv[]) {
    ifstream is(&argv[1][0]);
    string line;
    int cases;
    int typed, length;
    cout.precision(6);
    cout.setf(ios::fixed,ios::floatfield);
    if (is.is_open()) {
        if (is.good()) { 
            getline(is, line);
            cases = atoi(line.c_str());
        }
        for (int caseCounter = 0; caseCounter < cases; caseCounter++) {
            getline(is, line, ' ');
            typed = atoi(line.c_str());
            getline(is, line);
            length = atoi(line.c_str());
            //cout << typed << " " << length << endl;

            float * correct_prob = new float[typed];
            for (int i = 0; i < typed-1; i++) {
                getline(is, line, ' ');
                correct_prob[i] = atof(line.c_str());
                //cout << correct_prob[i] << "\t";
            } 
            getline(is, line);
            correct_prob[typed-1] = atof(line.c_str());
            //cout << correct_prob[typed-1] << endl;

 
            int ** possibilities = new int*[typed+2];
            float * expected = new float[typed+2];
            int comb = pow(2,typed);
            for (int i = 0; i < typed + 2; i++) {
                possibilities[i] = new int[comb];
            }

            //generate all variations
            float * probabilities = new float[comb];
            for (int j = 0; j < comb; j++)
                probabilities[j] = 1;
            int t = comb/2;
            for (int j = 0; j < typed; j++) {
                int c = 0; 
                while (c < comb) {
                    for (int i = 0; i < t; i++) {
                        probabilities[c++] *= correct_prob[j]; 
                    }
                    for (int i = 0; i < t; i++) {
                        probabilities[c++] *= (1 - correct_prob[j]); 
                    }
                }
                t /= 2;
            }

            for (int j = 0; j < comb; j++) {
                possibilities[typed+1][j] = length + 2;  
            }
            t = comb;
            for (int i = typed; i >= 0; i--) {
                float positive = i + length - (typed-i) + 1; 
                for (int j = 0; j < t; j++) {
                    possibilities[i][j] = positive; 
                }
                for (int j = t; j < comb; j++) {
                    possibilities[i][j] = positive + length + 1; 
                }
                t /= 2;
            }

            for (int i = 0; i < typed + 2; i++) {
                expected[i] = 0; 
                for (int j = 0; j < comb; j++) {
                    expected[i] += probabilities[j] * possibilities[i][j]; 
                }
                //cout << expected[i] << endl;
            }
            float min = expected[0];
            for (int i = 1; i < typed + 2; i++)
                if (expected[i] < min) 
                    min = expected[i];
            cout << "Case #" << caseCounter+1 << ": ";
            cout << min << endl; 

            delete [] correct_prob;
            delete [] probabilities;
            for (int i = 0; i < typed + 2; i++) 
                delete [] possibilities[i];
            delete [] possibilities;
        }
        is.close();
        return 0;
    }
    return -1;    
}
