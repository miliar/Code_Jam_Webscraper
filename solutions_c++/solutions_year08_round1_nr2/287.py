#include<iostream>
#include<algorithm>
#include<cmath>
#include<cassert>
#include<vector>
using namespace std;

typedef vector< pair<int,int> > vii;
#define pb push_back
vii p[128];

int n,m,re;
int x[16];
bool search(int pos,int cnt){
	if(cnt==re){
		bool sat=true;
		for(int i=0;i<m;i++){
			bool sp=false;
			for(int j=0;j<p[i].size();j++){
				if(x[p[i][j].first]==p[i][j].second){
					sp=true;
					break;
				}
			}
			if(sp==false){
				sat=false;
				break;
			}
		}
		return sat;
	}else if(pos>=n||cnt>re){
		return false;
	}else{
		x[pos]=1;
		if(search(pos+1,cnt+1))
			return true;
		x[pos]=0;
		if(search(pos+1,cnt))
			return true;
		return false;
	}
}
int main()
{	

	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out","w",stdout);

	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		int i;
		scanf("%d",&n);
		scanf("%d",&m);
		for( i=0;i<m;i++){
			p[i].clear();
			int t;
			scanf("%d",&t);
			while(t--){
				int x,y;
				scanf("%d%d",&x,&y);
				p[i].pb(make_pair(x-1,y));
			}
		}
		bool get=false;
		for(re=0;re<=n;re++){
			memset(x,0,sizeof(x));
			get=search(0,0);
			if(get) break;				
		}
		if(!get){
			printf("IMPOSSIBLE\n");
		}else{
			for(i=0;i<n;i++ ){
				printf("%d",x[i]);
				if(i==n-1) printf("\n");
				else printf(" ");
			}
		}
	}
	return 0;
}