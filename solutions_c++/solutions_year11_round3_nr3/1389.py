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
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define REP(i,n) for(i=0; i<n; i++)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define sz(c) (c).size()

using namespace std;

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;

int gcd(int a, int b)
{
    while(true)
    {
        a=a%b;
		if(!a) return b;
		b=b%a;
        if(!b) return a;
    }
}

int main()
{
	int n,l,h,T,t;
	ifstream in("input.txt");
	ofstream out("output.txt");	
	in>>T;
	REP(t,T)
	{
		in>>n>>l>>h;
		VI v(n);
		for(int i=0; i<n; i++)
			in>>v[i];
		if (l==1)
			out<<"Case #"<<(t+1)<<": "<<1<<endl;
		else
		{
			int r=1;
			bool f=true;
			for(r=l; f&&(r<=h); r++)
			{
				bool g=true;
				for(int i=0; g&&(i<n); i++)
					if ((v[i]%r)&&(r%v[i])) 
						g=false;
				f=!g;
			}
			if (!f) out<<"Case #"<<(t+1)<<": "<<(r-1)<<endl;
			else out<<"Case #"<<(t+1)<<": NO"<<endl;
		}
	}
	return 0;
}

