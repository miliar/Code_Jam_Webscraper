// By mirosuaf
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 


int zmien(string s) {
    return 60*(int(s[0]-'0')*10+int(s[1]-'0'))+int(s[3]-'0')*10+int(s[4]-'0');
    }

int main() {
int ile;
scanf("%d",&ile);

REP(iile,ile) {
int c1,c2,t,na,nb;
vector< pair<pair<int,int>,int> > tab;
scanf("%d",&t);
scanf("%d%d",&na,&nb);
char s1[200],s2[200];
string w1,w2;

REP(i,na) {
    scanf("%s%s",s1,s2);
    w1=s1; w2=s2;
    c1=zmien(w1); c2=zmien(w2);
    tab.push_back(make_pair(make_pair(c1,c2),0));
    }
        
REP(i,nb) {
    scanf("%s%s",s1,s2);
    w1=s1; w2=s2;
    c1=zmien(w1); c2=zmien(w2);
    tab.push_back(make_pair(make_pair(c1,c2),1));
    }

sort(tab.begin(),tab.end());

//REP(i,tab.size()) { cout << tab[i].first.first << "--" << tab[i].first.second << " ---> " << tab[i].second << endl;  }

int wynik[2]; wynik[0]=0; wynik[1]=0;
bool used[1000];
int earliest,how;

REP(i,tab.size()) used[i]=false;

REP(i,tab.size()) if (used[i]==false) {
    earliest=tab[i].first.second+t;
    how=tab[i].second;
    
    wynik[tab[i].second]++;    
    
    FOR(j,i+1,tab.size()-1) if (used[j]==false && tab[j].second==(how+1)%2 && tab[j].first.first>=earliest) {
		used[j]=true;
		how=(how+1)%2;
		earliest=tab[j].first.second+t;
		}	
    
}
printf("Case #%d: %d %d\n",iile+1,wynik[0],wynik[1]);
}

return 0;
}
