#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

int64 N, Pd, Pg;
int nt;

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	cin >> nt;
	for (int tn = 1; tn <= nt; ++tn)
	{
		cin >> N >> Pd >> Pg;

		int64 D;

		D = -1;

		if (Pd == 0)
		{
			D = 1;
		} else {
			for (int64 Kd = 1; Kd < 10001; ++Kd)
			{
				if ((Kd * 100) % Pd) continue;
				D = (Kd * 100) / Pd;
				if (Kd > D)
				{
					D = -1;
					continue;
				}
				break;
			}
		}

		int ok = 1;

		if (D > N) ok = 0;
		if (Pd != 100 && Pg == 100) ok = 0;
		if (Pg == 0 && Pd != 0) ok = 0;

		cout << "Case #" << tn << ": ";
		if (ok)
			puts("Possible");
		else
			puts("Broken");
	}

	return 0;
}