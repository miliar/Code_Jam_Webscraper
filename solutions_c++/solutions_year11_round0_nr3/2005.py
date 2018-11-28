#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");
#define MAX 1001
#define MAXVAL 1000000001
int nTest,cNum,N,num[MAX];
int sumXor,i,minVal,sumAdd;
int main() {
    fin >> nTest;
    for (cNum=1;cNum<=nTest;++cNum) {
        fin >> N;
        sumXor = 0;
        sumAdd = 0;
        minVal = MAXVAL;
        for (i=0;i<N;++i) {
            fin >> num[i];
            sumXor = sumXor ^ num[i];
            sumAdd = sumAdd + num[i];
            if (num[i] < minVal) {
               minVal = num[i];
            }
        }
        fout << "Case #" << cNum << ": ";
        if (sumXor != 0) {
           fout << "NO\n";        
        }
        else {
             fout << sumAdd - minVal << "\n";
        }
    }
    return 0;
}
