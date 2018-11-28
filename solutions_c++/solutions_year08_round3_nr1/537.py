#include <time.h>
#include <fstream>
#include <iostream>
#include <sstream>
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
const double pi = 2*acos(0.0);
const double eps = 1e-9;

#define in64 long long 


int main()
{
	ifstream file("C:\\Benoit\\code jam\\Round1-pb1\\A-small.in");
	ofstream fileOut("C:\\Benoit\\code jam\\Round1-pb1\\A-small.out");

	string line;
	int64 N, P, K, L;



	file >> N;
	
	for (int64 ii = 1 ; ii <= N; ii++)
	{
			file >> P;
			file >> K;
			file >> L;
			vector<int64> alpha; // should be L length;
			for (int64 jj = 1; jj <= L; jj++)
			{
				int64 proba;
				file >> proba;
				alpha.push_back(proba);
			}
			
			sort(alpha.begin(), alpha.end());
			vector<int64>::iterator it = alpha.end();
			int64 size = alpha.size();
			vector<int64> ref;
			int64 res = 0;		
			for (int64 kk = 1; kk <= K; kk++)
			{
				ref.push_back(1);
			}
			
			vector<int64>::iterator it2 = ref.begin();
			bool block = false;
			for (int64 zz = size -1; zz >= 0; zz--)
			{
				bool bFound = false;
				while (bFound == false)
				{
					if (*it2 <= P)
					{
						res = res + ((*it2) * alpha.at(zz));
						*it2 = *it2 + 1;
						bFound = true;
					}
					it2++;
					if (it2 == ref.end()) it2 = ref.begin();
				}				
			}
			
			fileOut << "Case #" << ii << ": " << res << "\n";	
	}
	file.close();
	fileOut.close();
  return 0;
}