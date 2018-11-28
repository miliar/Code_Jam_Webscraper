#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

template <class T>
inline const T& TMIN(const T& x, const T& y)
{ return (y<x ? y : x); }

template <class T>
inline const T& TMIN(const T& x, const T& y, const T& z)
{ return (y<x ? TMIN(y,z) : TMIN(x,z)); }

void Solve();

void main()
{
	int N;
	scanf("%d", &N);

	for(int n = 1; n <= N; n++)
	{
		printf("Case #%d: ", n);

		Solve();

		printf("\n");
	}

}

#define MAX_S_LEN 33
// case #n: 과 CR은 이미 main에서 출력되었음
void Solve()
{
	int x = 0, y = 0;

	int xdir = 0, ydir = 1; // north

	int L;
	scanf("%d", &L);

	vector<pair<int, int>> vwall;
	vector<pair<int, int>> hwall;

	for(int i = 0; i < L; i++)
	{
		char S[MAX_S_LEN];
		int T;
		scanf("%s %d", &S, &T);


		for(int j = 0; j < T; j++)
		{
			int len = strlen(S);
			for(int k = 0; k < len; k++)
			{
				if(S[k] == 'F')
				{
					if(xdir == 0)
					{
						if(ydir == 1)
						{
							vwall.push_back(make_pair(x, y));
						}
						else
						{
							vwall.push_back(make_pair(x, y-1));
						}
					}
					else
					{
						if(xdir == 1)
						{
							hwall.push_back(make_pair(x, y));
						}
						else
						{
							hwall.push_back(make_pair(x-1, y));
						}
					}

					x += xdir;
					y += ydir;

					//printf("(%d, %d)", x, y);
				}
				else if(S[k] == 'L')
				{
					if(xdir == 0)
					{
						if(ydir == 1)
						{
							xdir = -1;
							ydir = 0;
						}
						else
						{
							xdir = 1;
							ydir = 0;
						}
					}
					else
					{
						if(xdir == 1)
						{
							xdir = 0;
							ydir = 1;
						}
						else
						{
							xdir = 0;
							ydir = -1;
						}
					}
				}
				else // 'R'
				{
					if(xdir == 0)
					{
						if(ydir == 1)
						{
							xdir = 1;
							ydir = 0;
						}
						else
						{
							xdir = -1;
							ydir = 0;
						}
					}
					else
					{
						if(xdir == 1)
						{
							xdir = 0;
							ydir = -1;
						}
						else
						{
							xdir = 0;
							ydir = 1;
						}
					}
				}
			}
		}
	}

	//printf("x = %d, y = %d ", x, y);

	// pocket detection

	int iPocketCount = 0;
	int iInsideCount = 0;

	for(int px = -99; px < 99; px++)
	{
		for(int py = -99; py < 99; py++)
		{
			// h - outside check
			int small_hw = 0;
			int large_hw = 0;
			int small_vw = 0;
			int large_vw = 0;

			for(int hw = 0; hw < hwall.size(); hw++)
			{
				// same x
				if(hwall[hw].first == px)
				{
					if(hwall[hw].second <= py)
					{
						small_hw++;
					}
					else
					{
						large_hw++;
					}
				}
			}
			for(int vw = 0; vw < vwall.size(); vw++)
			{
				if(vwall[vw].second == py)
				{
					if(vwall[vw].first <= px)
					{
						small_vw++;
					}
					else
					{
						large_vw++;
					}
				}
			}

			// outside
			if(small_vw % 2 == 0 && large_vw % 2 == 0 && small_hw % 2 == 0 && large_hw % 2 == 0)
			{
				// hpocket satisfy
				if(small_hw > 0 && large_hw > 0)
				{
					iPocketCount++;
				}
				else if(small_vw > 0 && large_vw > 0)
				{
					iPocketCount++;
				}
			}
			else
			{
				iInsideCount++;
			}
		}
	}

	//printf("%d ", iInsideCount);
	printf("%d ", iPocketCount);
		


}