#include <cstdio>
#include <cstring>
#define N 1005
using namespace std;
double AC=0;
int TC,n,a[N],v[N],x,t;
int main(){
	scanf("%d",&TC);
	for (int TTC=1;TTC<=TC;TTC++){
		
		scanf("%d",&n);
		AC=0.0;
		
		for (int i=1;i<=n;i++)
			scanf("%d",&a[i]);
		memset(v,0,sizeof(v));
		
		for (int i=1;i<=n;i++)
			if (!v[i]){
				x=i;
				t=0;
				do{
					v[x]=1;
					x=a[x];
					t++;
				}while (x!=i);
				
				if (t>1) AC+=1.0*t;
			}
		printf("Case #%d: %.6lf\n",TTC,AC);
	}
	//scanf("\n");
	return 0;
}
