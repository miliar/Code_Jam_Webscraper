#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<long long, long long> PII;
const int INF = 1000000000;
long long t,r,k,n;
long long saved[1000000];
int main() {
	ifstream fin("C-large.in");
	ofstream fout("c-large.out");
	fin>>t;
	REP(test,t){
		memset(saved, 0, sizeof(saved));
		fin>>r>>k>>n;
		queue<PII> q;
		REP(i,n){
			long long tmp; fin>>tmp;
			q.push(PII(tmp, i));
		}
		map<queue<PII>, int > m;
		long long cnt = 0, ret = 0;
		while(cnt < r && m.find(q) == m.end()){
			m[q] = cnt;
			long long tot = 0;
			PII p = q.front();
			long long fi = p.second;
			bool ok = false;
			while(!ok && tot + p.first <= k){
				q.pop();
				tot += p.first;
				q.push(p);
				p = q.front();
				if(fi == p.second){
					ok = true;
				}
			}
			saved[cnt++] = tot;
			ret += tot;
		}	
		int start = m[q], mod = cnt - start;	
		//cout<<start<<" "<<mod<<endl;
		if(cnt != r){
			ret = 0;
			long long add = 0;
			REP(i,start)ret += saved[i];
			for(int i = 0;i<mod; i++)	add += saved[start + i];
			long long diff = (r-start) / mod;
			ret += (add * diff);	
			//cout<<start+(mod*diff)<<endl;		
			for(int i=0;i<(r-start)%mod;i++) ret += saved[start + i];
		}
		fout<<"Case #"<<(test+1)<<": "<<ret<<endl;
	}
    return 0;
}
