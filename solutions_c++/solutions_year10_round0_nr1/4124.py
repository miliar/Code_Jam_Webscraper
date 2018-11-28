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
#include <fstream>

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

bool fact(int N, int K)
{
	if (K==0 || N==0)
		return false;


	int fact = 1;
	for (int ii= 1; ii<=N; ii++)
		fact = 2 * fact;

	K = K +1;

	if ( K%fact == 0 )
		return true;
	
	return false;
}

int main() 
{
	string line;
	ifstream myfile ("C:\\Users\\nous\\Documents\\Benoit\\Developpement\\code jam\\Round1-pb1\\test\\debug\\A-large.in");
	ofstream outfile ("C:\\Users\\nous\\Documents\\Benoit\\Developpement\\code jam\\Round1-pb1\\test\\debug\\A-large.out");
	
	ostringstream out;

	if (myfile.is_open())
	{
		getline (myfile,line);
		istringstream iss(line);
		int numLines;
		iss >> numLines;
		
		for (int ii=0; ii<numLines; ii++)
		{
			getline (myfile,line);
			istringstream iss2(line);
			int N, K;
			iss2 >> N >> K;

			out << "Case #" << ii+1 << ": ";
			if (fact(N, K))
				out << "ON" << "\n";
			else
				out << "OFF" << "\n";	
		}
		outfile << out.str();
		outfile.close();
		myfile.close();
	}
	else cout << "Unable to open file"; 
}

