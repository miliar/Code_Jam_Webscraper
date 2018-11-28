#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cctype>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <utility>
#include <vector>
#include <bitset>
#include <deque>
#include <iomanip>
#include <complex>
#include <fstream>
#include <sstream>
#include <map>
//#include <climits>
//#include <list>

using namespace std;

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

#define show(x) cerr<<((#x))<<" = "<<((x))<<" "<<endl
#define bit(a,b) (((a)>>(b))&1)
#define gcd __gcd
#define endl '\n'
#define bcnt(x) ((__builtin_popcount(x)))
#define sz(x) ((int((x).size())))
#define sqr(x) ((((x))*((x))))
#define fx(x) fixed<<setprecision(x)

template<class T> inline void smn(T &a,const T &b){if(b<a) a=b;}
template<class T> inline void smx(T &a,const T &b){if(b>a) a=b;}
template<class T> inline T rev(const T & a){T _=a; reverse(_.begin(),_.end()); return _;}

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const double eps=1e-9;
const ld leps=1e-14;

int p[100000];
int t[100000];
int perm[100000];

bool cmp (const int &A, const int &B){
	return (p[A] * t[B] != p[B] * t[A]) ? (p[A] * t[B] > p[B] * t[A]) : (A<B);
}

int main()
{
	ios_base::sync_with_stdio(false);

	int T,N;

	cin >> T;

	for (int o=1; o<=T; o++){
		cin >> N;
		for (int i=1; i<=N; i++)
			cin >> t[i];
		for (int i=1; i<=N; i++)
			cin >> p[i];
		for (int i=1; i<=N; i++)
			perm[i] = i;
		sort(perm+1,perm+N+1,cmp); 
		cout << "Case #" << o << ": ";
		for (int i=1; i<=N; i++){
			cout << perm[i]-1 << ' ';
		}
		cout << endl;
	}

	return 0;
}
