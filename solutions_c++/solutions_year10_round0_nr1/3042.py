#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime> 
#include <cfloat> 

using namespace std;

int main ()
{
	freopen("in.txt", "r", stdin);
	freopen("out2.txt", "w", stdout);
	int t;
	cin >> t;
	int ca = 1;
	while (t--)
	{
		int n, k;
		cin >> n >> k;
		int i;
		for (i = 0; i < n; i++)
		{
			if (k & (1 << i))
				continue;
			break;
		}
		if(i == n)
			printf ("Case #%d: ON\n", ca++);
		else printf ("Case #%d: OFF\n", ca++);
	}
}