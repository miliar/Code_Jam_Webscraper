#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <iomanip>
#define LL long long
using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
int t,n,j,i,arr[1005],min,sum=0;
memset(arr,0,sizeof(arr));
cin>>t;
for(j=0;j<t;j++)
{
cin>>n;sum=0;
int flag;cin>>arr[0];flag=min=sum=arr[0];
    for(i=1;i<n;i++)
    {cin>>arr[i];flag^=arr[i];
    if(arr[i]<min)
    min=arr[i];
    sum+=arr[i];
    }
if(flag)
cout<<"Case #"<<j+1<<": "<<"NO"<<endl;
else
cout<<"Case #"<<j+1<<": "<<sum-min<<endl;

}
}
