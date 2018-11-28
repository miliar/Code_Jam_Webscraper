#include<stdio.h>
#include<fstream.h>
using namespace std;
typedef long long int lld;
int main()
{lld n,t,c=1,sum,num[10000],k,i,j,temp;

    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
scanf("%lld",&t);
while(t--)
{
scanf("%lld",&n);
for(i=0;i<n;i++)
{
scanf("%lld",&num[i]);
}

for(i=n-2;i>=0;i--)  
         {  
            for(j=0;j<=i;j++)  
  
                  {  
                    if(num[j]<num[j+1])  
                                    {  
                                      temp=num[j];  
                                     num[j]=num[j+1];  
                                     num[j+1]=temp;  
                                    }  
                   }  
  }
  
//for(i=0;i<n;i++)
{
//printf("%d ",num[i]);
}
k=num[0];
sum=num[0];
for(i=1;i<n-1;i++)
{ k=k^num[i];
sum+=num[i];
//printf("%d",k);

}
if(k==num[n-1])
{
printf("Case #%lld: %lld\n",c,sum);
        c++;
}//printf("%lld\n",sum);
else{
printf("Case #%lld: NO\n",c);
        c++;
}//printf("NO\n");
}
//getchar();getchar();
        return 0;
}      
