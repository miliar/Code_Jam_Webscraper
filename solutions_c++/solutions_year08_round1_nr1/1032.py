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
#include <fstream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

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

int main() 
{
	ifstream in("A-small-attempt2.in");
	ofstream out("output.txt");

	int t;
	in>>t;
	For(test, 1, t) {
		int len;
		int result = 0;
		in>>len;
		vector<int> v1;
		vector<int> v2;
		for(int i = 0; i < len; i++ )
		{
			int val; 
			in>>val;
			v1.push_back(val);
		}
		for(int i = 0; i < len; i++ )
		{
			int val; 
			in>>val;
			v2.push_back(val);
		}
		sort(v1.begin(),v1.end() );
		sort(v2.begin(),v2.end(),greater<int>() );
		for(int i = 0; i < len; i++ )
		{
			result += v1[i]*v2[i];
		}
		sort(v1.begin(),v1.end(),greater<int>() );
		sort(v2.begin(),v2.end() );
		int temp = 0;
		for(int i = 0; i < len; i++ )
		{
			temp += v1[i]*v2[i];
		}
		if( temp < result ) 
			result = temp;
		printf("Case #%d: %d\n", test, result);
		out<<"Case #"<<test<<": "<<result<<endl;
	}

	exit(0);
}