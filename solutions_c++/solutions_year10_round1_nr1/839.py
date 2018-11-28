#include<cstdio>
#include<cstring>

using namespace std;
const int d[8][2]={{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1},{-1,-1}};
char s[55][55];
int n,k;
void input()
{
	scanf("%d%d",&n,&k);
	for(int i=0;i<n;++i)
		scanf("%s",s[i]);	
}
void rotate()
{
	for(int i=0;i<n;++i)
	{
		int j=n-1;
		for(int l=n-1;l>=0;--l)
		if(s[i][l]=='.'){
			if(j>=l) j=l-1;
			while(j>=0 && s[i][j]=='.') j--;			
			if(j<0) break;
			s[i][l]=s[i][j];
			s[i][j]='.';
		}
	}
	/*
		printf("\n");
		for(int i=0;i<n;++i)
			printf("%s\n",s[i]);				
	*/
}
bool ok(int x,int y)
{
	return x>=0 && x<n && y>=0 && y<n;
}
int solve()
{
	int ret=0;
	for(int i=0;i<n;++i)
		for(int j=0;j<n;++j)		
			if(s[i][j]!='.')
			for(int dir=0;dir<4;++dir)
			{
				int rdir=(dir+4)%8;
				int cnt=1;
				
				int x=i+d[dir][0];
				int y=j+d[dir][1];
				while(ok(x,y) && s[x][y]==s[i][j]) x+=d[dir][0],y+=d[dir][1],cnt++;
				
				x=i+d[rdir][0];
				y=j+d[rdir][1];
				while(ok(x,y) && s[x][y]==s[i][j]) x+=d[rdir][0],y+=d[rdir][1],cnt++;
				
				if(cnt>=k)	{
					if(s[i][j]=='R') ret|=1;
					else ret|=2;
					if(ret==3) return ret;
				}
			}		
	return ret;
}
int main()
{
	freopen("rotate.in","r",stdin);	
	freopen("rotate.out","w",stdout);
	int cs;
	scanf("%d",&cs);
	for(int t=1;t<=cs;++t)
	{
		printf("Case #%d: ",t);
		input();
		rotate();
		int ans=solve();
		if(ans==0) printf("Neither\n");
		else if(ans==1) printf("Red\n");
		else if(ans==2) printf("Blue\n");
		else printf("Both\n");
	}
}
