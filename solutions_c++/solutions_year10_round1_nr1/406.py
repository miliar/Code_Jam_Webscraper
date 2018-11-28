#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

        int n,k;

bool isvalid(int x,int y)
{
    return (x>=0 && y>=0 && x<n && y<n);
}


int main()
{
    int t;
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++)
    {
        scanf("%d %d ",&n,&k);
        char inp[n+1][n+1];
        bzero(inp,sizeof(inp));
        for(int i=0;i<n;i++)
        {
            char in[n+1];
            gets(in);
            reverse(in,in+n);
            int s=0;
            for(int j=0;j<n;j++)
                if(in[j]!='.')
                {
                    inp[i][s]=in[j];
                    s++;
                }
//            puts(inp[i]);
        }
        int len[n][n];
        int x,y;
        int l1=0,l2=0;
#define foo(a,b,c,d) for(x=0;x<n;x++)for(y=0;y<n;y++){if(inp[x][y]==a && isvalid(b,c)) len[x][y] = len[b][c]+1; else len[x][y]=(inp[x][y]==a); d = max(d,len[x][y]);}
        foo('R',x-1,y,l1);
        foo('R',x-1,y-1,l1);
        foo('R',x-1,y+1,l1);
        foo('R',x,y-1,l1);
        foo('B',x-1,y,l2);
        foo('B',x-1,y-1,l2);
        foo('B',x-1,y+1,l2);
        foo('B',x,y-1,l2);
//printf("%d %d\n",l1,l2);

    printf("Case #%d: ",tc);
    if(l1>=k&&l2>=k)
        puts("Both");
    else if(l1>=k)
        puts("Red");
    else if(l2>=k)
        puts("Blue");
    else
        puts("Neither");
        
    }
}
