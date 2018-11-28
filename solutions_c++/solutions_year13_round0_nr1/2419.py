#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>

using namespace std;
int d[4][2]={0,1,1,0,1,1,1,-1};
 char a[10][10];

bool check(int i,int j,int k)
{
    int p,x=i,y=j;
    for (p=1; p<=4; p++)
    {
        if (x<1 || y<1 || x>4 || y>4) return false;
        if (a[x][y]=='T' || a[x][y]==a[i][j]) {}
        else return false;
        x+=d[k][0]; y+=d[k][1];
    }
    return true;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("a.out","w",stdout);
    int o,n=4,i,j,k,cas=0;
    scanf("%d",&o);
    while (o--)
    {
        int cnt=0;
        for (i=1; i<=n; i++)
         for (j=1; j<=n; j++)
          {
              cin>>a[i][j];
              if (a[i][j]=='.') cnt++;
          }
        int t=0; char res;
        for (i=1; i<=n; i++)
         for (j=1; j<=n; j++)
          if (a[i][j]!='.')
          for (k=0; k<4; k++)
           if (check(i,j,k))
            {t=1; res=a[i][j];}
        printf("Case #%d: ",++cas);
        if (t) printf("%c won\n",res);
        else
        {
            if (cnt==0) printf("Draw\n");
            else printf("Game has not completed\n");
        }

    }
}
