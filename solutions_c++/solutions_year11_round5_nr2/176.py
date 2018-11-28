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
#include <cassert>
#include <queue>
using namespace std;

#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define in(x,s) (s.find(x)!=s.end())

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const double eps = 1E-12;
const double pi=acos(-1.0); 


ifstream fin("b.in");
ofstream fout("b.out");

int T;
int N;
int cc[10010];
int main()
{
	
	fin>>T;
	for(int c=1;c<=T;c++)
	{		
		fin>>N;
		int tmp;
		memset(cc,0,sizeof(cc));
		for(int i=0;i<N;i++)
		{
			fin>>tmp;
			cc[tmp]++;
		}
		int res = 100000;
		for(int i=1;i<=10000;i++)
		{
			if(cc[i]==0) continue;
			int j=i;
			int t = cc[i];
			while(cc[j]>=t)
			{
				t = cc[j];
				j++;
				
			}
			//i,i+1,...j-1
			for(int x=i;x<=j-1;x++)
			{
				cc[x]--;
			}
			res = min(res, j-i);
			i--;

		}
		if(res==100000)
			res = 0;

		cout<<"Case #"<<c<<": "<<res<<endl;
		fout<<"Case #"<<c<<": "<<res<<endl;
		
	}
	return 0;
}
