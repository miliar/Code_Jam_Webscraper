/*
TASK:
LANG: C++
 */
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif
template<class key>
struct hashtemp
{

	enum
	{
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};

using namespace std;

#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO=0;
const long double INF=1/ZERO,EPSILON=1e-12;
#define all(c) (c).begin(),(c).end()
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
#define let(x,y) __typeof(y) x(y)

#define rrep(i,n) for(int  i=((int)n)-1;i>=0;--i)
#define rall(c) (c).rbegin(),(c).rend()
#define rrep2(i,a,b) for(int i=(a);i>=((int)b);--i)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define rep2d(i, j, v) rep(i, sz(v)) rep(j, sz(v[i]))
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)

int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

bool getDir(int i,int j,int k,int &ni,int &nj,int r,int c)
{
	ni=i+dir[k][0];
	nj=j+dir[k][1];
	return ni>=0 && ni<r && nj<c && nj>=0;
}

int arr[100][100];
int ret[100][100];
char res[100][100];

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
	int T;
	cin>>T;
	rep2(t,1,T)
	{
		int r,c;
		cin>>r>>c;
		rep(i,r)
			rep(j,c)
			{
				cin>>arr[i][j];
			}
		rep(I,r)
			rep(J,c)
			{
				int i=I,j=J;
				bool done=1;
				while(done)
				{
					done=0;
					int ni=-1,nj,ii,jj,m=arr[i][j];
					rep(k,4)
					{
						if(getDir(i,j,k,ii,jj,r,c) && arr[ii][jj]<m)
							done=1,m=arr[ii][jj],ni=ii,nj=jj;
					}
					if(ni!=-1)
					{
						i=ni;
						j=nj;
					}
				}
				ret[I][J]=i*100+j;
			}
		char next='a';
		map<int,char> mp;
		rep(i,r)
			rep(j,c)
				if(mp.count(ret[i][j]))
					res[i][j]=mp[ret[i][j]];
				else
					res[i][j]=mp[ret[i][j]]=next++;
		cout<<"Case #"<<t<<":\n";
		rep(i,r)
		{
			char *s="";
			rep(j,c)
			{
				cout<<s<<res[i][j];
				s=" ";
			}
			cout<<endl;
		}
	}
	return 0;
}
