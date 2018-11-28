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
//		cout << "Case #" << z+1 << ": " << count << endl;
	}
}
void scalarproduct()
{
	int size(0);
	cin >> size;
	for(int z=0; z<size; ++z) {
		long long v, t;
		cin >> v;
		vector<long long> up, down;
		for(int i=0; i<v; ++i)
		{
			cin >> t;
			up.push_back(t);
		}
		for(int i=0; i<v; ++i)
		{
			cin >> t;
			down.push_back(t);
		}
		sort(all(up));
		sort(all(down));
		reverse(all(down));
		long long res(0);
		FSZ(i,0,up) {
				res += up[i]*down[i];
		}
		cerr << "Case #" << z+1 << ": " << res << endl;
		cout << "Case #" << z+1 << ": " << res << endl;
	}

}

int main(int argc, char* argv[])
{
	scalarproduct();
//	saveUniverse();
//	train();
//	fly();
	return 0;
}

