#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i= (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

map<pair<char,char>,char> combine;
map<char,char> oppose;
vector<char> V;
char s[5],str[105];
int c,d,n,junk;

pair<char,char> pairup(char a,char b) {
    char mini = min(a,b);
    char maxi = max(a,b);
    return mp(mini,maxi);
}

int main() {
    int test; scanf("%d",&test); REP(tt,test) {
        combine.clear();
        oppose.clear();
        V.clear();
        scanf("%d",&c);
        REP(i,c) {
            getchar();
            scanf("%s",s);
            combine[pairup(s[0],s[1])] = s[2];
        }
        scanf("%d",&d);
        REP(i,d) {
            getchar();
            scanf("%s",s);
            oppose[s[0]] = s[1];
            oppose[s[1]] = s[0];
        }
        scanf("%d",&junk);
        scanf("%s",str);
        int len = strlen(str);
        REP(i,len) {
            char ch = str[i];
            if(V.empty() || combine.find(pairup(V.back(),ch)) == combine.end()) V.pb(ch);
            else {char res = combine[pairup(V.back(),ch)]; V.pop_back(); V.pb(res); }

            char back = V.back();
            if(oppose.find(back) != oppose.end()) {
                char f = oppose[back];
                bool found = false;
                REP(i,sz(V)) if(V[i] == f) found = true;
                if(found) V.clear();
            }
        }
        printf("Case #%d: [",tt+1);
        REP(i,sz(V)) {
            printf("%c",V[i]);
            if(i+1 < sz(V)) printf(", ");
        }
        printf("]\n");
    }
}
