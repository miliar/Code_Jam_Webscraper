/*
** Khamitbekov Madi
** Kazakhstan, Almaty
** Kazakh-Turkish High School, 2011
*/
#include <algorithm>
#include <iostream>
#include <string.h>
#include <utility>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>   
#include <cmath>
#include <queue>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector <vector <int> >  vvi;
typedef vector <pair <int, int> >  vpi;
typedef queue  <pair <int, int> > qpi;

#define abs(x) ((x) > 0 ? (x) : -(x))
#define all(v) (v).begin(), (v).end()
#define sq(x) ((x)*(x))
#define len length()
#define pb push_back
#define mp make_pair
#define inf 7777777
#define eps (1e-7)
#define sz size()
#define s second
#define f first

int main ()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	int T, n, x[1000];
	int psa=1, psb=1;
	char c[1000];
	cin >> T;
	vector <int> o, b;
	int dpo[1000], dpb[1000], dp[1000];
	for (int t = 0; t < T; t++) {
		cin >> n;
		cout << "Case #" << t+1 << ": ";
		int res = 0;
		int d = 0;
		int ls = -1;
		for (int i = 0; i < n; i++) {
			cin >> c[i] >> x[i];
			if (!i) dp[i] = x[i];
			else if (c[i] == c[i-1]) dp[i] = dp[i-1] + abs(x[i-1]-x[i])+1;
			else {
				int id = -1;
				for (int j = i-1; j >= 0; j--)
					if (c[j] == c[i]) {id = j;break;}
				int dis;
				if (id == -1) dis = x[i];
				else	      dis = abs(x[id]-x[i])+1;
				int w;
				if (id != -1) w = dp[id]+dis;
				else	      w = dis;
				if (w <= dp[i-1]) dp[i] = dp[i-1]+1;
				else	{
				           if (id == -1) dp[i] = dis;
				           else  	 dp[i] = dp[id]+dis;
				}
			}
		}
		//for (int i = 0; i < n; i++)	cout << dp[i] << " ";
		cout << dp[n-1] << "\n";
	}

	return 0;
}
    
