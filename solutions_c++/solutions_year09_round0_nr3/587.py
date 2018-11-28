#include <iostream>
#include <cstdio>
using namespace std;

#define MAXN 1000

char welcome[] = "#welcome to code jam";

int T[MAXN][20];

int testcase(){
    string Q; getline(cin, Q);
    string h = "#";
    string S = h + Q;
    int ss = S.size();
    for(int i=0; i<ss; ++i) for (int j=0; j<20; ++j) T[i][j] = 0;
    
    T[0][0] = 1;
    
    for(int i=0; i<ss; ++i) {
        for (int j=0; j<20; ++j) {
            if (S[i] == welcome[j]){
                for(int k=0; k<i; ++k){
                    T[i][j] += T[k][j-1];
                    T[i][j] %= 10000;
                }
            }
        }
    }
    
    int ret = 0;
    for(int i=0; i<ss; ++i) ret += T[i][19];
    return ret % 10000;
}

int main(){
int n; scanf("%d", &n);
string Q; getline(cin, Q); // getting rid of \n
for(int i=1; i<=n; ++i)
    printf("Case #%d: %04d\n", i, testcase());
return 0;
}
