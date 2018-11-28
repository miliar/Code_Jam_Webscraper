#pragma comment(linker, "/STACK:16777216")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <utility>

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )

using namespace std;

int t,n,p,mark,ans;
vector<int> ggl;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	forn(i,t)
	{
		ans = 0;
		cin >> n >> p >> mark;
		ggl.clear();
		ggl.resize(n);
		forn(i,n)
			cin >> ggl[i];
		int barely = mark + (mark-2)*2, exactly = mark + (mark-1)*2;
		forn(i,n)
		{
			if (ggl[i] >= exactly)
				ans++;
			else if (ggl[i] >= barely && p && ggl[i])
			{
				p--;
				ans++;
			}
			else if (!ggl[i] && !mark)
				ans++;
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}