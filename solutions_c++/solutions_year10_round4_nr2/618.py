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

int z,q,p,i,j,l,s,m,tab[1030],k,res,price[1030][1030];
bool used[1030][1030];

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d",&p);
    k=(1<<p);
    for (i=0;i<k;i++) scanf ("%d",&tab[i]);
    i=0;
    while (k>1) {
          k/=2;
          for (j=0;j<k;j++) {
              scanf ("%d",&price[i][j]);
              used[i][j]=false;
          }
          i++;
    }
    res=0;
    k=(1<<p);
    for (j=0;j<k;j++) {
        l=j/2; s=0;
        for (m=0;m<p;m++) {
            if (s>=tab[j]) used[s][l]=true;
            l/=2;
            s++;
        }
    }
    i=0;
    k=(1<<p);
    while (k>1) {
          k/=2;
          for (j=0;j<k;j++) if (used[i][j])
              res+=price[i][j];
          i++;
    }
    printf("Case #%d: %d\n",q,res);
}
return 0;
}
