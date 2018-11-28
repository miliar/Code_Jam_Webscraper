#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <string.h>
#include <cstdio>
#pragma comment(linker, "/STACK:167772160")
using namespace std;

typedef long long    Int;
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define mp make_pair
#define pb push_back
#define sz(x) int((x).size())
const int inf=1000000000;

set<int>q;
int pw[]={1,10,100,1000,10000,100000,1000000,10000000};

int ok(int n,int l,int r)
{
	q.clear();

	int len=0;
	int nn=n;
	while(nn){len++;nn/=10;}
	nn=n;

	
	FOR(o,1,len-1)
	{
		int t=n%10;
		n=n/10+t*pw[len-1];

		if(t && n>=l && n<=r && n>nn)q.insert(n);
	}
	return sz(q);
}

int main()
{     
	 freopen("input.txt","r",stdin);
	 freopen("output.txt","w",stdout);
	 int tes;cin>>tes;
	 FOR(o,1,tes)
	 {
		 Int ans=0;
		 int l,r;
		 cin>>l>>r;
		 FOR(i,l,r)
			 ans+=ok(i,l,r);
		 
		 cout<<"Case #"<<o<<": "<<ans<<endl;
	 }
}