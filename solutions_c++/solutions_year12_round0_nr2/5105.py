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

int l[105][3],d[105],n,q,z,i,s,p,res;

void jedz (int e) {
     int sup,r,i,j,k;
     if (e==n) {
        sup=0;
        r=0;
        for (i=0;i<n;i++) {
            if (l[i][2]-l[i][0]==2) sup++;
            if (l[i][2]>=p) r++;
        }
        if (sup==s) res=max(res,r);
        return;
     }
     for (i=0;i<=10;i++) for (j=i;j<=i+2;j++) for (k=j;k<=i+2;k++) if (i+j+k==d[e]) {
         l[e][0]=i;
         l[e][1]=j;
         l[e][2]=k;
         jedz(e+1);
     }
}

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d %d %d",&n,&s,&p);
    for (i=0;i<n;i++) scanf ("%d",&d[i]);
    res=0;
    jedz(0);
    printf("Case #%d: %d\n",q,res);
}
return 0;
}
