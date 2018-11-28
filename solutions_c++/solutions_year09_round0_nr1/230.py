#include<iostream>
using namespace std;
const int maxl=20;
const int maxd=5010;
int c[maxd][maxl],w[maxl][30],l,n,d,ans,tt;
void init()
{
     scanf("%d%d%d\n",&l,&d,&n);
     int i,j;
     for (i=0;i<d;i++)
     {
         for (j=0;j<l;j++)
         c[i][j]=(getchar()-'a');
         getchar();
     }
}

int check(int x)
{
    int i;
    for (i=0;i<l;i++)
    if (w[i][c[x][i]]!=tt) return 0;
    return 1;
}

void work()
{
     int i;
     char ch;
     for (tt=1;tt<=n;tt++)
     {
         ans=0;
         for (i=0;i<l;i++)
         {
             ch=getchar();
             if (ch=='(')
             {
                while (1)
                {
                      ch=getchar();
                      if (ch==')') break;
                      w[i][ch-'a']=tt;
                }
             }
             else w[i][ch-'a']=tt;
         }
         getchar();
         for (i=0;i<d;i++)
         if (check(i)) ans++;
         printf("Case #%d: %d\n",tt,ans);
     }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    init();
    work();
    return 0;
}
