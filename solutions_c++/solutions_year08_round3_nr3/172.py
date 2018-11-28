#include <iostream>
#include <algorithm>
using namespace std;

__int64 ans[1010];
__int64 a[1010];
__int64 b[1010];

__int64 out;
__int64 x,y,z;

int main()
{
	int T,t;
	int i,j;
	int n,m;
	

	freopen("C-small-attempt1.out","w",stdout);
	freopen("C-small-attempt1.in","r",stdin);

	scanf("%d",&T);
	for(t=1;t<=T;t++){
		
		scanf("%d%d%I64d%I64d%I64d",&n,&m,&x,&y,&z);
		
		for(i=0;i<m;i++)
			scanf("%I64d",&a[i]);
	
		for(i=0;i<n;i++){
			b[i]=a[i%m];
		
			a[i%m]=(x*a[i%m]+y*(i+1))%z;
			

		}
	

		memset(ans,0,sizeof(ans));
		for(i=0;i<n;i++){
			ans[i]++;
			for(j=i+1;j<n;j++){
				if (b[j]>b[i])
					ans[j]=(ans[j]+ans[i])% 1000000007;
			}
		}

		out = 0; 
		for(i=0;i<n;i++){
			out=(out+ans[i])%1000000007;
		}

		printf("Case #%d: %I64d\n",t,out);
	}
	return 0;
}
