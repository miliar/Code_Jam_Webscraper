#include<iostream>
#include<vector>
#include<math.h>
#include<string>
#include<set>
#include<deque>
#include<stack>
#include<algorithm>
#include<queue>
#include<map>
#include<cstdio>
using namespace std;
int main()
{long long t,n,c=0;
long long a[1009];
cin>>t;
while(t--)
{c++;
          cin>>n;
          for(int i=0;i<n;i++)
          cin>>a[i];          
          
long long ans=0;
for(int i=0;i<n;i++)
{
        ans=ans^a[i];
        }
        if(ans!=0) cout<<"Case #"<<c<<": NO"<<endl;
        else
        {long long sum=0;
            sort(a,a+n);
            for(int i=1;i<n;i++) sum+=a[i];
            cout<<"Case #"<<c<<": "<<sum<<endl;
            }
}

return 0;
}
