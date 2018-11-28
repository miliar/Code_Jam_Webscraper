#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define MAX(x,y) (x<y?y:x)
#define MIN(x,y) (x>y?y:x)

int ppos[1000005];
int nv;
bool clac(double t,int d){
	double p=ppos[0]-t;
	for(int i=1;i<nv;i++){
		double tp=MAX((p+d),(ppos[i]-t));
		if((tp-ppos[i])>t) return false;
		p=tp;
	}
	return true;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("Bl.out","w",stdout);
	
	int t,cas=0;
	scanf("%d",&t);
	while(t--){
		int c,d;
		scanf("%d%d",&c,&d);
		nv=0;
		for(int i=0;i<c;i++){
			int v,p;
			scanf("%d%d",&p,&v);
			for(int j=0;j<v;j++){
				ppos[nv++]=p;
			}
		}
		sort(ppos,ppos+nv);
		double low=0.0,high=nv*1.0*d;
		double mid=(low+high)/2.0,ans=mid;
		while(high-low>1e-4){
			if(clac(mid,d)){
				high=(ans=mid);
			}else{
				low=mid;
			}
			mid=(high+low)/2.0;
		}
		printf("Case #%d: %.3lf\n",++cas,ans);
	}
}