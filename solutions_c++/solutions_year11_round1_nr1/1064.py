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
#define MAX_N 100002
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
	int T,PD,PG;
	long long N;
	bool yes;
	cin >> T;
	for(int i = 1;i <= T;i++)
	{
		yes = true;
		cin >> N >> PD >> PG;
		if(PG == 100 && PD != 100)
		{
			yes = false;
		}
		else if(PG == 0 && PD != 0)
		{
			yes = false;
		}
		else
		{
			if(N >= 100)
			{
				yes = true;
			}
			else
			{
				yes = false;
				for(int j = 1;j <= N;j++)
				{
					if((j * PD) % 100 == 0)
					{
						yes = true;
						break;
					}
				}
			}
		}
		cout << "Case #" << i << ": ";
		if(yes)cout << "Possible" << endl;
		else cout << "Broken" << endl;
	}
return 0;
}
