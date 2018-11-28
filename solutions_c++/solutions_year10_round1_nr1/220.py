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

int z,q,a,n,i,j,k,tab[55][55],bat[55][55];
bool wygr,wygb;
char t[55];

void sprawdzPoziome (int x, int y) {
     for (int i=1;i<a;i++) if (bat[x][y+i]!=bat[x][y]) return;
     if (bat[x][y]==1) wygr=true; if (bat[x][y]==2) wygb=true;
}

void sprawdzPionowe (int x, int y) {
     for (int i=1;i<a;i++) if (bat[x+i][y]!=bat[x][y]) return;
     if (bat[x][y]==1) wygr=true; if (bat[x][y]==2) wygb=true;
}

void sprawdzUkosne1 (int x, int y) {
     for (int i=1;i<a;i++) if (bat[x+i][y+i]!=bat[x][y]) return;
     if (bat[x][y]==1) wygr=true; if (bat[x][y]==2) wygb=true;
}

void sprawdzUkosne2 (int x, int y) {
     for (int i=1;i<a;i++) if (bat[x-i][y+i]!=bat[x][y]) return;
     if (bat[x][y]==1) wygr=true; if (bat[x][y]==2) wygb=true;
}

int main() {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d %d",&n,&a);
    for (i=0;i<n;i++) {
        scanf ("%s",&t);
        for (j=0;j<n;j++) {
            if (t[j]=='.') tab[i][j]=0;
            if (t[j]=='R') tab[i][j]=1;
            if (t[j]=='B') tab[i][j]=2;
        }
    }
    for (i=n-1;i>=0;i--) {
        k=n-1;
        for (j=n-1;j>=0;j--) if(tab[i][j]) {
            bat[k][n-1-i]=tab[i][j];
            k--;
        }
        for (k=k;k>=0;k--) bat[k][n-1-i]=0;
    }
    wygr=wygb=false;
    for (i=0;i<n;i++) for (j=0;j<n-a+1;j++) sprawdzPoziome(i,j);
    for (i=0;i<n-a+1;i++) for (j=0;j<n;j++) sprawdzPionowe(i,j);
    for (i=0;i<n-a+1;i++) for (j=0;j<n-a+1;j++) sprawdzUkosne1(i,j); 
    for (i=a-1;i<n;i++) for (j=0;j<n-a+1;j++) sprawdzUkosne2(i,j);
    if (wygr && wygb) printf("Case #%d: Both\n",q); 
    if (wygr && !wygb) printf("Case #%d: Red\n",q); 
    if (!wygr && wygb) printf("Case #%d: Blue\n",q); 
    if (!wygr && !wygb) printf("Case #%d: Neither\n",q); 
}
return 0;
}
