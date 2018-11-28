#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<queue>
using namespace std;

const int MaxN = 20000;

int D[MaxN], f[MaxN], L[MaxN];
int N, S;

vector<int> rem[MaxN];

bool run()
{
	scanf("%d", &N);
	D[0]=0;
	set<int> T;
	for(int i=1;i<=N;++i)
	{
		f[i] = -1;
		scanf("%d %d", D+i, L+i);
		rem[i].clear();
	}
	scanf("%d", &S);

	T.insert(0);

	for(int i=1;i<=N;++i)
	{
		if(T.size()==0)return false;
		if(i > 1 && *T.begin() == 0) continue;
		f[i] = *T.begin();
		if(i == 1) T.erase(0);
		int k = min(D[i] - D[f[i]], L[i]);

	//	cout << "f[ "<<i<<" ] = "<<f[i]<<"  k = "<<k<<endl;

		if(D[i]+k >= S) return true;
		T.insert(i);

	//	cout << "----> insert "<<i<<endl;

		int lo = 0, hi = N + 1, mid;
		while(lo+1<hi)
		{
			mid = lo + hi >> 1;
			if(D[i]+k >= D[mid]) lo = mid;
			else hi = mid;
		}

	//	cout << "lo = "<<lo<<endl;

		rem[lo].push_back(i);
		for(int j=0;j<rem[i].size();++j) {
			T.erase(rem[i][j]);
	//		cout << "----> erase "<<rem[i][j]<<endl;
		}
	}
	return false;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int test;scanf("%d", &test);
	for(int no=1;no<=test;++no)
	{
		printf("Case #%d: ",no);

		cerr << "no#"<<no<<endl;

		if(run()) puts("YES"); else puts("NO");
	}
	return 0;
}