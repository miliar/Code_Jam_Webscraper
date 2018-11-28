//#pragma comment(linker, "/STACK:16777216")
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
#include <iterator>
#include <utility>

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned char UCHAR;
using namespace std;

const int N_MAX = 256;
char c[N_MAX][N_MAX], o[N_MAX][N_MAX];

int main()
{

#ifdef DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

    int tst;
    cin >> tst;


    for (int t = 1; t <= tst; ++t)
    {
    	vector< pair<UCHAR, UCHAR> > cv, ov;
    	int cnt;
    	cin >> cnt;
    	for (int i = 0; i < cnt; ++i)
    	{
    		UCHAR u, v, w;
    		cin >> u >> v >> w;
    		cv.push_back(make_pair(u, v));
    		c[u][v] = c[v][u] = w;
    	}
    	
    	int ont;
    	cin >> ont;
    	for (int i = 0; i < ont; ++i)
    	{
    		UCHAR u, v;
    		cin >> u >> v;
    		ov.push_back(make_pair(u, v));
    		o[u][v] = o[v][u] = 1;
    	}
    	
    	int n;
    	cin >> n;
    	vector<UCHAR> q;
    	for (int i = 0; i < n; ++i)
    	{
    		UCHAR x;
    		cin >> x;
    		q.push_back(x);
    		for (;;)
    		{
    			if (q.size() <= 1U) break;
    			int n = q.size();
    			if (c[q[n - 2]][q[n - 1]] != 0)
    			{
    				UCHAR nc = c[q[n - 2]][q[n - 1]];
    				q.pop_back();
    				q.pop_back();
    				q.push_back(nc);
    			}
    			else
    			{
    				
    				for (int j = 0; j < n - 1; ++j)
    					if (o[q[j]][q[n - 1]])
    					{
    						
    						q.clear();
    						break;
    					}
    				
    				break;
    			}
    		}

    		#ifdef DEBUG
    		/*cerr << "[";
    		for (size_t i = 0; i + 1 < q.size(); ++i)
    			cerr << q[i] << ", ";
    		if (!q.empty()) cerr << q.back();
	    	cerr << "]\n";*/
    		#endif
    	}

    	cout << "Case #" << t << ": [";
    	for (size_t i = 0; i + 1 < q.size(); ++i)
    		cout << q[i] << ", ";
    	if (!q.empty()) cout << q.back();
    	cout << "]\n";

    	for (size_t i = 0; i < cv.size(); ++i)
    		c[cv[i].first][cv[i].second] = c[cv[i].second][cv[i].first] = 0;
    	for (size_t i = 0; i < ov.size(); ++i)
    		o[ov[i].first][ov[i].second] = o[ov[i].second][ov[i].first] = 0;
    }

	return 0;
}
