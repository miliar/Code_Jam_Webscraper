#include<cstdio>
#include<algorithm>
using namespace std;
int c,d,t,y,w,n,a[1000005],ok;
double ac,x,f,e,mid,b[1000005];
int main(){
	scanf("%d",&t);
	for (int z=1; z<=t; z++){
		scanf("%d%d",&c,&d);
		n=0;
		while (c--){
			  scanf("%d%d",&w,&y);
			  for (int i=0; i<y; i++)
			      a[++n]=w;
		}
		sort(a+1,a+n+1);
		f=0; e=100000;
		while ((e-f)>1e-8){
			  mid=(f+e)/2;
			  for (int i=1; i<=n; i++) b[i]=a[i];
			  b[1]-=mid; ok=1;
			  for (int i=2; i<=n; i++){
				  if (b[i]-b[i-1]>=d){
					 if (b[i]-b[i-1]-d>mid) b[i]-=mid;
					 else b[i]=b[i-1]+d;
				  }
				  else{
					   if (b[i-1]+d-b[i]<mid) b[i]=b[i-1]+d;
					   else{ok=0; }
				  }
			  }
			  for (int i=2; i<=n; i++)
			      if (b[i]-b[i-1]<d) {ok=0;}
			  if (ok) e=mid;
			  else f=mid;
		}
		ac=(f+e)/2;
		printf("Case #%d: %lf\n",z,ac);
	}
	return 0;
}
