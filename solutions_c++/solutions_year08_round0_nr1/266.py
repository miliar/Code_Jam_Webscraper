#include<cstdio>
#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<algorithm>
#include<numeric>
#include<cstdlib>
#include<cmath>
#include<set>
#include<map>
#include<ctime>
#include<utility>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz size()
#define all(qq) qq.begin(),qq.end()
#define rall(qq) qq.rbegin(),qq.rend()
#define clr(qq) memset((qq),0,sizeof(qq))
#define fill(qq) memset((qq),0x3F,sizeof(qq))
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define repd(i,n) for(int i=(int)(n-1);i>=0;i--)
#define rep2(i,a,b) for(int (i)=(int)(a);i<(int)(b);i++)
#define fore(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define rint(qq) int(floor(qq+0.5))
#define sqr(qq) ((qq) * (qq))
#define ll long long
#define inf 999999999
#define fi first
#define se second

int n,s,q,ret;
map<string,int> ind;
map<int,string> meno;
int mem[1005][105];
int hlada[1005];

int go(int kde,int aky)
{
	if (kde==q) return 0;
	if (mem[kde][aky]!=-1) return mem[kde][aky];
	int ans=-2;
	rep(i,s)
	{
		if (hlada[kde]!=i)
		{
			int pom=go(kde+1,i);
			if (ans==-2||pom<ans)
			{
				if (i!=aky) pom++;
				ans=pom;
			}
		}
	}
	return mem[kde][aky]=ans;
}

int main ()
{
	cin>>n;
	rep(k,n)
	{
		meno.clear();
		ind.clear();
		memset(mem,-1,sizeof(mem));
		cin>>s;
		getchar();
		rep(i,s)
		{
			string s;
			getline(cin,s);
			meno[i]=s;
			ind[s]=i;
		}
		cin>>q;
		getchar();
		rep(i,q)
		{
			string s;
			getline(cin,s);
			hlada[i]=ind[s];
		}
		ret=go(0,0);
		rep(i,s)
		{
			ret=min(ret,go(0,i));
		}
		cout<<"Case #"<<k+1<<": "<<ret<<endl;
	}
	return 0;
}
