// welcomeToCJ.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int calc(string line) {

    string pattern = "welcome to code jam";
    int *count[19];
    for (int i = 0; i < 19; i++) {
        count[i] = new int[line.length()];
    }
    for (int i = 0; i < 19; i++) {
        for (int j = 0; j < line.length(); j++) {
            if (line[j] == pattern[i]) {
                if (i == 0) {
                    count[i][j] = 1;
                }
                else {
                    int tmp = 0;
                    for (int k = 0; k < j; k ++) {
                        tmp += count[i-1][k];
                        tmp = tmp % 10000;
                    }
                    count[i][j] = tmp;
                }
            }
            else {
                count[i][j] = 0;
            }
        }
    }
    int result = 0;
    for (int j = 0; j < line.length(); j++) {
        result += count[18][j];
        result = result % 10000;
    }
    return result;

}
string makedigit(int d) {
    char buf[10];
    sprintf(buf, "%d", d);
    string result = string(buf);
    while (result.length() < 4) 
        result = string("0") + result;
    return result;
}
int main(int argc, char* argv[])
{
    string pattern = "welcome to code jam";
    string filename = "D:\\C-large.in";
    string ofilename = "D:\\C-large.out";
    ifstream fin(filename.c_str());
    ofstream fout(ofilename.c_str());
    int N = 0;
    fin >> N;
    string tmp;
    getline(fin, tmp);
    for (int i = 0; i < N; i++) {
        string cline;
        getline(fin, cline);
        int occ = 0;
        occ = calc(cline);
        string result = makedigit(occ);
        fout << "Case #" << i+1 << ": " << result << endl;
    }
    fin.close();
    fout.close();
	return 0;
}

