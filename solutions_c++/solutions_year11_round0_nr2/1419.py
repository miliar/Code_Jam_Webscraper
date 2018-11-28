#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define FOR(i,a,b) for(int i=a;i<b;++i)
#define RFOR(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) FOR(i,0,n)
#define RREP(i,n) RFOR(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll unsigned long long int
#define uli unsigned long int
#define MAX (int)1e6

using namespace std;
ofstream fout ("B-large.out");
//ofstream fout ("B.out");
ifstream fin ("B-large.in");
#define cout fout
#define cin fin
int C, D, N;
string s;
map< pair<char,char>, char> combine;
set< pair<char,char> > oppose;

bool Oppose(char c, vector<char> v) {
    REP(i,v.size())
        if(oppose.count(mkp(v[i],c)))
            return true;
    return false;
}
int main() {
    int t;
    cin>>t;
    REP(T,t) {
        combine.clear();
        oppose.clear();          
        cin>>C;
        REP(i,C) cin>>s, combine[mkp(s[0],s[1])] = s[2], combine[mkp(s[1],s[0])] = s[2];
        cin>>D;
        REP(i,D) cin>>s, oppose.insert(mkp(s[0],s[1])), oppose.insert(mkp(s[1],s[0]));
        cin>>N>>s;
        vector<char> ans;
        
        REP(i,N) {
            if(ans.size()>0) {
                if(combine.count(mkp(ans[ans.size()-1], s[i])))
                    ans[ans.size()-1]=combine[mkp(ans[ans.size()-1], s[i])];
                else if(Oppose(s[i],ans))
                    ans.clear();
                else
                    ans.pb(s[i]);
            }
            else ans.pb(s[i]);
        }
        
        cout<<"Case #"<<T+1<<": [";
        REP(i, ans.size()) {
            if(i) cout<<", ";
            cout<<ans[i];
        }cout<<"]"<<endl;
        
    }
    system("pause");
    return 0;
}
