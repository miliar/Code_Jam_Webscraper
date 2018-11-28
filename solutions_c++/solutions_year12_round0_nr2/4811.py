#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    int t;
    int n=0;
    cin>>t;
    while(t--)
    {
        n++;
        int num,s,p,arr[110];
        cin>>num>>s>>p;
        for(int i=0;i<num;i++)
           cin>>arr[i];
        int count=0;
        sort(arr,arr+num);
        for(int j=0;j<num;j++)
        {
           int no=arr[j]/3;
           if(arr[j]%3!=0) no++;
           if(no>=p)
           {
              count++;
              arr[j]=-1;      
           }
           if(arr[j]==29 || arr[j]%3==1 || arr[j]==30)
              arr[j]=-1;
        }
        sort(arr,arr+num);
        int i=num-1;
        
        while(s>0 && i>=0)
        {
           if(arr[i]>0)
           {
              int no=arr[i]/3;
              if(arr[i]%3!=0) no++;
              if(no+1>=p)
              {
                 count++;
                 s--;
                 arr[i]=-1;
              }
           }
           i--;
        }
        printf("Case #%d: %d\n",n,count);
    }
}
