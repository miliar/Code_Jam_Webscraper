#include<queue>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<map>
#include<fstream>
using namespace std;
#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define rep(i,n) for(int i=0;i<n;i++)
#define pb push_back
#define sz size()
#define psi pair<string,int>
#define all(x) x.begin(),x.end()
#define GI ({int t;scanf("%d",&t); t;})
#define flush(x) memset(x,0,sizeof(x))
#define ll long long
int main() {
	int t=GI,cases=1;
	while(t--) {
		int n=GI,lbtime=0,lotime=0,bpos=1,opos=1,t=0;
		rep(i,n) {
			char m;
			int pos;
			cin>>m>>pos;
			if(m=='O') {
				int reachable_time = lotime + abs(pos-opos)+1;
				if(reachable_time<=t) t+=1;
				else t=reachable_time;
				lotime = t, opos=pos;
			}
			else {
				int reachable_time = lbtime + abs(pos-bpos)+1;
				if(reachable_time<=t) t+=1;
				else t=reachable_time;
				lbtime = t, bpos=pos;
			}
		}
		cout<<"Case #"<<cases<<": "<<t<<endl;
		cases++;
	}
}





