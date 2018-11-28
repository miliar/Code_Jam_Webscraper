#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

#define MAXLEN 505

const char *srch = "welcome to code jam";
const int sLen = 19;
int M[MAXLEN][20];

int main() {
    string line;
    int nCase;
    cin>>nCase;
    getline(cin, line);
    for(int a=1; a<=nCase; a++) {
        getline(cin, line);
        for(int x=0; x<MAXLEN; x++) for(int y=0;y<20;y++) M[x][y] = 0;
        if(line[line.length()-1]==srch[sLen-1]) M[line.length()-1][sLen-1]++;
        for(int pos=line.length()-2; pos>=0; pos--) {
            M[pos][sLen-1] = M[pos+1][sLen-1];
            if(line[pos]==srch[sLen-1]) M[pos][sLen-1]++;
        }
        for(int lt=sLen-2; lt>=0; lt--) {
            for(int pos=line.length()-2; pos>=0; pos--) {
                M[pos][lt] = M[pos+1][lt];
                if(line[pos]==srch[lt]) {
                    M[pos][lt] += M[pos+1][lt+1];
                }
                M[pos][lt] %= 10000;
            }
        }
        cout<<"Case #"<<a<<": ";
        printf("%04d\n", M[0][0]);
    }
    return 0;
}
