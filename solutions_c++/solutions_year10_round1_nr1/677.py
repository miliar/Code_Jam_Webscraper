#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <cmath>
#include <map>
using namespace std;
#define VT vector
typedef VT<int> VI;
typedef VT<VI> VVI;
typedef VT<string> VS;
typedef VT<double> VD;
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define ALL(c) c.begin(),c.end()
#define PB push_back
#define MP make_pair
#define FS first
#define SC second
#define SZ size() 

bool check_color(VS& field, char ch, int K)
{
	int N = field.size();

	bool check = false;

	for(int i =0; i < N-K+1; ++i)
	{
		for(int j =0; j < N-K+1; ++j)
		{
			bool all = true;
			for(int k = 0; k < K; ++k)
			{
				if (field[i+k][j+k] != ch)
				{
					all=false;
					break;
				}
			}
			if (all)return true;
		}
	}

	for(int i =0; i < N-K+1; ++i)
	{
		for(int j =0; j < N; ++j)
		{
			bool all = true;
			for(int k = 0; k < K; ++k)
			{
				if (field[i+k][j] != ch)
				{
					all=false;
					break;
				}
			}
			if (all) return true;
		}
	}

	for(int i =0; i < N; ++i)
	{
		for(int j =0; j < N-K+1; ++j)
		{
			bool all = true;
			for(int k = 0; k < K; ++k)
			{
				if (field[i][j+k] != ch)
				{
					all=false;
					break;
				}
			}
			if (all)
				return true;
		}
	}




	for(int i = N-1; i >= K-1; --i)
	{
		for(int j =0; j < N-K+1; ++j)
		{
			bool all = true;
			for(int k = 0; k < K; ++k)
			{
				if (field[i-k][j+k] != ch)
				{
					all=false;
					break;
				}
			}

			if (all)
				return true;
		}
	}


	return false;
}

int main(int argc, char* argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		int N, K;
		cin >>N>>K;
		VS field;

		for(int n=0;n<N;++n)
		{
			string s;
			cin >> s;

			string str(N, '.');
			int si = N-1;
			for(int j = N-1; j >= 0; --j)
			{
				if (s[j] != '.')
				{
					str[si] = s[j];
					si--;
				}
			}

			field.push_back(str);
		}

		bool red = check_color(field, 'R', K);
		bool blue = check_color(field, 'B', K);

		string res = "Neither";
		if (red && blue)
			res = "Both";
		else if (red)
			res = "Red";
		else if (blue)
			res = "Blue";

		cout << "Case #" << t << ": " << res << "\n";


	}

	int Int;
	std::cin >> Int;
}
// END CUT HERE
