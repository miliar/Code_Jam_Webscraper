#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int c,d,n;
int f[100][100];
bool g[100][100];
void Init()
{
     scanf("%d",&c);
     memset(f,0,sizeof(f));
     memset(g,false,sizeof(g));
     char ss[10];
     for(int i=0;i!=c;++i)
     {
        scanf("%s",&ss);
        f[ss[0]][ss[1]]=f[ss[1]][ss[0]]=ss[2];
     }
     scanf("%d",&d);
     for(int i=0;i!=d;++i)
     {
        scanf("%s",&ss);
        g[ss[0]][ss[1]]=g[ss[1]][ss[0]]=true;
     }
}
void Work()
{
     char s[110];
     int n,top=0;
     scanf("%d%*c",&n);
     for(int i=0;i!=n;++i)
     {
        char ch;
        scanf("%c",&ch);
        bool tt=true;
        if(top)
           if(f[s[top-1]][ch])
           {
              s[top-1]=f[s[top-1]][ch];
              tt=false;
           }
           else
             for(int i=0;i!=top;++i)
                if(g[s[i]][ch])
                {
                   tt=false;
                   top=0;
                   break;
                }
        if(tt) s[top++]=ch;
     }
     bool fi=true;
     printf("[");
     for(int i=0;i!=top;++i)
        if(fi)
        {
           printf("%c",s[i]);
           fi=false;
        }
        else printf(", %c",s[i]);
     printf("]\n");
}
int main()
{
    int T,i;
    scanf("%d",&T);
    for(int i=0;i!=T;++i)
    {
       Init();
       printf("Case #%d: ",i+1);
       Work();
    }
    return 0;
}
