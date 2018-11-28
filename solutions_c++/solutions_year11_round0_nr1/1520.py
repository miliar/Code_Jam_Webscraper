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

ofstream fout ("A-large.out");
//ofstream fout ("A.out");
ifstream fin ("A-large.in");
#define cout fout
#define cin fin

int main() {
    int t;
    cin>>t;
    REP(T,t) {
        int n, k;
        cin>>n;
        char c;
        int time=0, Opos=1, Bpos=1, Otime = 0, Btime = 0;
        REP(i,n) {
            cin>>c>>k;
            int t = 0;
            if(c=='O') {
                Otime += abs(Opos-k);
                Opos = k;
                Otime = max(Otime, time)+1;
            }
            else {
                Btime += abs(Bpos-k);
                Bpos = k;
                Btime = max(Btime, time)+1;
            }
            time = max(Btime, Otime);
            //cout<<Otime<<" "<<Btime<<" "<<time<<" "<<endl;
        }
        cout<<"Case #"<<T+1<<": "<<time<<endl;
    }
    system("pause");
    return 0;
}
    
