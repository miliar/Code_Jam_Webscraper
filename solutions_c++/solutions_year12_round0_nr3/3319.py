#include<stdio.h>

int main()
{
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C.out","wt",stdout);
    int N,a,b,c,i;
    int arn[200000][2];        
    int ari =0 ;      
    scanf("%d",&N);
    for(a=1;a<=N;a++)
    {
                     scanf("%d%d",&b,&c);
                     ari=0;
                     //printf("%d %d\n",b,c);
                 for(i=b;i<=c;i++)
                 {
                       //           printf("%d",i);                    
                                    
                                  
int d,dig;
//scanf("%d",&d);
d = i;
dig = d;
int nd = 0;
while(d!=0)
{
        d=d/10;
        nd++;
        }
       // printf("No of digit : %d",nd);
int ar[7];
int div=1;

//printf("\n");
int mul =1;

for(int k=0;k<=nd-1;k++)
{
        mul = mul *10;
       }
for(int j=0;j<=nd-2;j++)
{
        div =1;
for(int k=0;k<=j;k++)
{
        div = div *10;
       }


        //printf("\n div[%d]:%d\n",j,div);
 
        ar[j] = (dig%div)*(mul/div)+dig/div;
  //      printf ("ar[%d]:%d   ",j,ar[j]);  
        }
    //    printf("\n");
for(int l=0;l<=nd-2;l++)
{
        if(dig!=ar[l] && ar[l]>=b && ar[l]<=c)
        {
                      int ch = 0;
                      for(int n=0;n<=ari-1;n++)
                      {
                              if(dig==arn[n][0]&&ar[l]==arn[n][1])
                              ch=1;
                              else if(dig==arn[n][1]&&ar[l]==arn[n][0])
                              ch=1;
                              }

                              if(ch==0)
                          { 
                          arn[ari][0] = dig;
                          arn[ari][1] = ar[l];
                          ari++;
                          }
                      }
}
}
/*for(int m=0;m<=ari-1;m++)
{
        printf("[%d,%d]\n",arn[m][0],arn[m][1]);
        }                      
  */      

printf("Case #%d: %d\n",a,ari);
}
scanf("%d",&N);
                     }
