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

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define RREPEAT(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) RREPEAT(i,n-1,0)
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

ifstream fin ("B-large10.in");
#define cin fin
ofstream fout ("B-large10.out");
#define cout fout

int main() {
    int t;
    cin>>t;
    REP(T,t) {
		ll L,P,C;
		cin>>L>>P>>C;
		int cnt=0,ans=0;
		while(L*C<P) L*=C,cnt++;
		while(cnt>0) ans++,cnt/=2;
		cerr<<T+1<<endl;
		cerr<<L<<" "<<P<<" "<<C<<endl;
		cout<<"Case #"<<T+1<<": "<<ans<<endl;
    }
    system("pause");
    return 0;
}
