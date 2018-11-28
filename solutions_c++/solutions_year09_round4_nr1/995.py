#include<iostream>
#include<cstdio>
#include<string>
using namespace std;

const	int maxn = 41;
char	a[maxn][maxn];
int		b[maxn];

int		main(){
		int i, j, k, n, t, T, tmp, ans;
	//	freopen("in.txt","r",stdin);
	//	freopen("out.txt","w",stdout);
		for(cin>>T, t=1; t<=T; t++){
			printf("Case #%d: ",t);
			cin>>n;
			for(i=1; i<=n; i++){
				b[i] = 0;
				for(j=1; j<=n; j++){
					cin>>a[i][j];
					if (a[i][j]=='1') b[i] = j;
				}
			}
			ans = 0;
			for(i=1; i<=n; i++){
				for(j=i; j<=n; j++) if (b[j]<=i) break;
				ans += j-i; 
				tmp = b[j];
				for(k=j; k>i; k--) b[k] = b[k-1];
				b[i] = b[j];
			}
			printf("%d\n",ans);
		}
		return 0;
}