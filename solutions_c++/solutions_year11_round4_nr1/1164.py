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
#include<iomanip>
#include<fstream>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair <int,int> ii;
typedef long long LL;
#define sz(a) int((a).size())
#define pb push_back
const int INF = 2147483647;
const double PI = 3.141592653589793;

struct P {
       int b,e,v;
};

int z,q,x,s,r,t,n,i,b[1005],e[1005],w[1005],k,d,v,add,kol[2005];
double suma,tt,d2;
P tab[2005];

bool cmp (int a, int b) {
     return tab[a].v < tab[b].v;
}

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d %d %d %d %d",&x,&s,&r,&t,&n);
    tt=t;
    add=r-s;
    for (i=0;i<n;i++) {
        scanf ("%d %d %d",&b[i],&e[i],&w[i]);
    }
    b[n]=x;
    tab[0].b=0; tab[0].e=b[0]; tab[0].v=s; kol[0]=0;
    for (i=0;i<n;i++) {
        tab[2*i+1].b=b[i]; tab[2*i+1].e=e[i]; tab[2*i+1].v=s+w[i]; kol[2*i+1]=2*i+1;
        tab[2*i+2].b=e[i]; tab[2*i+2].e=b[i+1]; tab[2*i+2].v=s; kol[2*i+2]=2*i+2;
    }
    sort (kol,kol+2*n+1,cmp);
    i=0;
    suma = 0.0;
    while (i<=2*n) {
          k = kol[i];
          d = tab[k].e - tab[k].b;
          v = tab[k].v;
          //printf("%d %d\n",d,v);
          d2 = min((v+add)*tt,d*1.0);
          tt -= d2 / (v+add);
          suma += d2 / (v+add);
          suma += (d-d2) / v;
          i++;
    }
    printf("Case #%d: %.8lf\n",q,suma);
}
return 0;
}
