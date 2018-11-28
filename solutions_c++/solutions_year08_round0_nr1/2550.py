#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int main()
{
 	ifstream fi;
	ofstream fo;
	
 	fi.open("A-large.in", ios::in);
 	fo.open("A-large.out", ios::out);
	
	int n;
	fi >> n;
	
	for (int j = 1; j <= n; j ++)
	{
		int nse, nq;
		set < string > se, se_;
		string tse, q;

		fi >> nse;

		for (int i = 0; i <= nse; i ++)
		{
			char ch[201];
			fi.getline(ch, 200, '\n');
			tse = ch;
			se.insert(tse);
		}
		se.erase("");
	
		fi >> nq;
		int rs = 0;

		for (int i = 0; i <= nq; i ++)
		{
			char ch[201];
			fi.getline(ch, 200, '\n');
			q = ch;
	
			if (se.count(q) == 1)
			{
				se_.insert(q);
	
				if (se.size() == se_.size())
				{
					rs ++;
					se_.clear();
					se_.insert(q);
				}
			}
		}
		fo << "Case #" << j << ": " << rs << endl;
	}
	fi.close();
	fo.close();
	return 0;
}
