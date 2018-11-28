#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef vector<ld> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;


void solve_case(int TN)
{
	vvi Co(26, vi(26, -1));
	vvi Op(26, vi(26, -1));
	int N;
	string s;
	fin >> N;
	FOR(i, N)
	{
		fin >> s;
		Co[s[0]-'A'][s[1]-'A'] = s[2]-'A';
		Co[s[1]-'A'][s[0]-'A'] = s[2]-'A';
	}
	fin >> N;
	FOR(i, N)
	{
		fin >> s;
		Op[s[0]-'A'][s[1]-'A'] = 1;
		Op[s[1]-'A'][s[0]-'A'] = 1;
	}

	vi L;
	fin >> N >> s;
	FOR(i, N)
	{
		if (L.empty())
		{
			L.push_back(s[i]-'A');
			continue;
		}
		if (Co[L.back()][s[i]-'A'] != -1)
		{
			int b = L.back();
			L.pop_back();
			L.push_back(Co[b][s[i]-'A']);
			continue;
		}
		bool opposed = false;
		FOR(j, SZ(L)) 
			if (Op[L[j]][s[i]-'A'] == 1)
			{
				opposed = true;
				break;
			}
		if (opposed)
		{
			L.clear();
			continue;
		}
		L.push_back(s[i]-'A');
	}

	fout << "Case #" << TN << ": [";
	cout << "Case #" << TN << ": [";
	FOR(i, SZ(L))
	{
		fout << (char)(L[i]+'A');
		cout << (char)(L[i]+'A');
		if (i < SZ(L)-1)
		{
			fout << ", ";
			cout << ", ";
		}
	}
	fout << "]\n";
	cout << "]\n";
}

int main()
{
	fin.open("B.in"); 
	fout.open("B.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
