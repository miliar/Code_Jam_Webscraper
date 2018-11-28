#include <iostream>
using namespace std;
int main()
{
ios_base::sync_with_stdio(0);
int t;
cin>>t;
for(int nc=1;nc<=t;nc++)
{
int n,i,c,xx,su,mi=1000001;
cin >> n;
for(i=0,xx=0,su=0;i<n;i++)
{
cin>>c;
xx^=c;
su+=c;
if(c<mi)mi=c;
}
cout<<"Case #"<<nc<<": ";
if(xx){cout<<"NO"<<endl;continue;}
cout<<su-mi<<endl;
}
return 0;
}
