#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <map>

#define LL long long
#define pii pair<int, int>

using namespace std;

int main() {
    int ntc,n=4;
    char mat[10][10];
    char tmp[10];
    scanf("%d",&ntc);
    for (int tc=1;tc<=ntc;tc++) {
        for (int i=0;i<n;i++) {
            scanf("%s",mat[i]);
        }
        //scanf("%s",tmp);
        //for (int i=0;i<n;i++) {
        //    printf("%s\n",mat[i]);
        //}
        bool comp=true;
        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                if (mat[i][j]=='.') comp=false;
            }
        }
        bool xwin=false, owin=false;
        for (int i=0;i<n;i++) {
            if (xwin || owin) break;
            int x=0,o=0,t=0;
            for (int j=0;j<n;j++) {
                if (mat[i][j]=='X') x++; 
                else if (mat[i][j]=='O') o++;
                else if (mat[i][j]=='T') t++;
            }
            if (x==4) xwin=true;
            if (x==3 && t==1) xwin=true;    
            if (o==4) owin=true;
            if (o==3 && t==1) owin=true;
        }
        for (int i=0;i<n;i++) {
            if (xwin || owin) break;
            int x=0,o=0,t=0;
            for (int j=0;j<n;j++) {
                if (mat[j][i]=='X') x++; 
                else if (mat[j][i]=='O') o++;
                else if (mat[j][i]=='T') t++;
            }
            if (x==4) xwin=true;
            if (x==3 && t==1) xwin=true;    
            if (o==4) owin=true;
            if (o==3 && t==1) owin=true;
        }
        int x=0,o=0,t=0;
        for (int i=0;i<n;i++) {
            if (mat[i][i]=='X') x++; 
            else if (mat[i][i]=='O') o++;
            else if (mat[i][i]=='T') t++;
        }
       if (x==4) xwin=true;
       if (x==3 && t==1) xwin=true;    
       if (o==4) owin=true;
       if (o==3 && t==1) owin=true;
       
       x=0,o=0,t=0;
       for (int i=0;i<n;i++) {
            if (mat[i][n-i-1]=='X') x++; 
            else if (mat[i][n-i-1]=='O') o++;
            else if (mat[i][n-i-1]=='T') t++;
        }
        
       if (x==4) xwin=true;
       if (x==3 && t==1) xwin=true;    
       if (o==4) owin=true;
       if (o==3 && t==1) owin=true;
       
        printf("Case #%d: ",tc);
        if (xwin) printf("X won\n");
        else if (owin) printf("O won\n");
        else if (!comp) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
