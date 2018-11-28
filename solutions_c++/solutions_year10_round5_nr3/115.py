#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
typedef long long ll;
int C;
int cnt[10<<20];
typedef pair<int,int> P;
int main()
{
	int t;cin>>t;
	for(int a=1 ;a<=t; ++a) {
		memset(cnt,0,sizeof(cnt));
		cin>>C;
		priority_queue<P> q;
		for(int i=0; i<C; ++i) {
			int p,v;cin>>p>>v;
			p += 5<<20;
			cnt[p]=v;
			if (v>1) q.push(P(v,p));
		}
		ll r=0;
		while(!q.empty()) {
			P p=q.top();q.pop();
			int c=p.second;
			int x=cnt[c];
			if (x<2) continue;

			int a = x/2;
			r += a;
			cnt[c] -= 2*a;
			cnt[c-1] += a;
			cnt[c+1] += a;
			if (cnt[c-1]>1) q.push(P(cnt[c-1], c-1));
			if (cnt[c+1]>1) q.push(P(cnt[c+1], c+1));
		}
		cout<<"Case #"<<a<<": "<<r<<'\n';
	}
}
