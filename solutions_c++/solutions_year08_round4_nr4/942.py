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

char buf[1024*1024];

int main() {
	freopen("C:\\Projects\\GCJ\\input", "rt", stdin);
	freopen("C:\\Projects\\GCJ\\output.txt", "wt", stdout);

	gets(buf);
	int c = atoi(buf);
	for (int z=0;z<c;z++)
	{
		gets(buf);
		int k = atoi(buf), i;

		gets(buf);
		string str = buf;

		vector<int> vals;
		for (i=0;i<k;i++)
		{
			vals.push_back(i);
		}

		int res=1000000;
		do
		{
			int count = 1;
			string temp = str;
			for (int j=0;j<str.size();j++)
			{
				string rev = "..........................";
				for (int l=0;l<k;l++)
					rev[l] = temp[j+vals[l]];
				for (int p=0;p<k;p++)
				{
					temp[j+p] = rev[p];
				}

				for (int m=j;m<j+k;m++)
				{
					if (m==0)
						continue;
					if (temp[m] != temp[m-1])
						count++;
				}

				if (count > res)
					break;

				j += k-1;
			}

			if (count < res)
				res = count;
		}
		while (next_permutation(vals.begin(), vals.end()));

		cout << "Case #" << (z+1) << ": " << res << endl;
	}

	exit(0);
}
