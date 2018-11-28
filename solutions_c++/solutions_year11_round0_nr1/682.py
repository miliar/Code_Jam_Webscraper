#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable: 4018)
#ifdef NDEBUG
	#define _SECURE_SCL 0
#endif
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

int NN, TT;
int N;
int APos, BPos, ATime, BTime;
int Total;

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		APos = 1;
		BPos = 1;
		ATime = 0;
		BTime = 0;
		Total = 0;
		cin >> N;
		while (N-- > 0)
		{
			char Col;
			int But;
			cin >> Col >> But;
			if (Col == 'B')
			{
				int Dis = abs(APos - But);
				ATime -= Dis;
				if (ATime < 0)
				{
					Total += -ATime;
					BTime += -ATime;
				}
				APos = But;
				Total++;
				ATime = 0;
				BTime++;
			}
			else
			{
				int Dis = abs(BPos - But);
				BTime -= Dis;
				if (BTime < 0)
				{
					Total += -BTime;
					ATime += -BTime;
				}
				BPos = But;
				Total++;
				BTime = 0;
				ATime++;
			}
		}
		printf("Case #%d: ", TT);
		printf("%d\n", Total);
	}
	return 0;
}
