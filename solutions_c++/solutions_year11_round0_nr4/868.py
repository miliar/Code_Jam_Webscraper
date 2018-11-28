#include <iostream>
int ar[1500];
using namespace std;
int main()
{
ios_base::sync_with_stdio(0);
int t;
cin>>t;
for(int nc=1;nc<=t;nc++)
{
int n,i,z;
cin >> n;
for(i=1,z=0;i<=n;i++)
{cin>>ar[i];if(ar[i]!=i)z++;}
cout<<"Case #"<<nc<<": "<<((double)(z==1?0:z))<<endl;
}
return 0;
}
