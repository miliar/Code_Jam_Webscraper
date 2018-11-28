#include<iostream>
#define fo(i,u,d) for(int i=u;i<=d;i++)
using namespace std;
int t1=1,tt;
int n,d[100][100],f[100],v[100];
char c;

int main(){
	freopen("al.in","r",stdin);
	freopen("a.out","w",stdout);
	for(scanf("%d",&tt);t1<=tt;t1++){
		scanf("%d\n",&n);
		fo(i,1,n){
			f[i]=v[i]=0;
			fo(j,1,n){
				scanf("%c",&c);
				d[i][j]=c=='1';
				if (c=='1')
					f[i]=j;
			}
			scanf("\n");		
		}
		int ans=0;
		fo(i,1,n){
			int k;
			fo(j,i,n)
				if (f[j]<=i){
					k=j;
					break;
				}
			for(int j=k-1;j>=i;j--){
				swap(f[j],f[j+1]);
				ans++;
			}
		}
		printf("Case #%d: %d\n",t1,ans);
	}
	return 0;
}
			
		
			
			
