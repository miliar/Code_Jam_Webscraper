#include<cstdio>
#include<cstring>
typedef int arr[510][510];
int n,m,d,ans=0;
int a[510][510];
char s[1010];
arr sx,sy,ss;
int g(arr s,int x,int y){
	return s[x][y]-s[x-1][y]-s[x][y-1]+s[x-1][y-1];
}
int get(arr s,int x1,int x2,int y1,int y2){
	return s[x2][y2]-s[x1-1][y2]-s[x2][y1-1]+s[x1-1][y1-1]-g(s,x1,y1)-g(s,x1,y2)-g(s,x2,y1)-g(s,x2,y2);
}
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int TT=1;TT<=T;TT++){
		ans=0;
		scanf("%d%d%d",&n,&m,&d);
		for (int i=1;i<=n;i++){
			scanf("%s",s);
			for (int j=0;j<m;j++)a[i][j+1]=s[j]-'0';
		}
		memset(sx,0,sizeof sx);
		memset(sy,0,sizeof sy);
		for (int i=1;i<=n;i++){
			for (int j=1;j<=m;j++){
				sx[i][j]=a[i][j]*i+sx[i-1][j]+sx[i][j-1]-sx[i-1][j-1];
				sy[i][j]=a[i][j]*j+sy[i-1][j]+sy[i][j-1]-sy[i-1][j-1];
				ss[i][j]=a[i][j]+ss[i-1][j]+ss[i][j-1]-ss[i-1][j-1];
			}
		}
		for (int i=1;i<=n;i++){
			for (int j=1;j<m;j++){
				for (int k=2;i+k<=n&&j+k<=m;k++)if (k+1>ans){
					if (k%2==0){
						if (get(sx,i,i+k,j,j+k)-get(ss,i,i+k,j,j+k)*(i+k/2)==0&&
							get(sy,i,i+k,j,j+k)-get(ss,i,i+k,j,j+k)*(j+k/2)==0)
							ans=k+1;
					}else {
						if (get(sx,i,i+k,j,j+k)*2-get(ss,i,i+k,j,j+k)*(i*2+k)==0&&
							get(sy,i,i+k,j,j+k)*2-get(ss,i,i+k,j,j+k)*(j*2+k)==0)
							ans=k+1;
					}
				}
			}
		}
		if (ans<3)printf("Case #%d: IMPOSSIBLE\n",TT);
		else printf("Case #%d: %d\n",TT,ans);
	}
	return 0;
}
