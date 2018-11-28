#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
bool myfunction (int i,int j) { return (i>j); }
int main()
{int i,m,p,k,l,ans,n,t,f;
vector<int> freq;
cin>>n;
for(t=1;t<=n;t++)
{cin>>p>>k>>l;freq.clear();
for( i=0;i<l;i++)
{cin>>f;freq.push_back(f);
}

if(p*k<l)
{cout<<"Case #"<<t<<": Impossible"<<endl;continue;}
sort(freq.begin(),freq.end(),myfunction);ans=0;

for(i=0;i<l;i++)
{m=i/k;m=m+1;
ans+=m*freq[i];
}
cout<<"Case #"<<t<<": "<<ans<<endl;
}
return 0;
}
