#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <ctime>
#include <iomanip>
#include <time.h>
#include <string.h>

using namespace std;

#ifdef ONLINE_JUDGE
void init()
{
}
#else
FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("C-large.in", "r", stdin);
	outputstream = freopen("C-large.out", "w", stdout);
}
#endif

int tonum_int(const string& str)
{
	int num;
	stringstream ss(str);
	ss>>num;
	return num;
}

int num[1001];
int kk[30];

int main()
{
	init();
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		int n;
		cin >> n;
		int mini = (1<<30);
		int sum = 0;
		memset(kk, 0, sizeof(kk));
		for (int j = 0; j < n; ++j)
		{
			cin >> num[j];
			sum += num[j];
			mini = min(mini, num[j]);
			for (int k = 0; k < 20; ++k)
			{
				if (num[j] & (1 << k))
				{
					kk[k] = (kk[k] + 1) % 2;
				}
			}
		}
		bool brk = false;
		for (int j = 0; j < 20; ++j)
		{
			if (kk[j] == 1)
			{
				cout << "NO" << endl;
				brk = true;
				break;
			}
		}
		if (!brk)
		{
			cout << sum - mini << endl;
		}
	}
	return 0;
}
