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

int q,z,i,n,m,jest,good,ind,r,wyn,maxx,j,k;
string s[10005];
char t[30];
VI wek,wek2;

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d %d",&n,&m);
    for (i=0;i<n;i++) {
        scanf ("%s",&t);
        s[i]=t;
    }
    printf("Case #%d:",q);
    while (m--) {
          scanf ("%s",&t);
          maxx=-1;
          for (i=0;i<n;i++) {
              wek.resize(0);
              for (j=0;j<n;j++) if (s[j].size()==s[i].size()) wek.pb(j);
              ind = 0; r=0;
              while (wek.size() > 1) {
                    jest=0;
                    for (j=0;j<wek.size();j++) if (s[wek[j]].find(t[ind])!=string::npos) jest=1;
                    if (jest==1) {
                       if (s[i].find(t[ind])==string::npos) r++;
                       wek2.resize(0);
                       for (j=0;j<wek.size();j++) {
                           good=1;
                           for (k=0;k<s[i].size();k++) if ((s[i][k]==t[ind]) + (s[wek[j]][k]==t[ind]) == 1) good=0;
                           if (good) wek2.pb(wek[j]);
                       }
                       wek=wek2;
                    }
                    ind++;
              }
              if (r>maxx) {
                 maxx=r;
                 wyn=i;
              }              
          }
          printf(" %s",s[wyn].c_str());
    }
    printf("\n");
}
return 0;
}
