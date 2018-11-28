#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;
#define M 0x7ffffff
int map[5][5];
int flag[2];
void dfs(int x,int y,int n)
{
    int k;
    int i,j;
    k=0;i=x;j=y;
    while(i>=1&&i<=4&&j>=1&&j<=4)
    {
        if(map[i][j]==n||map[i][j]==2)
        {
            k++;
            i--;
        }
        else break;

    }
    if(k==4)
    {
        flag[n]=1;return ;
    }

    k=0;i=x;j=y;
    while(i>=1&&i<=4&&j>=1&&j<=4)
    {
        if(map[i][j]==n||map[i][j]==2)
        {
            k++;
            i++;
        }
        else break;

    }
    if(k==4)
    {
        flag[n]=1;return ;
    }

    k=0;i=x;j=y;
    while(i>=1&&i<=4&&j>=1&&j<=4)
    {
        if(map[i][j]==n||map[i][j]==2)
        {
            k++;
            j--;
        }
        else break;

    }
    if(k==4)
    {
        flag[n]=1;return ;
    }

    k=0;i=x;j=y;
    while(i>=1&&i<=4&&j>=1&&j<=4)
    {
        if(map[i][j]==n||map[i][j]==2)
        {
            k++;
            j++;
        }
        else break;

    }
    if(k==4)
    {
        flag[n]=1;return ;
    }
	//printf("k=%d\n",k);
    k=0;i=x;j=y;
    while(i>=1&&i<=4&&j>=1&&j<=4)
    {
        if(map[i][j]==n||map[i][j]==2)
        {
            k++;
            i--;
            j--;
        }
        else break;

    }
    if(k==4)
    {
        flag[n]=1;return ;
    }

    k=0;i=x;j=y;
    while(i>=1&&i<=4&&j>=1&&j<=4)
    {
        if(map[i][j]==n||map[i][j]==2)
        {
            k++;
            i--;
            j++;
        }
        else break;

    }
    if(k==4)
    {
        flag[n]=1;return ;
    }

    k=0;i=x;j=y;
    while(i>=1&&i<=4&&j>=1&&j<=4)
    {
        if(map[i][j]==n||map[i][j]==2)
        {
            k++;
            i++;
            j++;
        }
        else break;

    }
    if(k==4)
    {
        flag[n]=1;return ;
    }

    k=0;i=x;j=y;
    while(i>=1&&i<=4&&j>=1&&j<=4)
    {
        if(map[i][j]==n||map[i][j]==2)
        {
            k++;
            i++;
            j--;
        }
        else break;

    }
    if(k==4)
    {
        flag[n]=1;return ;
    }


}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
    int t,cnt=0,k;
    char ch;
    scanf("%d",&t);
    for(cnt=1;cnt<=t;cnt++)
    {
        memset(map,-1,sizeof(map));
        k=0;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            {
                cin>>ch;
                if(ch=='T')
                    map[i][j]=2;
                else if(ch=='X')
                    map[i][j]=0;

                else if(ch=='O')
                    map[i][j]=1;
                else if(ch=='.')
                    k=1;   //not completed

            }
        flag[0]=0;flag[1]=0;
        for(int i=1;i<=4;i++)
        {
			for(int j=1;j<=4;j++)
            {
                if(map[i][j]==0)
                {
				   dfs(i,j,0);
				   if(flag[0]==1)
					   	break;
				}
			}
			if(flag[0]==1)
				break;
		}
        for(int i=1;i<=4;i++)
        {
			for(int j=1;j<=4;j++)
            {
                if(map[i][j]==1)
                {
				   dfs(i,j,1);
				   if(flag[1]==1)
					   	break;
				}
			}
			if(flag[1]==1)
				break;
		}
        printf("Case #%d: ",cnt);
        if(flag[0]==1)
            printf("X won\n");
        else if(flag[1]==1)
            printf("O won\n");
        else if(k==1)
            printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
