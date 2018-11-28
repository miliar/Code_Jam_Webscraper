#include<stdio.h>
int n,m,i,j,k,l,t,tt;
int a[200][200],b[200][200];

bool check()
{
     int i,j;
     for (i=1;i<=100;i++)
      for (j=1;j<=100;j++) {if (a[i][j]!=0) {return true;}}
      return false;
}

int main()
{
    freopen("C-small-attempt0(2).in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&tt);
    for (t=1;t<=tt;t++)
    {
        scanf("%d",&n);
        for (i=1;i<=100;i++) for (j=1;j<=100;j++) {a[i][j]=0;}
        for (i=1;i<=n;i++)
        {
            int x1,x2,y11,y2;
            scanf("%d%d%d%d",&x1,&y11,&x2,&y2);
            for (j=x1;j<=x2;j++) for (k=y11;k<=y2;k++) {a[j][k]=1;}
        }
        
        int time=0;
        while (check())
        {
              time++;
              for (i=1;i<=100;i++) for (j=1;j<=100;j++)
              {
                  if ((i==1)&&(j==1)) {b[i][j]=0;} else
                  if (i==1) {if (a[i][j-1]==0) {b[i][j]=0;} else {b[i][j]=a[i][j];}} else
                  if (j==1) {if (a[i-1][j]==0) {b[i][j]=0;} else {b[i][j]=a[i][j];}} else
                  {
                            if ((a[i-1][j]==0)&&(a[i][j-1]==0)) {b[i][j]=0;} else
                            if ((a[i-1][j]==1)&&(a[i][j-1]==1)) {b[i][j]=1;} else
                            {b[i][j]=a[i][j];}
                  }
              }
              
              for (i=1;i<=100;i++) for (j=1;j<=100;j++) {a[i][j]=b[i][j];}
        }
        printf("Case #%d: %d\n",t,time);
        
    }
    return 0;
}
