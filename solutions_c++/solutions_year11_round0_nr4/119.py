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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("ed.in");
ofstream fout("ed.out");

int N;

int main()
{
	fin>>N;
	for(int c=0;c<N;c++)
	{
		int L;
		fin>>L;

		int t;
		int res = 0;
		for(int i=1;i<=L;i++)
		{
			fin>>t;
			if(t!=i)
				res ++;
		}

		
		cout<<"Case #"<<c+1<<": "<<res<<endl;
		fout<<"Case #"<<c+1<<": "<<res<<endl;
	

	
	}
	return 0;
}
