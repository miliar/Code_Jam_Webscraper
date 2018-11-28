#include<iostream>
using namespace std;
//int hash[2000010];
int main()
{
    int t,l=1;
    cin>>t;
    while(t--)
    {
        int a,b,ans=0,arr[10],arr1[10],arr2[10],rot[10];
        //for(int i=0;i<2000010;i++) hash[i]=0;
        cin>>a>>b;
        for(int n=a;n<b;n++)
        {
           int temp=n,j=0,p=0;
           while(temp>0)
           {
             arr[j++]=temp%10;
             temp/=10;                        
           }     
           for(int i=0;i<j;i++)
              arr1[i]=arr[j-i-1];
           for(int k=0;k<j;k++)
           {
              int m=0;     
              for(int i=0;i<=k;i++)
                 arr2[i]=arr1[j-k-1+i];
              for(int i=k+1;i<j;i++)
                 arr2[i]=arr1[i-k-1];              
              if(arr2[0]!=0)
              {
                for(int i=0;i<j;i++)
                  m=m*10+arr2[i];
                if(m>n && m<=b) 
                { 
                   int flag=1;    
                   for(int i=0;i<p && flag;i++) if(rot[i]==m) flag=0;
                   if(flag)    
                   {
                    ans++; 
                    rot[p++]=m;
                   }
                //cout<<n<<" "<<m<<" "<<ans<<"\n";                
                }
              }              
           }
        }      
       // for(int i=a;i<=b;i++) if(hash[i]) cout<<i<<"\n";
       printf("Case #%d: %d\n",l++,ans);
    }
}
