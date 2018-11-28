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
		int T;
		fin>>T;
		char ch;
		int np;

		int p1=1;
		int p2=1;
		int t1=0;
		int t2=0;
		int ct = max(t1,t2);
		for(int i=0;i<T;i++)
		{
			fin>>ch>>np;

			ct = max(t1,t2);
			if(ch=='O')
			{
				int cost = abs(np-p1) + 1;

				t1 += cost;
				if(t1<=ct)
					t1 = ct+1;
				p1 = np;
			}
			else
			{
				int cost = abs(np-p2) + 1;
				t2 += cost;
				if(t2<=ct)
					t2 = ct+1;
				p2 = np;
			}
		}		
		int res = max(t1,t2);
		

		cout<<"Case #"<<c+1<<": "<<res<<endl;
		fout<<"Case #"<<c+1<<": "<<res<<endl;

	
	}
	return 0;
}
