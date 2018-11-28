#include<cstdio>
#include<cmath>
#define L 1000

using namespace std;

int v[L],p[L];
char r[L];
int T,n,i,ans,olast,blast;
int I=0;

int main(){
	scanf("%d",&T);
	while (T--){
		scanf("%d",&n);
		for (i=0;i<n;++i)
			scanf(" %c%d",&r[i],&p[i]);
		ans=0;
		olast=blast=-1;
		for (i=0;i<n;++i){
			if (r[i]=='B'){
				if (blast == -1)
					v[i]=p[i];
				else
					v[i]=abs(p[blast]-p[i])+v[blast]+1;
				blast = i;
			}
			else{
				if (olast==-1)
					v[i]=p[i];
				else
					v[i]=abs(p[olast]-p[i])+v[olast]+1;
				olast = i;
			}
			if (i>0 && v[i]<=v[i-1])
				v[i]=v[i-1]+1;
		}
		printf("Case #%d: %d\n",++I,v[n-1]);
	}
}
