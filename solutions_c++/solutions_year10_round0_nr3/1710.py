#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;
#define LL long long

const int MN = 2001;

LL sum[MN], cnt[MN], val[MN], nxt[MN], lastSum[MN], lastCnt[MN]; 
int main()
{

	int kases;

	cin >> kases;

	for(int kase = 1; kase <= kases; ++ kase)
	{

	    LL r, k, n;

		cin >> r >> k >> n;

		for(int i = 0; i < n; ++i)
		{
			cin >> val[i];
			lastCnt[i] = -1;
			lastSum[i] = -1;
		}

		for(int i = 0; i < n; ++i)
		{
			LL totalsum = 0;
			bool done = false;
			for(int j = 0; j < n; ++j)
			{
				int index = (i + j) % n;

				if(totalsum + val[index] <= k)
				{
					totalsum += val[index];
				}
				else
				{
					sum[i] = totalsum;
					nxt[i] = index;
					done = true;
					break;
				}
			}

			if(!done)
			{
				nxt[i] = i;
				sum[i] = totalsum;
			}
		}

		LL res = 0;

		LL pos = 0;
		LL rnd = 0;
		
		bool looped = false;

		while(rnd < r)
		{
			if(looped || lastSum[pos] == -1)
			{
				lastSum[pos] = res;
				lastCnt[pos] = rnd;
				res += sum[pos];
				pos = nxt[pos];
				++rnd;
			}
			else
			{
				LL loopSum = res - lastSum[pos];
				LL loopCnt = rnd - lastCnt[pos];
                
				LL leftRounds = r - rnd;
				
				LL loops = leftRounds / loopCnt;

				res += loops * loopSum;
				
				rnd += loops * loopCnt;

				looped = true;
			}
			
			
		}

		cout << "Case #" << kase << ": " << res << endl;
	}

	return 0;
}