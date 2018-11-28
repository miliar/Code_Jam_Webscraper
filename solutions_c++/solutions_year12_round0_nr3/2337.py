#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <set>

using namespace std;

int main(){
    ifstream problemFile;
    ofstream resultFile;
    string line;
    int cases;

    problemFile.open("C-large.in");
    problemFile >> cases;

    resultFile.open ("result_C.txt");

    for(int i = 1; i < cases+1; i++){
        cout << "Case " << i << endl;
        stringstream sstream;
        int min, max;
        int result = 0;
        problemFile >> min;
        problemFile >> max;

        for(int number = min; number <= max; number++){
            set<int> tmpSet;
            stringstream ss2;
            ss2 << number;
            string s = ss2.str();
            for(int j = 0; j < s.size()-1; j++){
                string subs = s.substr(s.size()-1, 1);
                //cout << "subs = " << subs << endl;
                s.erase(s.size()-1,1);
                s.insert(0, subs);
                //cout << "s = " << s << endl;

                int tmp = atoi(s.c_str());
                if(tmp > number && tmp <= max){
                    //result++;
                    tmpSet.insert(tmp);
                    //cout << "Found #" << result << " : " << number << " - " << tmp << endl;
                }
            }
            result += tmpSet.size();
        }

        sstream << "Case #" << i << ": " << result;
        resultFile << sstream.str() << endl;
    }

    resultFile.close();
    problemFile.close();

    return 0;
}



