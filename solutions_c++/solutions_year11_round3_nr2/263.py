#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <cstdlib>

#define ll long long

using namespace std;

long long n,i,j,r,c,where,test,dd,t,l,tt,ans;
long long sum[2000005];
vector <long long> vec;
long long cur;
long long a[2000005];

int main(){
    freopen("c://input.txt","r",stdin);
    freopen("c://output.txt","w",stdout);
    cin>>tt;
    for(test=1;test<=tt;test++){
       
       cout<<"Case #"<<test<<": ";
       vec.clear();
       cin>>l>>t>>n>>c;
       for (i=0;i<c;i++)
           cin>>a[i];
       for (i=1;i<=n;i++){
           sum[i]=sum[i-1]+a[(i-1)%c];
       }
       ans=2ll*sum[n];
       if (t>=2ll*sum[n]) {cout<<2ll*sum[n]<<endl; continue;}
       for (i=1;i<=n;i++)
           if (sum[i]>=t/2ll){
              if (sum[i-1]<t/2ll){
                 where=sum[i]-t/2ll;
              } else
                where=sum[i]-sum[i-1];
              break;
              }
       for (j=i+1;j<=n;j++)
           vec.push_back(sum[j]-sum[j-1]);
       vec.push_back(where);
       sort(vec.rbegin(),vec.rend());
       long long cur = 0;
       for (i=0;i<l && i<vec.size();i++){
           cur+=vec[i];
       }
       cout<<ans-cur<<endl;
    }
    return 0;    
}
