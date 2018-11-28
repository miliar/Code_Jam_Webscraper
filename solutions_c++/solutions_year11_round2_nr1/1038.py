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
typedef unsigned long long ull;
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
	#ifndef ONLINE_JUDGE
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);
	#endif

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		char c[200][200];
		double wp[200], owp[200], oowp[200], total[200], win[200];
		int n;
		cout << "Case #" << t+1 << ":\n";
		cin >> n;
		for (int i = 0; i < n; i++) { 
			for (int j = 0; j < n; j++)	cin >> c[i][j];
			total[i] = win[i] = wp[i] = owp[i] = oowp[i] = 0;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++)
				if (c[i][j] != '.') {
					total[i]++;
					if (c[i][j] == '1') win[i]++;
				}
			if (total[i])
			wp[i] = win[i]/total[i];
		}
		for (int i = 0; i < n; i++) {
			double k = 0;
			owp[i] = 0;
			for (int j = 0; j < n; j++) {
				if (!total[j]) continue;
				if (c[j][i] == '1') owp[i] += (win[j]-1)/(total[j]-1);
				if (c[j][i] == '0') owp[i] += (win[j])/(total[j]-1);
				if (c[j][i] != '.') k++;
			}
			if (k)            
			owp[i] /= k;
		}
		for (int i = 0; i < n; i++) {
			double k = 0;
			for (int j = 0; j < n; j++)
				if (c[i][j] != '.') oowp[i] += owp[j], k++;
			if (k)
			oowp[i] /= k; 
		}
		for (int i = 0; i < n; i++) cout << 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] << endl;//printf ("%.6lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
	}
	return 0;
}
    
