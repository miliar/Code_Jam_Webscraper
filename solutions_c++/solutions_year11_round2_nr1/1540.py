#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;

#define GI ({int t ;scanf("%d",&t);t;})
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
#define pr(x) cout<<#x<<" : "<<x<<endl<<flush; 
typedef vector<int> VI;
typedef long long LL;
typedef unsigned long long uLL;
typedef pair<int,int> pII;
typedef pair<string,int> pSI;
typedef map<int,int> mII;
typedef map<string,int> mSI;
typedef vector<string> VS;


char tab[101][101];

int main ()
{
	int T = GI;
	
	FORZ (t, T) {
		int n;
		cin >> n;
		
		FORZ(i, 101)
			FORZ(j, 101)
				tab[i][j] = ' ';
		
		FORZ(i, n)
			FORZ(j, n)
				cin >> tab[i][j];		
				
		double wp[n], owp[n], oowp[n];
		
		FORZ (i, n) {
			int p = 0, w = 0;
			FORZ (j, n) {
				if (tab[i][j] == '.') continue;
				p ++;
				if (tab[i][j] == '1') w ++;
			}
			wp[i] = w * 1.0 / p;
			//cout << wp[i] << "\t";
		}
		//cout << "\n";
						
		FORZ (team, n) {
		
			char a[n][n];
			FORZ(i, n) {
				FORZ(j, n) {
					a[i][j] = tab[i][j];
				}
			}
			
			double owpteam = 0.0;
			int den = 0;
			
			FORZ (k, n) {
				if (k == team) continue;
				if (tab[team][k] == '.') continue;
				den ++;
				int p = 0, w = 0;
				FORZ (l, n) {
					if (l == team) continue;
					if (a[k][l] == '1') p ++, w ++;
					else if (a[k][l] == '0') p ++;
				}
				double wpteam = w * 1.0 / p;
				owpteam += wpteam;
			}
			
			owp[team] = owpteam / den;
			//cout << owp[team] << "\t";
		}
		//cout << "\n";
		
		FORZ (i, n) {
			int den = 0; double oowpteam = 0.0;
			FORZ (j, n) {
				if (i == j || tab[i][j] == '.') continue;
				oowpteam += owp[j];
				den ++;
			}
			oowp[i] = oowpteam * 1.0 / den;
			//cout << oowp[i] << "\t";
		}
		//cout << "\n";
		
		printf ("Case #%d:\n", t + 1);
		
//		RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

		double rpi[n];
		FORZ (i, n) {
			rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf ("%0.12f\n", rpi[i]);	
		}
		
	}
	
	return 0;
}


