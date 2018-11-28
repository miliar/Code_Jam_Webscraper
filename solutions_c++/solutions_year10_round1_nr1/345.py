#include <cstdio>

int dx[5]={0,1,0,1,1};
int dy[5]={0,0,1,1,-1};
int a[60][60];
int n,m;

bool check(int x, int y, int p)
{
     int t=a[x][y];
     bool re=1;
     for (int i=1;i<=m;i++)
     {
         if (x<1||x>n||y<1||y>n||a[x][y]!=t)
         {
             re=0;
             break;
         }
         x+=dx[p]; y+=dy[p];
     }
     return re;
}

int main()
{
    freopen("a1.in","r",stdin);
    freopen("a1.out","w",stdout);
    int T;
    scanf("%d",&T);    
    for (int run=1;run<=T;run++)
    {
        scanf("%d%d",&n,&m);
        for (int i=n;i>0;i--)
        {
            char ch;
            ch=getchar();
            for (int j=n;j>0;j--)
            {
                ch=getchar();
                if (ch=='.') a[j][i]=0;
                if (ch=='R') a[j][i]=1;
                if (ch=='B') a[j][i]=2;
            }
        }
        
        for (int j=1;j<=n;j++)
        {
            int last=0;
            for (int i=1;i<=n;i++)
                if (a[i][j])
                {
                   int t=a[i][j];
                   a[i][j]=0;
                   a[last+1][j]=t;
                   last++;
                }
        }
  /*      for (int i=n;i>0;i--)
        {
            for (int j=1;j<=n;j++)
                printf("%d",a[i][j]);
            printf("\n");
        }*/
        bool AR=0,AB=0;
        for (int i=1;i<=n;i++)
            for (int j=1;j<=n;j++)
                if (a[i][j])
                   for (int k=1;k<=4;k++)
                       if (check(i,j,k))
                       {
                           if (a[i][j]==1) AR=1;
                           else AB=1;
                           break;
                       }
        printf("Case #%d: ",run);
        if (AR&&AB) printf("Both\n");
        else
            if (AR) printf("Red\n");
            else
                if (AB) printf("Blue\n");
                else printf("Neither\n");
    }
    return 0;
}
        
                
