#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <set>
#include <numeric>
#include <iterator>
#include <sstream>
#include <list>

#define pb push_back
#define mp make_pair
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)

template<typename T> inline bool setmin(T &a, T b) { if(a>=b) { a=b; return true; } return false; }
template<typename T> inline bool setmax(T &a, T b) { if(a<=b) { a=b; return true; } return false; }

using namespace std;

void process(int tcase)
{
    int N,M,TGT;
    int a,b,c;
    cin >> N >> M >> TGT;

    cerr << tcase << endl;

    if(N * M < TGT)
    {
	cout << "Case #" << tcase << ": IMPOSSIBLE" << endl;
	return;
    }

    for(a=0;a<=M;a++)
    {
	for(b=0;b<=N;b++)
	{
	    if(a == 0 && b == 0) continue;
	    c =  a*b + TGT;

	    if(a == 0)
	    {
		if(c % b == 0)
		{
		    int y = c/b;
		    if(y <= M)
		    {
			cout << "Case #" << tcase << ": 0 " << a << " " << b << " 0 0 " << y << endl;
			return;
		    }
		}
		continue;
	    }

	    if(b == 0)
	    {
		if(c % a == 0)
		{
		    int x = c/a;
		    if(x <= N)
		    {
			cout << "Case #" << tcase << ": 0 " << a << " " << b << " 0 " << x << " 0" << endl;
			return;
		    }
		}
		continue;
	    }

	    int cc = c % b , aa = a % b;
	    int x,step,y;

	    if(cc == 0)
	    {
		x = 0;
	    }
	    else
	    {
		if(aa == 0)
		    continue;
		int gg = __gcd(aa,cc);
		int ac = cc*aa/gg;
		x = ac / aa;
	    }

	    if(aa == 0)
		step = 1;
	    else
	    {
		int gg = __gcd(aa,b);
		int bc = aa*b/gg;
		step = bc / aa;
	    }

	    int leastx = (c - M*b + (a-1)) / a;
	    if(leastx < x) leastx=x;
	    int diffx = leastx - x;
	    diffx = (diffx + step - 1)/step*step;

	    int xx = x + diffx;
	    if(xx > N) continue;
	    y = (c - a*xx) / b;
	    if(y < 0 || y > M) continue;
	    cout << "Case #" << tcase << ": 0 " << a << " " << b << " 0 " << xx << " " << y << endl;
	    return;
	}
    }


    long long ret=0;
    cout << "Case #" << tcase << ": IMPOSSIBLE" << endl;
}

int main(void)
{
    int T;
    cin >> T;
    for(int t=1;t<=T;t++)
    {
        process(t);
    }
}
