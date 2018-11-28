#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
bool flag[35][35];
int map[35][35];

char a[35][35];
int bian[40];
	int m,n,bianchang;
void test(int x,int y,int num){
	int i,j;
	int ok=1;
	for(i=x;i<x+num;i++)
	{
		for(j=y;j<y+num;j++){
			if(flag[i][j]) {ok=0;break;}
			else{
				if(j+1<y+num&&map[i][j]==map[i][j+1]) {ok=0;break;}
				if(j-1>=y&&map[i][j]==map[i][j-1]) {ok=0;break;}
				if(i+1<x+num&&map[i][j]==map[i+1][j]) {ok=0;break;}
				if(i-1>=x&&map[i][j]==map[i-1][j]) {ok=0;break;}
			}
		}
		if(ok==0) break;
	}
	if(ok==1){
		bian[num]++;
		for(i=x;i<x+num;i++)
			for(j=y;j<y+num;j++)
				flag[i][j]=true;
	}
}
int jishu=0;
void solve(){
	int i;
	int ans=0;
	for(i=1;i<=bianchang;i++) if(bian[i]>0) ans++;
	printf("Case #%d: %d\n",jishu,ans);
	for(i=bianchang;i>=1;i--){
		if(bian[i]>0) printf("%d %d\n",i,bian[i]);
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out3.txt","w",stdout);
	int t;
	scanf("%d",&t);

	int yxc;
	int i,j,k;
	while(t--){
		jishu++;
		scanf("%d%d",&m,&n);
		memset(bian,0,sizeof(bian));
		memset(flag,0,sizeof(flag));
		getchar();
		for(i=0;i<m;i++){
			scanf("%s",a[i]);
			for(j=0;j<n/4;j++){
				
				if(a[i][j]>='0'&&a[i][j]<='9') yxc=a[i][j]-'0';
				else yxc=a[i][j]-'A'+10;
				
				if(yxc>=8) {map[i][4*j+0]=1;yxc-=8;}
				else map[i][4*j+0]=0;
				if(yxc>=4) {map[i][4*j+1]=1;yxc-=4;}
				else map[i][4*j+1]=0;
				if(yxc>=2) {map[i][4*j+2]=1;yxc-=2;}
				else map[i][4*j+2]=0;
				if(yxc>=1) {map[i][4*j+3]=1;yxc-=1;}
				else map[i][4*j+3]=0;
			}
		}
		bianchang=(m>n?n:m);
		
		for(k=bianchang;k>=1;k--){
			for(i=0;i+k-1<m;i++){
				for(j=0;j+k-1<n;j++){
					test(i,j,k);
				}
			}
		}
		solve();	
	}
	
	return 0;
}