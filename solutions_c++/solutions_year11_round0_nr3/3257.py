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

	int T, n, a[1000];

	cin >> T;
	for (int t = 0; t < T; t++) {
		cout << "Case #" << t+1 << ": ";
		cin >> n;
		for (int j = 0; j < n; j++)	cin >> a[j];
		int res = -1;
		for (int i = 0; i < (1<<n); i++) {
			int s1=0, s2=0, s = 0;
			for (int j = 0; j < n; j++) 
				if (i&(1<<j)) s1 ^= a[j], s += a[j];
				else	      s2 ^= a[j];
			if (s1 == s2 && s1 != 0) res = max (res, s);
		}                   	
		if (res == -1) cout << "NO\n";
		else	       cout<< res << endl;
	}

	return 0;
}
    
