#include<stdio.h>
#include<algorithm>
#include<string>
using namespace std;

int in[103][103];
int ans[103][103];
int tag[10009];
int h,w;
int mov[][2]={-1,0,0,-1,0,1,1,0};
bool Valid(int r,int c)
{
     return r<h&&r>=0&&c>=0&&c<w;
}
int Get(int r,int c)
{
    if(ans[r][c]!=-1)
		return ans[r][c];
	ans[r][c]=r*w+c;
	int now=in[r][c];
	int i;
	int rr,cc;
	for(i=0;i<4;i++)
	{
	    rr=r+mov[i][0];
		cc=c+mov[i][1];
        if(!Valid(rr,cc))
			continue;
        if(in[rr][cc]<now)
		{
		   ans[r][c]=Get(rr,cc);
		   now=in[rr][cc];
		}
	}
	return ans[r][c];
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
	int i,j,k;
	scanf("%d",&t);
    for(k=0;k<t;k++)
	{
	    scanf("%d%d",&h,&w);
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
			{
				tag[i*w+j]=-1;
				ans[i][j]=-1;
				scanf("%d",&in[i][j]);
			}
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
				Get(i,j);
		printf("Case #%d:\n",k+1);
		int ji=0;
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
			{
			    if(tag[ans[i][j]]==-1)
				{
					tag[ans[i][j]]=ji++;
				}
				printf("%c",tag[ans[i][j]]+'a');
				if(j==w-1)
					puts("");
				else
					printf(" ");
			}
	}
    return 0;
}