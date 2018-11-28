#include<algorithm>
#include<cassert>
#include<cmath>
#include<iomanip>
#include<iostream>
#include<iterator>
#include<limits>
#include<list>
#include<map>
#include<numeric>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<utility>
#include<vector>
using namespace std;

typedef unsigned long ulong;
typedef unsigned int uint;

#define REP2(var,start,limit) for(int var=(start);var<(limit);++var)
#define REP(i,n) REP2(i,0,n)
#define ITER(x,it) for(typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define RANGE(x) (x).begin(),(x).end()
template<typename T> int SZ(const T& c) { return (int)c.size(); }
template<typename T> T infinity() { return numeric_limits<T>::max(); }

int main()
{
	int N;
	cin >> N;
	for(int c=0;c<N;++c)
	{
        long R, k, N;
        long g[1000];
        cin >> R >> k >> N;
        for(int i=0;i<N;++i) cin >> g[i];
        long euros=0;
        int i=0;
        for(;R>0;R--)
        {
            int cride=0;
            int igroups=0;
            while(cride+g[i] <= k && igroups < N)
            {
                //clog << "ride " << R << " group " << i << endl; 
                cride += g[i];
                igroups++;
                i = (i+1) % N;
            }
            euros += cride;
        }
		cout << "Case #" << c+1 << ": " << euros << endl;
	}
}
