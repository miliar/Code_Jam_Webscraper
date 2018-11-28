#include<string>
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<vector>
#include<map>
using namespace std;

#define sf scanf
#define pf printf
#define dbg put("OK\n");
#define fo(i,n) for(i=0;i<n;i++)
#define rfo(i,n) for(i=n;i>0;i--)

//#define small
#define large
int main()
{
	#ifdef small
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-out.out","w",stdout);
	#endif
	#ifdef large
	freopen("A-large.in","r",stdin);
	freopen("A-large-out.out","w",stdout);
	#endif
	int i, j,id,t;
	scanf("%d",&t);
	for(id=1;id<=t;id++)
	{
	    int n,m,blue=0,white=0;
	    scanf("%d %d",&n,&m);
	    char grid[51][51];
	    memset(grid,'.',sizeof(grid));
	    for(i=1;i<=n;i++)
	    {
	        for(j=1;j<=m;j++)
	        {
	            cin>>grid[i][j];
	            if(grid[i][j]=='#') blue++;
	            if(grid[i][j]=='.') white++;
	        }
	    }
	    //cerr<<(blue/4)%10<<endl;
	    //if( (blue/4) % 10 !=0 && white==0) {printf("Case #%d:\nImpossible\n",id);continue;}
	    //else {
            for(i=1;i<=n;i++)
            {
                for(j=1;j<=m;j++)
                {
                    //cout<<grid[i][j]<<grid[i][j+1]<<grid[i+1][j]<<grid[i+1][j+1]<<endl;
                    if(grid[i][j]=='#' && grid[i][j+1]=='#' && grid[i+1][j]=='#' && grid[i+1][j+1]=='#')
                    {
                        grid[i][j]='/'; grid[i][j+1]='\\';grid[i+1][j]='\\'; grid[i+1][j+1]='/'; blue-=4; //
                        //printf("Remaining %d\n",blue);
                    }
                }
            }
        //}
        if(blue==0)
        {
            printf("Case #%d:\n",id);
            for(i=1;i<=n;i++)
            {
                for(j=1;j<=m;j++)
                {
                    printf("%c",grid[i][j]);
                }
                printf("\n");
            }
            printf("\n");continue;
        }
        printf("Case #%d:\nImpossible\n",id);
	}

    return 0;
}
