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
ofstream fout ("C-large.out");
ifstream fin ("C-large.in");
#define cout fout
#define cin fin
int main() {
    int t;
    cin>>t;
    REP(T,t) {
        int n,x=0, sum=0, mn=1<<30, b;
        cin>>n;
        REP(i,n) cin>>b,x^=b, sum+=b, mn=min(mn,b);
        cout<<"Case #"<<T+1<<": ";
        if(x) cout<<"NO"<<endl;
        else cout<<sum-mn<<endl;
    }
    system("pause");
    return 0;
}
