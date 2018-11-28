#include <stdio.h>
#include <vector>

using namespace std;

long long T, R, k, N;
vector <int> v;
vector <long long> Ptr;
vector <long long> Mch;

void Hmch(int st)
{
	long long sum = 0;
	int pointer = st;

	for(int i = 0; i < N; i++)
	{
		if( pointer >= N )
			pointer = 0;

		if( sum + v[pointer] <= k )
			sum = sum + v[pointer];
		else
			break;

		pointer++;
		if( pointer >= N )
			pointer = 0;
	}

	Ptr.push_back(pointer);
	Mch.push_back(sum);
}

long long Func()
{
	for(int i = 0; i < N; i++)
	{
		Hmch(i);
	}

	long long ans = 0;

	int cur = 0;

	for(int i = 0; i < R; i++)
	{
		ans += Mch[cur];
		cur = Ptr[cur];
	}

	return ans;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	scanf("%d", &T);

	for(int i = 0; i < T; i++)
	{
		v.clear();
		Mch.clear();
		Ptr.clear();

		scanf("%d%d%d", &R, &k, &N);

		for(int i = 0; i < N; i++)
		{
			int tmp;
			scanf("%d", &tmp);
			v.push_back(tmp);
		}

		printf("Case #%d: %lld\n", i+1, Func());
	}

	return 0;
}