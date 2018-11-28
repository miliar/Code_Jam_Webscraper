#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <sstream>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define INF 2000000000
#define EPS 1e-11
#define MAX_N 10000
using namespace std;

#ifdef _WIN32 
typedef __int64 int64; 
#else 
typedef long long int64; 
#endif 

typedef pair <int,int> ii;

int
main()
{
	int T,move,p2;
	char p1;
	char bef;
	int time,before,need;
	int posB,posO;
	cin >> T;
	for(int i = 1;i <= T;i++)
	{
		bef = 'C';
		time = 0;
		before = 0;
		posB = 1;
		posO = 1;
		cin >> move;
		while(move--)
		{
			cin >> p1 >> p2;
			if(p1 == 'B')
			{
				need = p2 - posB;
				if(need < 0)need *= -1;
				if(bef == 'B')
				{
					before = before + need + 1;
					time = time + need + 1;
				}
				else
				{
					bef = 'B';
					if(need <= before)
					{
						time = time + 1;
						before = 1;
					}
					else
					{
						time = time + (need - before) + 1;
						before = need - before + 1;
					}
				}
				posB = p2;
			}
			else
			{
				need = p2 - posO;
				if(need < 0)need *= -1;
				if(bef == 'O')
				{
					before = before + need + 1;
					time = time + need + 1;
				}
				else
				{
					bef = 'O';
					if(need <= before)
					{
						time = time + 1;
						before = 1;
					}
					else
					{
						time = time + (need - before) + 1;
						before = need - before + 1;
					}
				}		
				posO = p2;
			}
		}
		cout << "Case #" << i  << ": " << time << endl;
	}
return 0;
}
