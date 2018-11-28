#include<cstdio>
const int N=50;
int T,n,a[N][N],b[N];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;t++){
		scanf("%d",&n);
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				scanf("%1d",&a[i][j]);
		for (int i=0;i<n;i++){
			b[i]=0;
			for (int j=0;j<n;j++)
				if (a[i][j])
					b[i]=j;
		}
		int ans=0;
		for (int i=0;i<n;i++){
			int k;
			for (int j=i;j<n;j++)
				if (b[j]<=i){
					k=j;break;
				}
			ans+=k-i;
			for (int j=k;j>i;j--)
				b[j]=b[j-1];
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
