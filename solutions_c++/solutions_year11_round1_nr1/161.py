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

int z,q,minn,pd,pg;
LL n;

void nie () {
     printf("Case #%d: Broken\n",q);
}

int nwd (int a, int b) {
    if (b==0) return a;
    return nwd(b,a%b);
}

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
      cin >> n >> pd >> pg;
      minn = 100/nwd(100,pd);
      if (minn > n) {nie(); continue;}
      if (pd != 0 && pg == 0) {nie(); continue;}
      if (pd != 100 && pg == 100) {nie(); continue;}
      printf("Case #%d: Possible\n",q);
}
return 0;
}
