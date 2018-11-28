//Sat May  8 01:43:35 CDT 2010
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

using namespace std;

int main(int argc, char* argv[])
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for (int ncase = 1; ncase <= T; ncase++)
	{
		long R, k, N;
		cin >> R >> k >> N;
		queue<long> v;
		for (long i = 0; i < N; i++)
		{
			int number;
			cin >> number;
			v.push(number);
		}

		long long cost = 0;	//The total cost;
		long long take = 0;	//The temp number of riders;
		long count = 0;	//The number of groups;

		for(; R>0; )
		{
			if(take + v.front() > k || count == N)
			{
				R--;
				take = 0;
				count = 0;
			}
			else
			{
				v.push(v.front());
				cost += v.front();
				take += v.front();
				v.pop();
				count++;
			}
		}
		cout << "Case #" << ncase << ": " << cost << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
