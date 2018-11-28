#include <iostream>
#include <algorithm>

using namespace std;

#define NMAX 2001

__int64 getProfit()
{
	__int64 p[NMAX];

	__int64 R,k,N;
	cin >> R >> k >> N;
	for(__int64 i=0; i<N; ++i)
		cin >> p[i];
	////////////////////////

	__int64 prof[NMAX];
	__int64 jmp[NMAX];

	for(__int64 i=0; i<N; ++i)
	{
		__int64 sum=0;
		__int64 j=i;

		while(sum+p[j]<=k)
		{
			sum += p[j];
			j = (j+1)%N;
			if (i==j) break;
		}

		prof[i] = sum;
		jmp[i] = j;
	}

	///////////////////////

	__int64 tl[NMAX][2]; //[0] iter in time, [1] total profit

	for(__int64 i=0; i<N; ++i)
		tl[i][0] = -1;

	__int64 pos = 0, sum = prof[pos];

	tl[pos][0] = 0;
	tl[pos][1] = sum;
	pos = jmp[pos];

	bool big_jump = false;
	for(__int64 i=1; i<R; ++i)
	{
		__int64 old_i = tl[pos][0];
		__int64 old_sum = tl[pos][1];
		__int64 old_sum2 = sum;

		tl[pos][0] = i;
		sum += prof[pos];
		tl[pos][1] = sum;

		if (!big_jump && old_i != -1)
		{
			__int64 delta_profit = sum - old_sum;
			__int64 delta_i = i-old_i;
			sum = old_sum2 + delta_profit * ((R-i)/delta_i);
			i += delta_i * ((R-i)/delta_i)-1;
			big_jump = true;
		}
		else
			pos = jmp[pos];						
	}

	return sum;
}

int main()
{
	int t;
	cin >> t;
	for(int i=0; i<t; ++i)
		cout << "Case #"<<i+1<<": "<<getProfit()<<endl;

	return 0;
}