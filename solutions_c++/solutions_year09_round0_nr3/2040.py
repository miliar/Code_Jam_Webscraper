//welcome to code jam
#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <algorithm>
#include <cstring>
using namespace std;

/*
01234567890123456789
welcome to code jam
*/

int sz;
char line[501];
char s[21] = {"welcome to code jam"};
int memo[21][501];

int main() {
    int t, T;
    int i, j;
    
    gets(line);
    T = atoi(line);
    
    for(t=1; t<=T; t++) {
       gets(line);
       sz = strlen(line);
       
       for(i=0; i<21; i++) memo[i][sz] = 0;
       for(i=sz-1; i>=0; i--) {
          for(j=18; j>=0; j--) {
             if( s[j]==line[i] ) {
                 if(j==18) memo[j][i] = (memo[j][i+1] + 1)%10000;
                 else memo[j][i] = (memo[j+1][i+1] + memo[j][i+1])%10000;
             }
             else {
                 memo[j][i] = memo[j][i+1];
             }
          }
       }
       
       printf("Case #%d: %04d\n", t, memo[0][0]);
    }
    
}
