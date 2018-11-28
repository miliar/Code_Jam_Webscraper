#include<stdio.h>
#include<string.h>
FILE *fpin=fopen("A-large.in","r");
FILE *fpout=fopen("a.out","w");
int a[205];
char c[205];
int n,sum,tt;
int abs(int a)
{
   if(a>0) return a;
   else return -a;
}
void dfs(int k,int t,int cnt,int l)
{
     if(cnt>n){fprintf(fpout,"Case #%d: %d\n",tt,sum);return;}
     int i,j,tl=0;
     if(a[cnt]>k+l||a[cnt]<k-l)
     {
        sum+=abs(a[cnt]-k)-l;
        tl+=abs(a[cnt]-k)-l;
     }
     tl+=1;
     sum+=1;j=a[cnt];
     for(i=cnt+1;i<=n;i++)
      if(c[i]!=c[cnt]) break;
      else
      {
         sum+=abs(a[i]-a[i-1])+1;
         tl+=abs(a[i]-a[i-1])+1;
         j=a[i];
      }
     dfs(t,j,i,tl);
}
int main()
{
    int p,i;
    fscanf(fpin,"%d",&p);tt=0;
    while(p--)
    {
        sum=0;tt++;
        fscanf(fpin,"%d",&n);
        for(i=1;i<=n;i++)
        {
           fscanf(fpin,"%c",&c[i]);
           while(c[i]==' ') 
           fscanf(fpin,"%c",&c[i]);
           fscanf(fpin,"%d",&a[i]);
        }
        dfs(1,1,1,0);
    }
    fclose(fpout);
    fclose(fpin);
}
