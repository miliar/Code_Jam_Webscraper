
#include <stdio.h>
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
#define sz size()
#define mp make_pair
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define MIN(v) *min_element(all(v))
#define MAX(v) *max_element(all(v))
#define last(a) int(a.size() - 1)

int case_number = 0;
#define gout case_number++, printf("Case #%d: ",case_number), cout

#define fs first
#define sc second


typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<long double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
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
	
	int tt;
	cin >> tt;
	
	while (tt--) {
		
		
		int N, L, H;
		cin >> N >> L >> H;
		
		vi entrada(N);
		
		fi(N) cin >> entrada[i];
		
		int resultado = 0;
		
		for (int i =L ; i<=H; i++) {
			bool conseguido = true;
			
			fj(N) {
				if (entrada[j]%i != 0 && i % entrada[j] != 0) conseguido = false;
			}
			
			if (conseguido == true){
				resultado = i;
				break;
			}
			
		}
		
		gout;
		
		if (resultado == 0) cout << "NO" << endl;
		else cout << resultado << endl;
		
	}
	
	
	
	return 0;
}
