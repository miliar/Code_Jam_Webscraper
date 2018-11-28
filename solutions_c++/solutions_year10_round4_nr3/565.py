#include <stdio.h>
#include<iostream>
#include<string>
#include<vector>
#include<map>
using namespace std;

const int maxn = 110;
int R;
int g[maxn][maxn];
int n,m;
bool update()
{
	int cnt=0;
	//for(int i=1;i<=n;i++){
	//	for(int j=1;j<=m;j++)cout<<g[i][j];cout<<endl;
	//}
	//cout<<endl;
	for(int i=n;i>=1;i--)
		for(int j=m;j>=1;j--)
		{
			if( g[i][j]==0 && g[i-1][j] && g[i][j-1] )
			{
				cnt++;
				g[i][j]=1;
			}
			else if( g[i][j] ==1 && (g[i-1][j] || g[i][j-1]) )
			{
				cnt++;
				g[i][j]=1;
			}
			else g[i][j]=0;
		}

	return (cnt>0);

}
int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	int i,j,k;
	int T;
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++)
	{
		cin>>R;
		int x1,y1,x2,y2;
		n=m=0;
		memset(g,0,sizeof(g));
		for(i=0;i<R;i++)
		{
			cin>>x1>>y1>>x2>>y2;
			if( x2 > n ) n=x2;
			if( y2 > m ) m=y2;
			for(j=x1;j<=x2;j++)
				for(k=y1;k<=y2;k++)g[j][k]=1;
		}

		for(k=1;;k++)
		{
			if( !update() )break;
		}
		printf("Case #%d: %d\n",ca,k);
	}
}
