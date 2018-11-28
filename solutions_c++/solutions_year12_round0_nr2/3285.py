#include<stdio.h>

int main()
{
    freopen("B-large.in","rt",stdin);
	freopen("D2.out","wt",stdout);
    int T,t;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
    int N,S,p,T[100],i,R[100][2][3],count=0;
    scanf("%d",&N);
    scanf("%d",&S);
    scanf("%d",&p);
    for(i=0;i<=N-1;i++)
    {
    scanf("%d",&T[i]);
    int n,a[3],b[3];
    n=T[i];
    //scanf("%d",&n);
    a[0] = n/3;
    a[1] = (n-a[0])/2;
    a[2] = n-a[0]-a[1];
    if(n%3==0 && n!=0)
    {
              b[0] = n/3;
              b[1] = b[0]-1;
              b[2] = b[0]+1;
              }         
    if(n%3==1 && n!=1)
    {
              b[0] = n/3-1;
              b[1] = b[0]+2;
              b[2] = b[0]+2;
              }
    if(n%3==2)
    {
              b[0] = n/3;
              b[1] = b[0];
              b[2] = n-b[0]-b[1];
              }
    if(n==0)
    {
            b[0] =0;
            b[1] = 0;
            b[2] = 0;
            }
    if(n==1)
    {
            b[0] =0;
            b[1] = 0;
            b[2] = 1;
            }
                              
    for(int j=0;j<=2;j++)
    {
    R[i][0][j]= a[j];
    R[i][1][j]= b[j];
}
}
for(int j=0;j<=N-1;j++)
{ 
                if((R[j][0][0]<p&&R[j][0][1]<p&&R[j][0][2]<p&&S!=0)&&(R[j][1][0]>=p||R[j][1][1]>=p||R[j][1][2]>=p))
                {
                    count++;
                    S--; 
                    }

                if(R[j][0][0]>=p||R[j][0][1]>=p||R[j][0][2]>=p)
                {
                    count++;
                    }                                                                                              
                        }
                                                                        {
}
printf("Case #%d: %d\n",t,count);
}
}
    
