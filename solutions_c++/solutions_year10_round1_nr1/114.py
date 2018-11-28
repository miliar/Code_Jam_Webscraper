#include<stdio.h>
#include<string.h>
char s[100][100],st[100][100];
int n,m,i,j,k,l,t,tt;
bool bo1,bo2;
int le[4],ri[4];

void find(int x,int y)
{
     int i,j,x1,y1;
     if ((!bo1)&&(st[x][y]=='R'))
     {
         for (i=0;i<4;i++)
         {
             j=k-1;
             x1=x;y1=y;
             bo1=true;
             while ((x1+le[i]>=0)&&(y1+ri[i]>=0)&&(x1+le[i]<n)&&(y1+ri[i]<n)&&(j-1>=0)&&(st[x1+le[i]][y1+ri[i]]=='R'))
             {
                   x1+=le[i];
                   y1+=ri[i];
                   j--;
             }        
             if (j>0) {bo1=false;}
             if (bo1) {break;} 
         }
     }
     
     if ((!bo2)&&(st[x][y]=='B'))
     {
         for (i=0;i<4;i++)
         {
             j=k-1;
             x1=x;y1=y;
             bo2=true;
             while ((x1+le[i]>=0)&&(y1+ri[i]>=0)&&(x1+le[i]<n)&&(y1+ri[i]<n)&&(j-1>=0)&&(st[x1+le[i]][y1+ri[i]]=='B'))
             {
                   x1+=le[i];
                   y1+=ri[i];
                   j--;
             }        
             if (j>0) {bo2=false;}
             if (bo2) {break;} 
         }
     }
     
     
     y++;
     if (y==n) {x++;y=0;}
     if (x!=n) {find(x,y);}
}

int main()
{
    le[0]=0;ri[0]=1;
    le[1]=1;ri[1]=0;
    le[2]=1;ri[2]=-1;
    le[3]=1;ri[3]=1;
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tt);
    for (t=1;t<=tt;t++)
    {
        scanf("%d%d",&n,&k);gets(s[0]);
        for (i=0;i<n;i++) {gets(s[i]);}
        for (i=0;i<n;i++)
         for (j=0;j<n;j++) {st[j][i]=s[n-1-i][j];}
        
        for (i=n-2;i>=0;i--)
         for (j=0;j<n;j++)
          if (st[i][j]!='.')
           {
              l=i+1;
              while ((l<n)&&(st[l][j]=='.'))             
              {
                 st[l][j]=st[l-1][j];
                 st[l-1][j]='.';
                 l++;   
              }
           }
         bo1=bo2=false;  
         find(0,0);
         printf("Case #%d: ",t);  
         if ((bo1)&&(bo2)) {printf("Both\n");} else
         if ((!bo1)&&(!bo2)) {printf("Neither\n");} else  
         if ((!bo1)&&(bo2)) {printf("Blue\n");} else
         if ((bo1)&&(!bo2)) {printf("Red\n");}
    }
    return 0;
}
