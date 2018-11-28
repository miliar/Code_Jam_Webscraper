#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
    int t,t1,n,i,j,min1;
    t1 = 1;
    cin>>t;
    while(t1<=t){
               cin>>n;
               int a[n];
               long long sum = 0;
               long long ans = 0;
               for(i=0;i<n;i++){
                               cin>>a[i];
                  //             cout<<a[i]<<endl;
                               sum = sum+a[i];
                               ans = ans^a[i];
               }
               if(ans){
                       cout<<"Case #"<<t1<<": NO"<<endl;
               }
               else
               {
                   min1 = *min_element(a,a+n);
                   sum = sum-min1;
                   cout<<"Case #"<<t1<<": "<<sum<<endl;
               }
               t1++;
    }
}
                   

                  
               
