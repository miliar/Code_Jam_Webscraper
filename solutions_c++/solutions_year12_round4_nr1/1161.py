#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <algorithm>
#include <utility>
#define PB push_back
#define SIZE(x) (int)x.size()

using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef map<int,bool> MIB;

VI dist,len;
int D;

#define MAX 10100
#define INF 2000000000
VI maxH;
VI minH;

bool check(int nr, int h)
{
	int dokad=dist[nr]+h;
	if (dokad>=D) return true;

	int& mah=maxH[nr];
	int& mih=minH[nr];
	if (h<=mah) return false;
	if (h>=mih) return true;

	int poz=(int)(upper_bound(dist.begin(),dist.end(),dokad)-dist.begin())-1;
	for (int i=nr+1; i<=poz; ++i)
	{
		int nh=min(dist[i]-dist[nr],len[i]);
		if (check(i,nh))
		{
			mih=h;
			return true;
		}
	}
	mah=h;
	return false;
}

int main()
{
	ios::sync_with_stdio(0);

	int Testow; cin>>Testow;
	for (int test=1; test<=Testow; ++test)
	{
		int N; cin>>N;
		dist.resize(N); len.resize(N);
		maxH.clear(); minH.clear();
		maxH.resize(N,0); minH.resize(N,INF);
		for (int i=0; i<N; ++i) cin>>dist[i]>>len[i];
		cin>>D;

		bool czy=check(0,dist[0]);
		cout<<"Case #"<<test<<": "<<(czy? "YES":"NO")<<endl;		
	}

	return 0;
}