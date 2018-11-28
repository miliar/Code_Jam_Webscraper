#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

const double PI = 3.14159265;
const double EPSILON = 1e-9;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define EQ(x, y) (abs((x)-(y)) < EPSILON)
#define ISPOS(x) ((x) > EPSILON)
#define ISNEG(x) ((x) < -EPSILON)
#define ISZERO(x) (abs(x) <= EPSILON)

typedef long long int LLI;

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }


double asin2(double x) {
	double res = asin(max(-1.0, min(1.0, x)));
	assert(-PI/2 <= res && res <= PI/2);
	return res;
}
vector<int> keys;
int main()
{
	int N;
	cin >> N;
	int P, K, L;
	int key;
	Rep(i, N)
	{
		cin >> P >> K >> L;
		keys.clear();
		Rep(j, L)
		{
			cin >> key;
			keys.push_back(key);
		}
		sort(keys.begin(), keys.end());
		//for(int j = 0; j < L; j++)
		//{
			//cout << keys[j] << "  " ;
		//}
		//cout << endl;
		int cost = 1;
		LLI sum = 0;
		for(int j = 0; j < L; j++)
		{
			if(j%K == 0 && j != 0) cost++;
			//cout << cost << " ";
			sum += keys[L- 1-j]*cost; 
		}
		cout << "Case #" << i + 1 << ": " << sum << endl;
	}
	return 0;
}
