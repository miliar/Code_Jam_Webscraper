#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#include<string>
#include<algorithm>

using namespace std;

#pragma comment(linker, "/STACK:1024000000,1024000000")
#define PB push_back
#define MP make_pair

const double pi=2.0*asin(1.0),eps=1e-12;
const int maxn=1100,maxm=1100000,inf=0x3f3f3f3f;

int main()
{
	int t,ca=1,i,j;
	char ch[10][10];
	scanf("%d",&t);
	g:while(t--)
	{
		printf("Case #%d: ",ca++);
		for(i=0;i<4;i++)scanf("%s",ch[i]);
		for(i=0;i<4;i++)
		{
                for(j=0;j<4;j++)
                {
                    if(ch[i][j]=='O'||ch[i][j]=='.')break;
                }
                if(j==4)
                {
                    printf("X won\n");
                    goto g;
                }
                for(j=0;j<4;j++)
                {
                    if(ch[j][i]=='O'||ch[j][i]=='.')break;
                }
                if(j==4)
                {
                    printf("X won\n");
                    goto g;
                }


                for(j=0;j<4;j++)
                {
                    if(ch[i][j]=='X'||ch[i][j]=='.')break;
                }
                if(j==4)
                {
                    printf("O won\n");
                    goto g;
                }
                for(j=0;j<4;j++)
                {
                    if(ch[j][i]=='X'||ch[j][i]=='.')break;
                }
                if(j==4)
                {
                    printf("O won\n");
                    goto g;
                }
		}
		for(i=0;i<4;i++)
		{
            if(ch[i][i]=='O'||ch[i][i]=='.')break;
		}
		if(i==4)
        {
              printf("X won\n");
              goto g;
        }
        for(i=0;i<4;i++)
		{
            if(ch[i][3-i]=='O'||ch[i][3-i]=='.')break;
		}
		if(i==4)
        {
              printf("X won\n");
              goto g;
        }

        for(i=0;i<4;i++)
		{
            if(ch[i][i]=='X'||ch[i][i]=='.')break;
		}
		if(i==4)
        {
              printf("O won\n");
              goto g;
        }
        for(i=0;i<4;i++)
		{
            if(ch[i][3-i]=='X'||ch[i][3-i]=='.')break;
		}
		if(i==4)
        {
              printf("O won\n");
              goto g;
        }
        for(i=0;i<4;i++)
        {
        	for(j=0;j<4;j++)
        	{
        		if(ch[i][j]=='.')
        		{
        			printf("Game has not completed\n");
             		 goto g;
        		}
        	}
        }
        printf("Draw\n");
	}
	return 0;
}

