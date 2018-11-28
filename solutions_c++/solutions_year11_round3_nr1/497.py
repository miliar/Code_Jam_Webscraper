#include <string.h>
#include <string>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <vector>
#include <map>
#include <math.h>
#include <stdio.h>
using namespace std;
int t;
int main(){
    scanf("%d",&t);
    for (int T=0;T<t;T++){
        int r,c;
        char s[100][100];
        scanf("%d %d",&r,&c);
        for (int i=0;i<r;i++) scanf("%s",s[i]);
        bool b=true;
        for (int i=0;i<r;i++)
        for (int j=0;j<c;j++){
            if (s[i][j]=='#'){
                if (i+1>=r) {b=false; continue;}
                if (j+1>=c) {b=false; continue;}
                if (s[i+1][j]!='#') {b=false; continue;}
                if (s[i][j+1]!='#') {b=false; continue;}
                if (s[i+1][j+1]!='#') {b=false; continue;}
                s[i][j]='/';
                s[i][j+1]='\\';
                s[i+1][j]='\\';
                s[i+1][j+1]='/';
                }
            }
        if (!b) printf("Case #%d:\nImpossible\n",T+1); else {
            printf("Case #%d:\n",T+1);
            for (int i=0;i<r;i++) printf("%s\n",s[i]);
            }
        }
    return 0;
    }
