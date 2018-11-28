#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <queue>
//#include <cmath>

#define mp make_pair
#define sz(v)((int)((v).size()))
#define all(v) v.begin(),v.end()
#define pb push_back

using namespace std;

const int maxn=110;
const int maxm=1100;
const int inf=100000000;

typedef pair<int,int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x){return x>0 ? x:(-x);}
template<class T> T sqr(T x){return x*x;}

int d[maxn][maxm];

int n,m;

vi q;

int go(int x,int y)
{
	if(x>=m) return 0;
	int& res=d[x][y];
	if(res!=-1) return res;
	res=inf;
	if(q[x]!=y) return res=go(x+1,y);
	res=inf;
	for(int i=0;i<n;i++)
		if(i!=q[x])
			res=min(res,go(x+1,i)+1);
	return res;
}

void GetLine(int& x)
{
	char ts[10000];
	gets(ts);
	sscanf(ts,"%d",&x);
}

int main()
{
	int tc;
	GetLine(tc);
	for(int ic=0;ic<tc;ic++){
		memset(d,-1,sizeof(d));
		GetLine(n);
		q.clear();
		map<string,int> M;
		char ts[10000];
		for(int i=0;i<n;i++)
		{			
			gets(ts);
			M[ts]=i;
		}
		GetLine(m);
		for(int i=0;i<m;i++)
		{
			gets(ts);
			q.push_back(M[ts]);
		}
		int res=inf;
		for(int i=0;i<n;i++)
			res=min(res,go(0,i));
		cout << "Case #" << (ic+1) << ": ";
		cout << res << "\n";
	}
	return 0;
}
