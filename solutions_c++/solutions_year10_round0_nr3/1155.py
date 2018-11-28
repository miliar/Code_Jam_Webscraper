#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int MaxN = 10010;

long long sum[MaxN];
long long money[MaxN];
long long ans[MaxN];
int vst[MaxN];
int reach[MaxN];
int R, K, N;

void solve()
{
	memset(vst, 0, sizeof(vst));
	int st = 0, t = 0;
	while(++t<=R && !vst[st])
	{
		vst[st] = t;
		ans[t] = ans[t-1] + money[st];
		st = reach[st];	
	}
//	for(int i=1; i<t; i++)	cout << ans[i] << " ";cout << endl;
	long long ret = ans[t-1];	
	if(t <= R)
	{
		R -= t - 1;
		int C = t - vst[st];
		ret += R/C*(ans[t-1]-ans[vst[st]-1]);
		ret += ans[vst[st]+R%C-1] - ans[vst[st]-1];
	}
	cout << ret << endl;
//	cout << ret << "  " << ck << endl;
//	if(ret != ck)	puts("wrong");
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int T;	cin >> T;
	for(int t=1; t<=T; t++)
	{
		printf("Case #%d: ", t);
		cin >> R >> K >> N;
		for(int i=0; i<N; i++)	cin >> sum[i];
//			sum[i] = rand()%K+1;
		for(int i=0; i<N; i++)
		{
			long long tmp = sum[i];
			int j = (i+1) % N;	
			while(j != i)
			{
				tmp += sum[j];
				if(tmp > K)	break;
				j = (j+1) % N;	
			}
			reach[i] = j;
			money[i] = tmp - (j!=i)*sum[j];	
		}
		solve();
	}
	
//	while(1);
	return 0;	
}
