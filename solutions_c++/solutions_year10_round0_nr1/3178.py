#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <numeric>
using namespace std;

typedef long long tint;
typedef pair<int,int> pii;
typedef complex<double> pto;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;

#define forn(i,n) forsn(i,0,n)
#define forsn(i,s,n) for( tint ___n=tint(n), i=tint(s) ; i<___n ; ++i )
#define fordn(i,n) fordsn(i,0,n)
#define fordsn(i,s,n) for( tint ___s=tint(s), i=tint(n)-1 ; i>=___s ; --i )
#define forall(i,c) for( typeof((c).begin()) i=(c).begin() ; i!=(c).end() ; ++i )
#define all(c) (c).begin(), (c).end()
#define sz(a) ((int)(a).size())
#define pb push_back
#define clear(x,c) memset(x,c,sizeof(x))

const int mx[] = {-1,0,1,0};
const int my[] = {0,-1,0,1};
const int inf=0x7fffffff;

//#define cin ent
//#define cout sal

int main() {
	
	int tCases;
	cin >> tCases;
	for(int i = 1; i <= tCases; i++){
		int N, K;
		cin >> N >> K;
		int snappers = (1 << N) - 1;
		if(snappers == (K % (snappers + 1))){
			cout << "Case #" << i << ": " << "ON" << endl;
		}
		else{
			cout << "Case #" << i << ": " << "OFF" << endl;
		}
	}

    return 0;
}
