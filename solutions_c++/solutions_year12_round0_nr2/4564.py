#include<stdio.h>
int main()
{
    freopen("A1.txt","r",stdin);
    freopen("A2.txt","w",stdout);
    int t=0,s=0,n=0,i=0,p=0,arr[105]={0},j,num,s1,ans,a,b,rem;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
                    s=0,n=0,p=0,s1=0,a=0,b=0,ans=0;
                    scanf("%d %d %d",&n ,&s ,&p );
                    for(j=0;j<n;j++)
                    {
                                    scanf("%d",&arr[j]);
                                    }
                    //s1=max. no. of surprising cases under all circumstances
                    //a=no. of surprising cases in which we can get p without use of surprise element
                    //b=no. of surprising cases in which we get p with surprise element only 
                    for(j=0;j<n;j++)
                    {
                                            num=arr[j]/3;
                                            rem=arr[j]%3;
                                            if(rem==0)
                                            {
                                                      s1++;
                                                      if(num>=p)
                                                      a++;
                                                      else if((arr[j]!=0)&&(num+1)>=p)
                                                      b++;
                                                      }
                                            else if(rem==1)
                                            {
                                            
                                                      if((num+1)>=p)
                                                      a++;
                                                      }
                                            else if(rem==2)
                                            {
                                            
                                                      if((num+1)>=p)
                                                      a++;
                                                      else if((num+2)>=p)
                                                      b++;
                                                      }
                                    }
                    if((s>=b))
                    ans=a+b;
                    else
                    ans=a+s;
                    printf("Case #%d: %d\n",i+1,ans);
    }
    return 0;
}
