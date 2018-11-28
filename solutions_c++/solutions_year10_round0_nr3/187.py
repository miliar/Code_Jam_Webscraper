#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 1000;

int g[MAXN];
int t[MAXN];
long long preSum[MAXN];
int R, k, N;

long long calc(int head)
{
	if (R == 0)
		return 0;
	long long res = 0;
	long long sum;
	int r = 0;
	preSum[0] = 0;
	while (r < R && t[head] == -1)
	{
		t[head] = r;
		int tail = head;
		sum = g[head];
		tail = (head+1)%N;
		for(; head != tail && sum+g[tail] <= k; tail = (tail+1)%N)
			sum += g[tail];
		res += sum;
		r++;
		preSum[r] = res;
		head = tail;
	}

	res += ((R-t[head])/(r-t[head])-1) * (res-preSum[t[head]]);
	R = (R-t[head])%(r-t[head]);
	memset(t, -1, sizeof(t));
	res += calc(head);

	return res;
}

void process()
{
	cin >> R >> k >> N;
	for(int i=0; i<N; i++)
		cin >> g[i];
	memset(t, -1, sizeof(t));
	cout << calc(0) << endl;
}

int main()
{
	int T;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		printf("Case #%d: ", i+1);
		process();
	}
}

