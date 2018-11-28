#include<cstdio>
#include<climits>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<sstream>
#include<cassert>
#include<complex>

#define FOR(a , b , c) for(int a = (int)b; a<=(int)c; a++)
#define FORD(a , b , c) for(int a = (int)b; a>=(int)c; a--)
#define pb push_back
#define mk make_pair
#define sz(v) ((int)(v).size())
#define all(v) v.begin() , v.end()
#define set(x, with) memset(x , with , sizeof(x))
#define same(a,b) (fabs((a)-(b))<0.000000001)
#define even(a) ((a) % 2 == 0)
#define odd(a) ((a) % 2 == 1)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int , int> ii;

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

void init(void);
bool process(void);
void out(int);
int getC(ll, int);
ll setC(ll, int, int);

int ans;
int N;
const int MaxN = 1000;
ii Points[MaxN + 1];
const int MaxY= 30;
ll Cy[MaxN + 1];

int main(void){
	int T;
	cin >> T;
	FOR(i,1, T){
		init();
		for(ans=1; ans<=3; ans++){
			if(process()) break;
		}
		if(N <= 10){
			cerr << "ANs = " << ans << endl;
		}
		out(i);
	}
	return 0;
}

int getC(ll C, int offset){
	int tmp = (C >> ((offset-1) * 2)) & 3;
	if(tmp < 0 || tmp > 3) cerr << "a/sdflkuhaksdfh" << endl;
	return tmp;
}

ll setC(ll C, int offset, int color){
	int tmp = getC(C, offset);
	ll ret = C - (((ll)tmp) << ((offset - 1) * 2)) + (((ll)color) << ((offset - 1) * 2));
	if(ret < 0){
		cerr << C << ' ' << offset << ' ' << color << endl;
		cerr << "Asdflisahdfiuqwfhasd" << endl;
		exit(0);
	}
	return ret;
}

void init(void){
	cin >> N;
	if(N <= 10){
		cerr << "N=" << N << endl;
	}
	FOR(i, 1, N){
		cin >> Points[i].first >> Points[i].second;
		if(N <= 10){
			cerr << Points[i].first << ' ' <<Points[i].second << endl;
		}
	}
	sort(&Points[1] , &Points[N + 1]);
	set(Cy, 0);
	Cy[1] = 0;
	FOR(x, 2, N){
		Cy[x] = Cy[x - 1];
		int y = Points[x - 1].second;
		Cy[x] = setC(Cy[x], y, 3);
		if(y > 1){
			Cy[x] = setC(Cy[x], y - 1, 3);
		}
		if(y < MaxY){
			Cy[x] = setC(Cy[x], y + 1, 3);
		}
	}
}

bool process(void){
	set<ll> possible[2];
	FOR(i, 1, ans){
		possible[1].insert(setC(0, Points[N].second, i) & Cy[N]);
	}
	int from = 1;
	int to = 0;
	FORD(i, N-1, 1){
		int y = Points[i].second;
		set<ll>::iterator it = possible[from].begin();
		while(it != possible[from].end()){
			ll colorset = *it;
			if(colorset < 0){
				cerr << "WTF" << endl;
			}
			FOR(j, 1, ans){
				int tmp = getC(colorset, y);
				if(tmp == j) continue;
				if(y > 1){
					tmp = getC(colorset, y - 1);
					if(tmp == j) continue;
				}
				if(y < MaxY){
					tmp = getC(colorset, y + 1);
					if(tmp == j) continue;
				}
				ll newcolor = setC(colorset, y, j) & Cy[i];
				possible[to].insert(newcolor);
			}
			it++;
		}
		from = to;
		to = !to;
		possible[to].clear();
	}
	return sz(possible[from]) > 0;
}

void out(int C){
	printf("Case #%d: %d\n" , C, ans);
}
