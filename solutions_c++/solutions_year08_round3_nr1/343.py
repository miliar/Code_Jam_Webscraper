// gcj2008.cpp : Defines the entry point for the console application.
//

#include <fstream>
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
#include <cmath>
using namespace std;

// 현재의 template
#define sz(v) ((int)(v).size())
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define FSZ(i,a,v) F(i,a,sz(v))
#define all(v) v.begin(),v.end()
string itoa(int i) { stringstream ss; ss<<i; return ss.str(); }
#define same(a,b) (fabs((a)-(b))<0.0000001)
inline int loop(int size, int now, int add) { return (now+add)%size; }
#define two(N) (1<<(N))
#define contain(S,N) (((S)&two(N))!=0)
#define subset(S,X) (((S)&(X))==(X))
// 해당 위치에 비트의 값 체크 (0인지, 1인지)
#define bitpos(X,P) ((X&(1<<(P)))&&(1<<(P)))
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
#define bound(i,j,isize,jsize) (0<=(i)&&(i)<(isize)&&0<=(j)&&(j)<(jsize))

const long double PI = acos(0.0)*2;


void test() {
	int size(0);
	char sz[1024];
	cin >> size;
	cin.getline(sz, 1024);
	for(int z=0; z<size; ++z) {
		int v;
		cin >> v;
		cin.getline(sz, 1024);
		cerr << "Case #" << z+1 << ": " << v << endl;
		cout << "Case #" << z+1 << ": " << v << endl;
	}
}

void text() {
	int size(0);
	cin >> size;
	for(int z=0; z<size; ++z) {
		int P, K, L;
		cin >> P >> K >> L;
		vector<int> keys;
		for(int i=0; i<L; ++i) {
			int v;
			cin >> v;
			keys.push_back(v);
		}
		sort(all(keys));
		reverse(all(keys));
		long long rr(0);
		FSZ(i,0,keys) {
			rr += keys[i]*((i/K)+1);
		}

		cerr << "Case #" << z+1 << ": " << rr << endl;
		cout << "Case #" << z+1 << ": " << rr << endl;
	}
}

// 소수인지 체크한다.
bool isPrime (long long n)
{
	if (n<=0) return false;
	if (n==1) return true;
	if (n==2) return true;
	if (n%2==0) return false;
	long long m=sqrt((long double)n);

	for (long long i=3; i<=m; i+=2)
		if (n%i==0)
			return false;

	return true;
}

string g_str;
long long cnt(0);

void go(int before, int pos, long long v, int type) {
	stringstream ss;
	ss << g_str.substr(before, pos-before);
	long long n;
	ss >> n;
	if(pos == g_str.size()) {
		if(type == 2) n = -n;
		v += n;
//		cerr << v;
		if(!isPrime(v)) ++cnt;
		else;
			// cerr << " fine!!";
//		cerr << endl;
		return;
	}
	go(before, pos+1, v, type);
	if(type == 2) n = -n;
	go(pos, pos+1, v+n, 1);
	go(pos, pos+1, v+n, 2);
}

void ugly() {
	int size(0);
	cin >> size;
	for(int z=0; z<size; ++z) {
		long long n;
		cin >> g_str;
		cnt = 0;
		go(0,1,0,1);
		cerr << "Case #" << z+1 << ": " << cnt << endl;
		cout << "Case #" << z+1 << ": " << cnt << endl;
	}
}

int main(int argc, char* argv[])
{
	text();
//	ugly();
	return 0;
}

