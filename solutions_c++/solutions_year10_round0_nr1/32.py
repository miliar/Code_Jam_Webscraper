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

int z,n,k,i,q,l,m;

int main() {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d %d",&n,&k);
    l=k+1;m=1;
    while (l%2==0) {
          m++;
          l/=2;
    }
    for (i=1;i<n;i++) k/=2;
    if (k%2 && n<=m) printf("Case #%d: ON\n",q);
    else printf("Case #%d: OFF\n",q);
}
return 0;
}
