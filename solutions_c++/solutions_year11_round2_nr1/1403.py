#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;
 
#define DEBUG(x) //x
#define REP(i,a) for(int i=0;i<int(a);i++)
#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define VI vector<int>
#define size(x) int((x).size())
#define all(x) (x).begin(), (x).end()
#define MK(x, y) make_pair(x, y)
#define PB push_back
 
typedef pair<int, int> pii;

int main()
{
	int T; cin >> T;
	
	for (int i = 1; i <= T; i++)
	{
		cout << "Case #" << i << ":" << endl;
		int n; cin >> n;
		vector< vector< char> > m(n, vector<char> (n, 0));
		vector< vector<int> > g(n, vector<int>());
		vector<int> win(n, 0);
		vector<int> games(n, 0);
		
		for (int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
			{
				cin >> m[i][j];
				if (m[i][j] == '.')
					continue;
				g[i].push_back(j);
				games[i]++;
				if (m[i][j] == '1')
					win[i]++;
			}
			
		vector<double> wp(n), owp(n), oowp(n);
		
		for (int i = 0; i < n; i++)
			wp[i] = double(win[i]) / games[i];

		for (int i = 0; i < n; i++)
		{
			double sum = 0;
			for (int j = 0; j < size(g[i]); j++)
			{
				int o = g[i][j];
				if (m[o][i] == '1')
				{
					if (size(g[o]) > 1)
						sum += double(win[o]-1)/(size(g[o])-1);
				}
				else
				{
					if (size(g[o]) > 1)
						sum += double(win[o])/(size(g[o])-1);
				}
			}
			if (size(g[i]))
				sum /= size(g[i]);
			owp[i] = sum;
		}
				
		for (int i = 0; i < n; i++)
		{
			double sum = 0;
			for (int j = 0; j < size(g[i]); j++)
				sum += owp[g[i][j]];
			if (size(g[i]))
				sum /= size(g[i]);
			oowp[i] = sum;
		}
				
		//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
		for (int i = 0; i < n; i++)
			cout << 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i] << endl;
	}    
    return 0;
}

