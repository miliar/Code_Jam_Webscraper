#include <iostream>
#include <queue>
using namespace std;
#define fin "log.in"
#define fout "log.out"
#define NMAX 1001

int t;
long long r,n,k;
long long was[NMAX],g[NMAX],to[NMAX],c[NMAX];
queue<pair<long long,long long> > q;

int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	cin>>t;
	long long cur,iter,place,cost,ans;
	for (int i=0; i<t; ++i){
		while (!(q.empty()))
			q.pop();
		cin>>r>>k>>n;
		ans=0;
		for (int j=0; j<n; ++j){
			cin>>g[j];
			was[j]=to[j]=0;
			q.push(make_pair(g[j],j));
		}
		iter=0;
		cost=0;
		while ((was[q.front().second]==0)&&(r>0)){
			was[q.front().second]=1;
			place=k;
			cur=q.front().second;
			while ((place>=q.front().first) && ((cur!=q.front().second) || (place==k))){
				place-=q.front().first;
				q.push(q.front());
				q.pop();
			}
			to[cur]=q.front().second;
			c[cur]=k-place;
			ans+=c[cur];
			r--;
		}
		if (r!=0){
			cur=q.front().second;
			for (int j=0; j<n; ++j)
				was[j]=0;
			while (was[cur]==0){
				was[cur]=1;
				cost+=c[cur];
				cur=to[cur];
				iter++;
			}
			ans+=cost*(r/iter);
			r=r%iter;
			cur=q.front().second;
			while (r!=0){
				r--;
				ans+=c[cur];
				cur=to[cur];
			}
		}
		cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}
}