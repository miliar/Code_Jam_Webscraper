#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <cctype>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long int64;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<string> vs;

template<class T> T abs(T x){return x>0 ? x:(-x);}
template<class T> T sqr(T x){return x*x;}

const int maxn=11;

int n,m;
int a[maxn];
int d[maxn][1<<maxn];
bool b[1<<maxn][1<<maxn];

bool ok(int x,int y)
{
	return !(x&y) && !(x&(2*y)) && !((2*x)&y);
}

int Nbits(int x)
{
	int res=0;
	while(x)
	{
		if(x&1) res++;
		x/=2;
	}
	return res;
}

int nbits[1<<maxn];

int main()
{
	int tc;
	cin >> tc;
	for(int i=0;i<(1<<maxn);i++){
		nbits[i]=Nbits(i);
		for(int j=0;j<(1<<maxn);j++)
			b[i][j]=ok(i,j);
	}
	for(int ic=0;ic<tc;ic++)
	{
		printf("Case #%d: ",ic+1);
		cin >> n >> m;
		memset(a,0,sizeof(a));
		memset(d,0,sizeof(d));
		for(int i=0;i<n;i++){
			string s;
			cin >> s;
			for(int j=0;j<m;j++)
				if(s[j]=='x') a[j]|=(1<<i);
		}
		swap(n,m);
		for(int i=0;i<(1<<m);i++)
			if(!(i&a[0]))
				d[0][i]=nbits[i];
		for(int i=1;i<n;i++)
			for(int j=0;j<(1<<m);j++)
				if(!(j&a[i]))
					for(int k=0;k<(1<<m);k++)
						if(b[j][k])
							d[i][j]=max(d[i][j],d[i-1][k]+nbits[j]);
		int res=0;
		for(int i=0;i<(1<<m);i++)
			res=max(res,d[n-1][i]);
		cout << res << "\n";
	}
	return 0;
}
