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
		int a[1002];
		int r, k, n;
		cin >> r >> k >> n;
		queue <int > Q;
		
		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
			Q.push(a[i]);
		}
		long long ans = 0;
		while (r--)
		{
			int cnt = 0;
			queue <int > Q2;
			while (!Q.empty() && Q.front() + cnt <= k)
			{
				cnt += Q.front();
					ans += Q.front();
					Q2.push(Q.front());
					Q.pop();
			}

			while (!Q2.empty())
			{
				Q.push(Q2.front());
				Q2.pop();
			}

			//cout << ans << endl;
		}

		printf ("Case #%d: %d\n",ca++, ans);
	}
}