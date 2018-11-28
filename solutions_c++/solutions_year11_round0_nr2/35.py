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
	inputstream = freopen("B-large.in", "r", stdin);
	outputstream = freopen("B-large.out", "w", stdout);
}
#endif

int tonum_int(const string& str)
{
	int num;
	stringstream ss(str);
	ss>>num;
	return num;
}

int maps[100][100];
int opp[100][100];

int main()
{
	init();
	int T;
	cin >> T;
	for (int ii = 1; ii <= T; ++ii)
	{
		memset(maps, 0, sizeof(maps));
		memset(opp, 0, sizeof(opp));
		int C;
		cin >> C;
		char a, b, c;
		for (int j = 0; j < C; ++j)
		{
			cin >> a >> b >> c;
			maps[(int)a][(int)b] = maps[(int)b][(int)a] = (int)c;
		}
		int D;
		cin >> D;
		for (int j = 0; j < D; ++j)
		{
			cin >> a >> b;
			opp[(int)a][(int)b] = true;
			opp[(int)b][(int)a] = true;
		}
		int N;
		cin >> N;
		string str;
		cin >> str;
		vector<char> res;
		for (int i = 0; i < str.size(); ++i)
		{
			char ch = str[i];
			res.push_back(ch);
			if (res.size() >= 2)
			{
				char c1 = res[res.size()-1];
				char c2 = res[res.size()-2];
				if (maps[c1][c2] != 0)
				{
					res.pop_back();
					res.pop_back();
					res.push_back((char)maps[c1][c2]);
				}
				else
				{
					for (int j = 0; j + 1 < res.size(); ++j)
					{
						if (opp[ch][res[j]])
						{
							res.clear();
							break;
						}
					}
				}
			}
		}
		cout << "Case #" << ii << ": [";
		for (int i = 0; i < res.size(); ++i)
		{
			if (i != 0) cout << ", ";
			cout << res[i];
		}
		cout << "]" << endl;
	}
					
						
				
		
			
	return 0;
}
