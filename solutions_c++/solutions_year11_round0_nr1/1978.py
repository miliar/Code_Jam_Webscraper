#include<iostream>
#include<cstdio>
#include<algorithm>
#include<map>
#include<set>
#include<queue>
#include<cstring>
#include<cmath>
#include<string>
using namespace std;

#define f0E(i,n) for(int i=0;i<=n;++i )
#define f0L(i,n) for(int i=0; i<n; ++i )
#define f1E(i,n) for(int i=1; i<=n; ++i)
#define f1L(i,n) for(int i=1; i<n; ++i)

#define ull unsigned long long int
#define ll long long int

int m[100];char w[100];
int main()
{
	freopen("C:\\Users\\Kuldeep\\Downloads\\A-large.in","r",stdin);
	freopen("C:\\Users\\Kuldeep\\Desktop\\out.txt","w",stdout);
	int t;
	cin>>t;
	f0L(j,t)
	{
		int n;
		cin >> n;
		int bot[2] = { 1, 1 };
		int stp[2] = { 0, 0 };
		f0L(k,n) cin>>w[k]>>m[k];
		int bp = w[0]=='B'?1:0;
		stp[bp] = abs(m[0]-bot[bp])+1;
		bot[bp] = m[0];
		for( int i=1; i<n; ++i )
		{
			int bc = w[i]=='B'?1:0;
			int s = abs(m[i]-bot[bc])+1;
			bot[bc] = m[i];
			if( stp[bc]+s <= stp[bp] )
				stp[bc]=(stp[bp]+1);
			else stp[bc]+=s;
			bp = bc;
		}
		cout<<"Case #"<<(j+1)<<": "<<max(stp[0],stp[1])<<endl;
	}
	return 0;
}