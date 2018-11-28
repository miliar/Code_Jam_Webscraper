#include<stdio.h>

#define scan(a) fscanf(in,"%d",&a)

const int INF=2000000;

FILE *in = fopen( "C-large.in" , "r" );
FILE *out = fopen( "out.txt" , "w" );

int a[2000];

int main()
{
    int T,sum,v,k,n,i,m,minv;
   // fscanf(in,"%d",&T);
    scan(T);
    
    for(k=1;k<=T;k++)
    {
    
          scan(n);
          for(i=0,v=0,minv=INF,sum=0;i<n;i++)
          {
              scan(a[i]);
            //  scanf("%d",&a[i]);
              v+=a[i];
              sum^=a[i];
              if(a[i]<minv)
                 minv=a[i];
          }
          
       //   fprintf(out.txt,"Case #%d: ",&k);
          
          if(sum!=0)
               fprintf(out,"Case #%d: NO\n",k);
          else
               fprintf(out,"Case #%d: %d\n",k,v-minv);
               
       
    
          
    }
    return 0;
}
