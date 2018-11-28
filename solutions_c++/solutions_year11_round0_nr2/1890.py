#include <iostream>
#include <fstream>
using namespace std;
#define SIZE 30
#define MAXLEN 110
#define OPPOSE -1
ifstream fin("in.txt");
ofstream fout("out.txt");
int opp[SIZE][SIZE];
int com[SIZE][SIZE];
int nTest,caseNum;
char str[MAXLEN];
char res[MAXLEN];
int s_len,resIdx;
int C,D,N;

int getIndex(char c) {
    return c - 'A' + 1;
}
char getChar(int idx) {
     return (char)(idx + 'A' - 1);
}
void init () {
     int i,j;
     for (i=0;i<SIZE;++i) {
         for (j=0;j<SIZE;++j) {
             com[i][j] = opp[i][j] = 0;
         }
     }
}
void readData() {
    string combine, oppose;
    int i,src,dst,val;
    fin >> C;
    for (i=1;i<=C;++i) {
        fin >> combine;            
        src = getIndex(combine[0]);
        dst = getIndex(combine[1]);
        val = getIndex(combine[2]);
        com[src][dst] = com[dst][src] = val;
    }
    fin >> D;
    for (i=1;i<=D;++i) {
        fin >> oppose;
        src = getIndex(oppose[0]);
        dst = getIndex(oppose[1]);
        val = OPPOSE;
        opp[src][dst] = opp[dst][src] = val;
    }
    fin >> N;
    fin >> str;
}
int main() {
    fin >> nTest;
    for (caseNum = 1; caseNum<=nTest; ++caseNum) {
        init();
        readData();
        s_len = strlen(str);
        res[0] = str[0];
        resIdx = 1;
        int i,j;
        for (i=1;i<s_len;++i) {
            int prevIdx, currIdx,isClear;
            currIdx = getIndex(str[i]);
            prevIdx = getIndex(res[resIdx-1]);
            //if combine then remove and replace
            if (com[prevIdx][currIdx] >= 1 && com[prevIdx][currIdx] <= 26) {
                 res[resIdx-1] = getChar(com[prevIdx][currIdx]);
                 continue;
            }
            //if oppose then clear
            isClear = 0;
            for (j=resIdx-1;j>=0;--j) {
                prevIdx = getIndex(res[j]);
                if (opp[prevIdx][currIdx] == OPPOSE) {
                   resIdx = 0;
                   if (i+1 < s_len) {
                      res[resIdx] = str[i+1];
                      ++i;
                      ++resIdx;
                   }            
                   isClear = 1;       
                   break;
                }
            }                        
            if (isClear == 1) {
               continue;
            }
            //else append
            else {
                 res[resIdx] = str[i];
                 ++resIdx;
            }
        }
        //print out
        fout <<"Case #" << caseNum << ": [";
        for (i=0;i<resIdx;++i) {
            if (i==0) {
               fout <<res[i];
            }
            else {
                 fout <<", "<<res[i];
            }
        }
        fout << "]\n";
    }
    return 0;
}
