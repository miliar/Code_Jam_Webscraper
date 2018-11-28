
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <sstream>
#include <cmath>

using namespace std;


#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define fi(n) forn(i,n)
#define fj(n) forn(j,n)
#define fk(n) forn(k,n)
#define sz .size()
#define mp make_pair
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define last(a) int(a.size() - 1)

int case_number = 0;
#define gout case_number++, printf("Case #%d: ",case_number), cout

#define fs first
#define sc second


typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;


const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const ll inf64 = ((ll)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;


int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }



int main( )
{
	int T = ni();
	while (T--){
		int N = ni();
		int S = ni();
		int p = ni();
		int sol = 0;
		fi(N){
			int total = ni();
			int div = total / 3;
			int mod = total % 3;
			
			if (div >= p) sol++;
			else if (div == p-1){
				if ( div > 0 && mod == 0 && S > 0){
					sol++;
					S--;
				}
				else if (mod > 0) sol++;
			}
			else if (div == p-2 && mod == 2 && S > 0){
				sol++;
				S--;
			}
		}
		gout << sol << endl;
	}
	
	return 0;
}
