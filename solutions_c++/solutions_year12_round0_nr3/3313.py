
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
#define sz size
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


void itoa(int i, char *buff){
	
	sprintf(buff, "%d", i);

}

int main( )
{
	int partitions[2000001] = {0};
	int partition = 1;
	
	fi(2000001){
		if(partitions[i] == 0){
			char buffer [33];
			itoa(i,buffer);
			string s1 (buffer);
			forit(it, s1){
				if ( (*it) != '0'){
					string s2 = string(it, s1.end());
					s2.append(s1.begin(),it);
					int ac = atoi(s2.c_str());
					if (ac < 2000001) partitions[ac] = partition;
				}
			}
			partition++;
		}
	
	}
	
	int T = ni();
	while(T--){
		int A = ni(), B = ni();
		multiset<int> myset;
		int sol = 0;
		for (int i = A; i <=B; i++){
			int ac = partitions[i];
			sol += myset.count(ac);
			myset.insert(ac);
		}
		gout << sol << endl;
	}
	
	return 0;
}
