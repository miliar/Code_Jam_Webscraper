#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    int a[1100],n,t,i,j,l;
    scanf("%d",&t);
    l=1;
    while(l<=t)
    {
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
                   scanf("%d",&a[i]);
}
int sum=0,sum1=0,ans,min=a[0];
  for (i = 0; i < n; i++)
  {
      if (a[i] < min)
		{
		  min = a[i];
       }
         }
         //printf("%d",min);
for(i=0;i<n;i++)
{
                sum=sum^a[i];
                sum1=sum1+a[i];
                }
       if(sum==0)
       {
                          // printf("%d",min);
                          ans=sum1-min;
                          printf("Case #");
                          printf("%d",l);
                          printf(": ");
                          printf("%d",ans);
                          cout<<endl;
                           }
                           if(sum!=0)
                           {
                                      printf("Case #");
                          printf("%d",l);
                          printf(": ");
                          printf("NO");
                          cout<<endl;
                          }
                           l++;
                          }
return 0;
}
