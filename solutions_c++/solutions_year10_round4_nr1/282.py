#include<cstdio>
#include<iostream>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<ctime>
using namespace std;
const int INF = 2147483647;
const double PI = 3.141592653589793;

int z,q,i,j,m,tab[150][150],k,res,wyn,akt,a,t,s,ss,tt;
bool good, good2;

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d",&k);
    for (i=1;i<=2*k-1;i++) for (j=1;j<=2*k-1;j++) tab[i][j]=-1;
    m = k+1; t=0;
    for (i=1;i<=2*k-1;i++) {
        if (i<=k) m--; else m++;
        if (i<=k) t++; else t--;
        for (j=m;j<m+2*t;j+=2)
            scanf ("%d",&tab[i][j]);
    }
    //for (i=1;i<=2*k-1;i++) 
    //for (j=1;j<=2*k-1;j++)
    //printf("%d %d %d\n",i,j,tab[i][j]);
    res = INF;
    for (i=1;i<=2*k-1;i++) 
        for (j=1;j<=2*k-1;j++) {
            good = true;
            for (s=1;s<i;s++) if (i+(i-s)<=2*k-1) {
                for (t=1;t<=2*k-1;t++) if (tab[s][t]!=-1 && tab[i+(i-s)][t]!=-1 && tab[s][t]!=tab[i+(i-s)][t]) {
                    good = false;
                    //printf
                }
            }
            //printf("%d %d %d\n",i,j,good);
            for (t=1;t<j;t++) if (j+(j-t)<=2*k-1) {
                for (s=1;s<=2*k-1;s++) if (tab[s][t]!=-1 && tab[s][j+(j-t)]!=-1 && tab[s][t]!=tab[s][j+(j-t)]) good = false;
            }
            //printf("%d %d %d\n",i,j,good);
            if (good) {
               akt = abs (i-k) + abs(j-k) + k;
               akt = akt * akt - k * k;
               //printf("%d %d %d\n",i,j,akt);
               res = min(res,akt);
            }
        }
    printf("Case #%d: %d\n",q,res);
}
return 0;
}
