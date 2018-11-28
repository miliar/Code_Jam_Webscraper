#include<cstdio>
#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>
#include<utility>
#include<map>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<list>
using namespace std;
#define F(x,a,b) for(x=a;x<=b;++x)
int main(){
	freopen("bin.txt","r",stdin);
	freopen("bou.txt","w",stdout);
	int C,cc,i,n,d,p[256],v[256],j,k,N;
	double l,r,m,q;bool ok;
	scanf("%d",&C);
	F(cc,1,C){
		scanf("%d%d",&n,&d);N=0;
		F(i,0,n-1){scanf("%d%d",p+i,v+i);N+=v[i];}
		l=0;r=1e10;
		F(j,0,100){
			vector< pair<double,double> > L;
			m=0.5*(l+r);
			F(i,0,n-1)F(k,1,v[i])
				L.push_back(make_pair(p[i]+m,p[i]-m));
			sort(L.begin(),L.end());
			ok=true;q=-1e20;
			F(i,0,N-1)if(q+d>L[i].first){ok=false;break;}
				else{
					q+=d;if(q<L[i].second)q=L[i].second;
				}
			if(ok)r=m;else l=m;
		}
		printf("Case #%d: %.8lf\n",cc,r);
	}
	return 0;
}
