#include <stdio.h>
#include <algorithm>

using namespace std;

#define N 250

int T,d,n,m,p[N],v[N];
double t[N],tt[N];
double l,r,mid;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int lT,i,j;
	scanf("%d",&T);
	for(lT=1;lT<=T;lT++){
		m=0;

		scanf("%d%d",&n,&d);
		for(i=0;i<n;i++){
			scanf("%d%d",&p[i],&v[i]);
			for(j=0;j<v[i];j++){
				t[m++]=p[i];
			}
		}
		sort(t,t+m);

		l=0;r=d*m;
		while(r-l>=1e-7){
			mid=(l+r)/2;
			tt[0]=t[0]-mid;
			for(i=1;i<m;i++){
				if(tt[i-1]+d>t[i]+mid)break;
				if(tt[i-1]+d<t[i]-mid)
					tt[i]=t[i]-mid;
				else
					tt[i]=tt[i-1]+d;
			}
			if(i==m)r=mid;
			else l=mid;
		}

		printf("Case #%d: %.7lf\n",lT,r);
	}
	return 0;
}