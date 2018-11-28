#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
pair<int, int> A[200]; // pos, count

pair<int, int> getRange(pair<int, int> S, int shift, int d)
{
	int left, right;
	left = S.first - shift;
	right = left + d*(S.second - 1);

	return make_pair(left, right);
}

int getTime(int pos, pair<int, int> to)
{
	return max(abs(pos - to.first), abs(pos - to.second) );
}

int main()
{
	int T, test;

	cin >> T;
	for (test=1;test<=T;test++)
	{
		int d, n;
		cin >> n >> d;
		d*=2;

		for (int i=0;i<n;i++)
		{
			int pos, Count;
			cin >> pos >>  Count;
			A[i] = make_pair(pos*2, Count);
		}

		int L=A[0].second*d/2 + 1, R=1000000000;
		int Min = 2000000000;

		//first
		//while(L<=R)

		for (int M=0;M<=10000;M++)
		{
			//int M = (L+R)/2;
			int last;

			pair<int, int> first = getRange(A[0], M, d);
			int Time = getTime(A[0].first, first);

			last = first.second;

			bool f = true;
			for (int i=1;i<n;i++)
			{
				int delta = A[i].first - last - d;
				if (delta == 0)
				{
					pair<int, int> range = getRange(A[i], 0, d);
					int curr_t = getTime(A[i].first, range);
					if (curr_t > Time)
					{
						f = false;
						break;
					}
					
					last = range.second;
				}
				else if (delta<0)
				{
					pair<int, int> range = getRange(A[i], delta, d);
					int curr_t = getTime(A[i].first, range);
					if (curr_t > Time)
					{
						f = false;
						break;
					}

					last = range.second;
				}
				else // delta>0
				{
					pair<int, int> range = getRange(A[i], delta, d);
					int curr_t = getTime(A[i].first, range);
					if (curr_t <= Time)
					{
						last = range.second;
					}
					else
					{
						int len = range.second - range.first;
						int minT = len/2;
						if (minT > Time)
						{
							f = false;
							break;
						}
						else
						{
							int shift;
							if (delta>minT)
							{
								shift = minT + (Time-minT);
							}
							else
							{
								shift = minT - (Time-minT);
							}

							pair<int, int> range2 = getRange(A[i], shift, d);
							int curr_t = getTime(A[i].first, range2);
							if (curr_t>Time || range2.first-d < last)
							{
								f = false;
								break;
							}
							
							last = range2.second;
						}
					}

					
				}
			}

			if (f)
			{
				if (Time<Min)
					Min = Time;

				//R = M - 1;
			}
			else
			{
				//L = M + 1;
			}
		}

		cout << "Case #" << test << ": " << (((double)Min)/2.0) << endl;

	}

	return 0;
}