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
	inputstream = freopen("in.txt", "r", stdin);
	outputstream = freopen("output.txt", "w", stdout);
}
#endif

int tonum_int(const string& str)
{
	int num;
	stringstream ss(str);
	ss>>num;
	return num;
}

char cmd[101];
int pos[101];

int main()
{
	init();
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int n;
		cin >> n;
		for (int j = 0; j < n; ++j)
		{
			cin >> cmd[j] >> pos[j];
		}
		int opos = 1;
		int bpos = 1;
		int res = 0;
		for (int j = 0; j < n; ++j)
		{
			if (cmd[j] == 'O')
			{
				int dif = abs(opos - pos[j]);
				res += (dif + 1);
				opos = pos[j];
				int tpos = -1;
				for (int k = j + 1; k < n; ++k)
				{
					if (cmd[k] == 'B')
					{
						tpos = pos[k];
						break;
					}
				}
				int bmove = min(dif + 1, abs(bpos - tpos));
				if (tpos != -1)
				{
					if (tpos > bpos)
					{
						bpos += bmove;
					}
					else
					{
						bpos -= bmove;
					}
				}
			}
			else
			{
				int dif = abs(bpos - pos[j]);
				res += (dif + 1);
				bpos = pos[j];
				int tpos = -1;
				for (int k = j + 1; k < n; ++k)
				{
					if (cmd[k] == 'O')
					{
						tpos = pos[k];
						break;
					}
				}
				int omove = min(dif + 1, abs(opos - tpos));
				if (tpos != -1)
				{
					if (tpos > opos)
					{
						opos += omove;
					}
					else
					{
						opos -= omove;
					}
				}
			}
		}
		cout << "Case #" << i << ": " << res << endl;
	}
		
			
	return 0;
}
