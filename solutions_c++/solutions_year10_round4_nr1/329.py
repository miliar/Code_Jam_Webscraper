#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
const int N=200;
using namespace std;
char a[N][N];
int m,n;
bool ok(int i,int j){
	if(i<0||i>m||j<0||j>m)return false;
	if(i<n)return j>=(n-1)-i&&j<=(n-1)+i;
	return j>=(n-1)-(m-1-i)&&j<=(n-1)+(m-1-i);
}
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int i,j,k,t,tt=1,x,y,mx,mn;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		getchar();
		memset(a,0,sizeof(a));
		m=n*2-1;
		for(i=0;i<m;i++)
			gets(a[i]);
		mn=100;
		for(i=0;i<m;i++)
			for(j=0;j<m;j++){
				for(k=x=0;x<m;x++)
					for(y=0;y<m;y++){
						if(!ok(x,y))continue;
						if(ok(2*i-x,2*j-y)&&a[x][y]!=a[2*i-x][2*j-y])k=1;
						if(ok(x,2*j-y)&&a[x][y]!=a[x][2*j-y])k=1;
						if(ok(2*i-x,y)&&a[x][y]!=a[2*i-x][y])k=1;
					}
				if(k)continue;
				mx=0;
				for(x=0;x<m;x++)
					for(y=0;y<m;y++)
						if(ok(x,y))mx=max(mx,abs(i-x)+abs(j-y));
				mn=min(mn,mx+1);
			}
		printf("Case #%d: %d\n",tt++,mn*mn-n*n);
	}
	return 0;
}
