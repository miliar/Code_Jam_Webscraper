#include<stdio.h>
FILE*f1=fopen("B-large.in","r");
FILE*f2=fopen("out.out","w");
int main()
{
    int t;
    fscanf(f1,"%d",&t);
    int a,i,n,s,p,x,rs=0;
    for(a=0;a<t;a++)
    {
      rs=0;
      fscanf(f1,"%d%d%d",&n,&s,&p);
       //if(a==99)
       //printf("%d %d %d\n",n,s,p);
      for(i=0;i<n;i++)
      {
       fscanf(f1,"%d",&x);
       //if(a==99)
       //printf("%d\n",x);
       if(x == 0)
       {
        if(p == 0)
        rs++;
        continue;
       }
       if(s != 0)
       {
        if(x % 3 == 0 && x/3+1 == p)
        {
         s--;
         rs++;
         //continue;
        }
        if(x % 3 == 2 && x/3+2 == p)
        {
         s--;
         rs++;
         //continue;
        }        
       }
       if(x % 3 == 0)
       {
           if(p <= x/3)
           rs++;
       }
       else
       {
        if(p <= x/3+1)
        rs++;
       }
       
      }
      fprintf(f2,"Case #%d: %d\n",a+1,rs);
    }
    //scanf("%*d");
}
