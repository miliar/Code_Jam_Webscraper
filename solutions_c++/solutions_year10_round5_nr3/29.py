#include <cstdio>
#include <iostream>
#include <map>
using namespace std;
#define oo 100006
map<int,int> f,g;
int a[oo],M;
int N;

inline void Readin()
{
	f.clear();
	M=0;

	cin >> N;
	for (int i=1;i<=N;++i)
	{
		int x,y;
		cin >> x >> y;
		f[x]=y;
		if (y>1) ++M;
	}
}

inline void Solve()
{
	int cnt=0;
	while (M)
	{
		++cnt;
		g=f;
		for (map<int,int>::iterator i=f.begin();i!=f.end();++i)
			if (i->second>=2)
			{
				g[i->first-1]+=1;
				g[i->first]-=2;
				g[i->first+1]+=1;
				break;
			}
		f=g;
		
		M=0;
		for (map<int,int>::iterator i=f.begin();i!=f.end();++i)
			if (i->second>=2) ++M;
	}
	
	cout << cnt << endl;
}

int main()
{
	int Test,Case=0;
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
