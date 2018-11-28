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

int i,mapa[400],j,ind,q,z;
char t[200];
string s1,s2,s;

int main () {
/*for (j=0;j<3;j++) {
    fgets(t,sizeof(t),stdin); s1=t;
    fgets(t,sizeof(t),stdin); s2=t;
    for (i=0;i<s1.size();i++) mapa[int(s1[i])]=int(s2[i]);
}
mapa[113]=122;
for (i=97;i<=122;i++) {
    ind=-1;
    for (j=97;j<=122;j++) if (mapa[j]==i) ind=0;
    if (ind==-1) mapa[122]=i;
}
for (i=97;i<=122;i++) printf("mapa[%d]=%d;\n",i,mapa[i]);*/
mapa[97]=121;
mapa[98]=104;
mapa[99]=101;
mapa[100]=115;
mapa[101]=111;
mapa[102]=99;
mapa[103]=118;
mapa[104]=120;
mapa[105]=100;
mapa[106]=117;
mapa[107]=105;
mapa[108]=103;
mapa[109]=108;
mapa[110]=98;
mapa[111]=107;
mapa[112]=114;
mapa[113]=122;
mapa[114]=116;
mapa[115]=110;
mapa[116]=119;
mapa[117]=106;
mapa[118]=112;
mapa[119]=102;
mapa[120]=109;
mapa[121]=97;
mapa[122]=113;
scanf ("%d\n",&z);
for (q=1;q<=z;q++) {
    fgets(t,sizeof(t),stdin);
    s=t;
    for (i=0;i<=s.size();i++) if (int(s[i])<=122 && int(s[i])>=97) s[i]=char(mapa[int(s[i])]);
    printf("Case #%d: %s",q,s.c_str());
}
return 0;
}
