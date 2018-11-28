#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>

using namespace std;

int main(){
    ifstream problemFile;
    ofstream resultFile;
    string line;
    int cases;

    problemFile.open("B-large.in");
    getline(problemFile, line);
    cases = atoi(line.c_str());

    resultFile.open ("result_B.txt");

    for(int i = 1; i < cases+1; i++){
        cout << "Case " << i << endl;
        stringstream sstream;
        int number, surprises, min;
        int count = 0;

        problemFile >> number;
        problemFile >> surprises;
        problemFile >> min;

        //cout << "n = " << number << " s = " << surprises << " min = " << min << endl;

        for(int j = 0; j < number; j++){
            int value;
            problemFile >> value;

            int upperlimit = (3 * min) - 2;
            if(upperlimit < 0) upperlimit = 0;
            int lowerlimit;
            if(min > 1){
                lowerlimit = (3 * min) - 4;
                if(lowerlimit < 0) lowerlimit = 0;
            }else{
                lowerlimit = min;
            }

            if(value >= upperlimit) count++;
            else if(value >= lowerlimit && surprises > 0) {
                surprises--;
                count++;
                //cout << "    surprises: " << surprises << endl;
            }
        }

        sstream << "Case #" << i << ": " << count;

        resultFile << sstream.str() << endl;
    }

    resultFile.close();
    problemFile.close();

    return 0;
}


