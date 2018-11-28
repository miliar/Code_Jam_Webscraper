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

vector<char> wek;
int z,q,i,j,k,l,c,d,n,zm;
char l1,l2,tab1[40][3],tab2[40][2],t[105];

int main () {
scanf ("%d",&z);
for (q=1;q<=z;q++) {
    scanf ("%d",&c);
    for (i=0;i<c;i++) {
        scanf ("%s",&t);
        tab1[i][0]=t[0];
        tab1[i][1]=t[1];
        tab1[i][2]=t[2];
    }
    scanf ("%d",&d);
    for (i=0;i<d;i++) {
        scanf ("%s",&t);
        tab2[i][0]=t[0];
        tab2[i][1]=t[1];
    }
    scanf ("%d %s",&n,&t);
    wek.resize(0);
    for (i=0;i<n;i++) {
        wek.pb(t[i]);
        zm=1;
        while (wek.size()>1 && zm==1) {
              zm = 0; l1=wek[wek.size()-1]; l2=wek[wek.size()-2];
              for (j=0;j<c;j++) if ((tab1[j][0]==l1 && tab1[j][1]==l2) || (tab1[j][0]==l2 && tab1[j][1]==l1)) {
                  wek.pop_back(); wek.pop_back(); wek.pb(tab1[j][2]); zm=1; j=c;
              }
        }
        zm=0;
        for (j=0;j<wek.size();j++) for (k=0;k<wek.size();k++) for (l=0;l<d;l++) if (tab2[l][0]==wek[j] && tab2[l][1]==wek[k]) zm=1;
        if (zm==1) wek.resize(0);
    }
    printf("Case #%d: [",q);
    for (i=0;i<wek.size();i++) {
        if (i>0) printf(", ");
        printf("%c",wek[i]);
    }
    printf("]\n");
}
return 0;
}
