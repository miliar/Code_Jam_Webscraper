#include<iostream>
#include <cstring>
using namespace std;
char s[55][55];
struct node{
	int x,y;
}f[3000];
int n,m;
int fortex(int x,int y,int len){
	int i;
	if (s[x][y]!='#'||s[x+1][y]!='#'||s[x][y+1]!='#'||s[x+1][y+1]!='#'||x>=n-1||y>=m-1)
	{
		return 0;
	}
	for (i=0;i<len;++i)
	{
		if (x<f[i].x+2&&x>=f[i].x&&y<f[i].y+2&&y>=f[i].y)
		{
			return 0;
		}
	}
	return 1;
}
void bfs(int x,int y,int &cnt,int &len){
	if (cnt==0)
	{
		return ;
	}
	int i,j;
		if (fortex(x,y,len))
		{
			f[len].x=x,f[len++].y=y;
			cnt-=4;
		}
		if (cnt==0)
		{
			return;
		}
	for (j=y+1;j<m-1;++j)
	{
		if (s[x][j]=='#')
		{
			if (fortex(x,j,len))
			{
				bfs(x,j,cnt,len);
				if (cnt==0)
				{
					return;
				}
				len--;
				cnt+=4;
			}
			
		}
	}
	for (i=x+1;i<n-1;++i)
	{
		for (j=0;j<m-1;++j)
		{
			if (s[i][j]=='#')
			{
				if (fortex(i,j,len)==1)
				{
					bfs(i,j,cnt,len);
					if (cnt==0)
						return;
					len--;
					cnt+=4;
				}
			}
		}
	}
}
int main(){
	int txt,cas=1,i,j,cnt;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&txt);
	while(txt--){
		scanf("%d%d",&n,&m);
		cnt=0;
		for (i=0;i<n;++i)
		{
			scanf("%s",s[i]);
			for (j=0;j<m;++j)
			{
				if (s[i][j]=='#')
				{
					cnt++;
				}
			}
		}
		printf("Case #%d:\n",cas++);
		if (cnt%4!=0)
		{
			puts("Impossible");
			continue;
		}
		int len=0;
		for (i=0;i<n-1;++i)
		{
			for (j=0;j<m-1;++j)
			{
				if(s[i][j]=='#')
					break;
			}
			if (j<m-1)
			{
				break;
			}
		}
		if(i!=n-1&&j!=m-1&&fortex(i,j,0))
		{
			bfs(i,j,cnt,len);
		}
		for (i=0;i<len;++i)
		{
			s[f[i].x][f[i].y]='/';
			s[f[i].x][f[i].y+1]='\\';
			s[f[i].x+1][f[i].y]='\\';
			s[f[i].x+1][f[i].y+1]='/';
		}
		if (cnt!=0)
		{puts("Impossible");
		continue;
		}
		for (i=0;i<n;++i)
			puts(s[i]);
	}
	return 0;
}

