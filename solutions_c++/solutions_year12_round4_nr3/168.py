//By Lin
#include<cstdio>
#include<cstring>
using namespace std; 

long long y[10005],x[10005];
int que[10005],n,v[10005]; 

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int t,h,i,j,k; 
	long long h1,h2,t1,t2;
	scanf("%d",&t);
	for(h=1;h<=t;h++)
	{
		scanf("%d",&n);
		for(i=1;i<n;i++)
			scanf("%lld", &x[i]);
		memset(y,0,sizeof(y));
		y[x[1]]=1e9; 
		int qb= 0 , qe=0; 
		que[qe++]=x[1]; 
		v[0]=1; 
		bool ab=true; 
		for(int i=2; i<=n-1; i++)
		{
			while(qb<qe && i >= que[qe-1])qe--;
			if(qb==qe){
				y[x[i]]=1e9; 
			}
			else {
				if(x[i] > que[qe-1]){
					ab=0; 
					break; 
				}
				if(x[i]==que[qe-1])continue; 
				h2=y[que[qe-1]]-y[i];
				t2=que[qe-1]-i;
				t1=x[i]-i;
				h1=h2*t1/t2; 
				if(h2*t1%t2 != 0)h1 ++; 
				y[x[i]]=h1 + y[i]; 
				h2=y[que[qe-1]]-y[v[qe-1]];
				h1=y[x[i]]-y[v[qe-1]];
				t2=que[qe-1]-v[qe-1];
				t1=x[i]-v[qe-1]; 
				if(h1*t2 >= h2*t1){ ab=0; break; } 
			}
			que[qe]=x[i];
			v[qe++]=i; 
		}
		printf("Case #%d:" , h); 
		if(!ab)printf(" Impossible\n");
		else {
			for(i=1; i<n; i++)
			{
				h1=y[x[i]]-y[i], t1=x[i]-i;
				for(j=i+1; j<x[i]; j++){
					h2=y[j]-y[i], t2=j-i; 
					if(h1*t2 <= h2*t1) ab=0; 
				}
				for(j=x[i]+1;j<=n;j++){
					h2=y[j]-y[i], t2=j-i; 
					if(h1*t2 < h2*t1)ab=0; 
				}
			}
			for(i=1;i<=n;i++)
				printf(" %lld" ,y[i]);
			printf("\n");
		}
	}
	return 0; 
}
