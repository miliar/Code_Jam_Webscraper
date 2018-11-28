#include <iostream>
#include <cstdio>
using namespace std;

const int MAXN = 50;

int x[MAXN], v[MAXN];
bool good[MAXN];

void work()
{
	int N, K, B, T;
	cin >> N >> K >> B >> T;
	for(int i=0; i<N; i++)
		cin >> x[i];
	for(int i=0; i<N; i++)
		cin >> v[i];
	for(int i=0; i<N; i++)
		good[i] = (x[i]+v[i]*T >= B);
	
	int gCnt = 0, bCnt = 0;
	int res = 0;
	for(int i=N-1; i>=0; i--)
		if (good[i]){
			if (gCnt >= K)
				break;
			gCnt++;
			res += bCnt;
		}
		else
			bCnt++;
	if (gCnt >= K)
		cout << res << endl;
	else
		cout << "IMPOSSIBLE" << endl;
}

int main()
{
	int C;
	cin >> C;
	for(int i=0; i<C; i++){
		printf("Case #%d: ", i+1);
		work();
	}
}

