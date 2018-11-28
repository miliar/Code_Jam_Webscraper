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

int z,q,d,k,a,p[2],n[2],res,dist;
char t[2];

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d",&d);
    p[0]=p[1]=1; n[0]=n[1]=0; res=0;
    while (d--) {
          scanf ("%s %d",&t,&a);
          k = (t[0]=='O');  
          dist = abs(p[k]-a);
          dist = max(dist-n[k],0) + 1;
          res += dist;
          p[k] = a;
          n[1-k] += dist;
          n[k] = 0;
    }
    printf("Case #%d: %d\n",q,res);
}
return 0;
}
