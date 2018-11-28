#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define scan(a) fscanf(in,"%d",&a)
#define scanc(a) fscanf(in," %c",&a)
#define min(a,b) (a)<(b)?(a):(b)
#define max(a,b) (a)>(b)?(a):(b)

const int INF=2000000;

FILE *in = fopen( "A-large.in" , "r" );
FILE *out = fopen( "out.txt" , "w" );

int a[2000],v[2000];
char ch[2000];

int main()
{
    int T,i,j,k,n,d,curx,cury,nexx,nexy,sum;
   // fscanf(in,"%d",&T);
    scan(T);
    
    for(k=1;k<=T;k++)
    {
          scan(n);
          for(i=0;i<n;i++)
          {
                scanc(ch[i]);
                scan(v[i]);
              //  fprintf(out,"%c %d\n",ch[i],v[i]);
          }
          
          for(i=0,sum=0,curx=1,cury=1;i<n;i++)
          {
                nexx=curx,nexy=cury;
                if(ch[i]=='B')
                {
                    // nexy=cury;
                     for(j=i+1;j<n;j++)
                        if(ch[j]=='O')
                        {
                              nexy=v[j];
                              break;
                        }
                     d=abs(v[i]-curx)+1;
                     sum+=d;
                     curx=v[i];
                     if(nexy>cury)
                           cury=min(nexy,cury+d);
                     else
                           cury=max(nexy,cury-d);
                }
                else
                {
                  //   nexx=curx;
                     for(j=i+1;j<n;j++)
                        if(ch[j]=='B')
                        {
                              nexx=v[j];
                              break;
                        }
                     d=abs(v[i]-cury)+1;
                     sum+=d;
                     cury=v[i];
                     if(nexx>curx)
                           curx=min(nexx,curx+d);
                     else
                           curx=max(nexx,curx-d);
                }
               // fprintf(out,"%d %d %d %d %d\n",sum,curx,cury,nexx,nexy);
          }
      
          
         fprintf(out,"Case #%d: %d\n",k,sum);
               
    
          
    }
    return 0;
}
