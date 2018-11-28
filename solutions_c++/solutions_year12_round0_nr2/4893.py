#include<iostream>
using namespace std;

int main()
{

int t,s,p,n;

scanf("%d",&t);
for(int k=1;k<=t;k++)
{
   scanf("%d",&n);
   scanf("%d",&s);
   scanf("%d",&p);
   int ans=0,can=0;
   int arr[110];
   for(int i=0;i<n;i++)
   {

           scanf("%d",&arr[i]);
       //cout<<arr[i]<<endl;
           int m=arr[i]/3;
           int a=m,b=m,c=m;
           if(3*m!=arr[i])
           {
              b+=1;
              if((a+b+c)!=arr[i])
              c+=1;
           } 
         //  cout<<a<<" "<<b<<" "<<c<<endl;
        //      cout<<p<<endl;
           if(b>=p)
           {
              ans++;

           }
           else if(s>0&&((b+1)<=10)&&((c-1)>=0)&&(b+1)>=p&&(arr[i]%3!=1))
           {
              ans++;
              s--;
           }
   }

   printf("Case #%d: %d\n",k,ans);
   
}

return 0;
}
