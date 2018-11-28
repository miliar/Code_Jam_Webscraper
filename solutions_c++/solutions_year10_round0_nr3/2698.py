// google_B_Qualification.cpp : 定义控制台应用程序的入口点。
//

// BEGIN CUT HERE

// END CUT HERE
#include <stdafx.h>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <bitset>



using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double eps = 1e-9;

inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int I, J;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

int N;
long long K;
long long R;
int T;


long long arr[1001];
long long aa[1001];

//#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif

	int c=0;
	int oldc[1000];
	memset(oldc,0,sizeof(oldc));
	bool f = false;
	long long count = 0;
	long long sum = 0;
	cin>>T;
	for(int i = 0 ;i<T;i++){
		cin>>R>>K>>N;
		for(int j = 0;j<N;j++){
			cin>>arr[j];
		}
		count = 0;
		c = 0;
		memset(oldc,0,sizeof(oldc));
		memset(aa,0,sizeof(aa));
		f = false;
		for(long long x = 0;x < R;x++){
			sum = 0;
			if(oldc[c] && !f){
				count = aa[oldc[c]-1] + (count - aa[oldc[c]-1])*((R-oldc[c]+1)/(x-oldc[c]+1));
				x =(x-oldc[c]+1)*((R-oldc[c]+1)/(x-oldc[c]+1)) + oldc[c]-2;
				f = true;
			}
			else
			{
				oldc[c] = x+1;
				for(int y = 0;y < N;y++){
					if(sum + arr[c] <= K){
						sum += arr[c];
						c = (c+1)%N;
					}
					else{
						break;
					}
				}
				if(!f)
					aa[x%N] = count;
				count += sum;
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}


