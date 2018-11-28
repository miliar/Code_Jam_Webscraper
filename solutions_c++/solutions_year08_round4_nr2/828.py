#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

using namespace std;
typedef long long ll;

struct aaa
{
	int start;
        bool operator<(const aaa& o) const
        {
                return start<o.start;
        }
};

#if 0
        scanf(" ");
        gets(buf);
        n = 0;

        string s(buf);
        istringstream iss(s);
        string s2;
        while (iss >> s2)
                name[n++] = s2;
	vector<long> array1;
	array1.clear();
	
#endif

int main()
{
	int numCase;
	cin >> numCase;
	ll i, j, k,l,m, n, a;
	ll x,y;
	for (i = 0; i < numCase; i++)
	{
		int end = 0;
#if 0
1 1 1
1 2 64
10 10 1
#endif
	cin >>n >> m >> a;
int xx = 0;
	for(xx=0;xx<=n;xx++) {
		for(x=0;x<=n;x++) {
			for(y=0;y<=m;y++)  {
				for (j = x; j <= n; j++) {
					for (k = y; k <= m; k++)
					{
						if(abs((j-xx)*y-k*(x-xx)) == a) {
							end = 1;
							break;
						}
					}
					if(end==1)
						break;
				}
			if(end==1)
				break;
			}
			if(end==1)
				break;
		}
		if(end==1)
			break;
	}
		if(end == 0) {
		cout << "Case #" << (i+1) << ": " << "IMPOSSIBLE" << endl;
		} else {
		cout << "Case #" << (i+1) << ": " << xx << " 0 " << x << " " << y << " " << j << " "<< k << endl;
		}
	}
	return 0;
}
