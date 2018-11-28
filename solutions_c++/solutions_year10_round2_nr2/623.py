#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string.h>
#include <stdlib.h>
using namespace std;

int n,k,t;
long long b;
long long x[51];
int v[51];

int main()
{
int tc;
cin >>tc;

for(int c=1;c<=tc;++c)
{
 cin>>n>>k>>b>>t;
 for(int i=0;i<n;++i)
	cin>>x[i];
 for(int i=0;i<n;++i)
	cin>>v[i];
 
 int cnt=0;
 int r[51]={0},swaps[51]={0};
 for(int i=n-1;i>=0;--i)
 {
//  if (cnt==k) break; 
  if (x[i]+v[i]*t>=b)
	  r[i]=1;
 }
int ans=0;

 for (int i=n-1;i>=0;--i) {
	int end=n-1;
	if(r[i]==0) continue;
	cnt++;int swps=0;
	for(int j=i+1;j<=end;++j)
	{
		if (r[j]==1) {swps+=swaps[j];break;}
		if(x[j]-x[i]<=(v[i]-v[j])*t)
			++swps;
	}
	swaps[i]=swps;
	ans+=swps;
	if (cnt==k) break;
 }
if (cnt==k)
	cout<<"Case #"<<c<<": "<<ans<<endl;
else
	cout<<"Case #"<<c<<": IMPOSSIBLE"<<endl;
}

}
