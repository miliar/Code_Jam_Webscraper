#include<stdio.h>
using namespace std;
int main()
{
    freopen("F:\\C-large.in","r",stdin);
    freopen("F:\\file7.txt","w+",stdout);
    int T,A,B,i=0,j=10,k=0,t=0,pos=1,temp,sum=0,lonth=1,compare[50];
    int num[50];
    scanf("%d",&T);
    for(i=0;i<T;i++)
    {
                    sum=0;
                    scanf("%d %d",&A,&B);
                    j=10;
                    lonth=1;
                    while(A/j!=0)
                    {
                                 lonth+=1;
                                 j=j*10;
                    }
                    //printf("%d\n",lonth);
                    /*temp=B;
                    for(j=0;j<lonth;j++)
                    {
                                        b[lonth-1-j]=temp%10;
                                        temp=temp/10;
                    }*/
                    for(j=A;j<=B;j++)
                    {
                                temp=j;
                                for(k=0;k<lonth;k++)
                                {
                                                    num[lonth-1-k]=temp%10;
                                                    temp=temp/10;
                                }
                                /*for(k=0;k<lonth;k++)
                                {
                                                   printf("%d",num[k]);
                                                   }
                                                   printf("\n");*/
                                for(k=0;k<lonth-1;k++)
                                {
                                                    temp=0;
                                                    compare[k]=0;
                                                    for(pos=lonth-k-1;pos<lonth;pos++)
                                                    {
                                                                                    if(num[pos]==0&&temp==0){goto sign;}
                                                                                    compare[k]=compare[k]*10+num[pos];
                                                                                    temp++;
                                                    }
                                                    for(pos=0;pos<lonth-k-1;pos++)
                                                    {
                                                                                compare[k]=compare[k]*10+num[pos];
                                                                                temp++;
                                                    }
                                                    //printf("%d\n",compare[k]);
                                                    sign:;
                                }
                                for(k=0;k<lonth-1;k++)
                                {
                                                      for(t=0;t<lonth-1;t++)
                                                      {
                                                                            if(t!=k)
                                                                            {
                                                                                    if(compare[k]==compare[t])
                                                                                    {
                                                                                                              compare[k]=0;
                                                                                    }
                                                                            }
                                                      }
                                                      if(compare[k]>j&&compare[k]<=B)
                                                      {
                                                                               sum+=1;
                                                      }
                                }
                                //printf("!\n");                              
                    }
                    printf("Case #");
                    printf("%d",i+1);
                    printf(": ");
                    printf("%d\n",sum);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
                                                                                                    
                                                    
