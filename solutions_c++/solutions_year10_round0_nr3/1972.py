#include <stdio.h>
#include <vector>
using namespace std;

int main(){
	int t,r,k,n;
	vector<long long> g,v,tv;
	scanf("%d",&t);
	for (int tc=1;tc<=t;tc++){
		scanf("%d %d %d",&r,&k,&n);
		g.clear();g.resize(n,0);
		v.clear();v.resize(n,-1);
		tv.clear();tv.resize(n,0);
		for (int i=0;i<n;i++) scanf("%lld",&g[i]);
		int pos=0;
		int tr=0;
		long long res=0;
		for (;tr<r;tr++){
			if (v[pos]<0){
				int tres=0;
				v[pos]=res;
				tv[pos]=tr;
				for (int i=0;(i<n)&&(tres<k);i++){
					tres+=g[pos];
					pos=(pos+1)%n;
				}
				if (tres>k){
					pos=(pos-1+n)%n;
					tres-=g[pos];
				}
				res+=tres;
			}
			else{
				int tr2=((r-tr)/(tr-tv[pos]));
				res+=(res-v[pos])*tr2;
				tr+=(tr-tv[pos])*tr2;
				break;
			}
		}
		for (;tr<r;tr++){
			int tres=0;
			for (int i=0;(i<n)&&(tres<k);i++){
				tres+=g[pos];
				pos=(pos+1)%n;
			}
			if (tres>k){
				pos=(pos-1+n)%n;
				tres-=g[pos];
			}
			res+=tres;
		}
		printf("Case #%d: %lld\n",tc,res);
	}
}