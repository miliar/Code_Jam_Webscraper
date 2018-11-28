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
#define MOD 10007
#define BIT(x) (1<<(x))

using namespace std;

int pascal[105][105];

int get_move(int w,int h)
{
    if(w<0 || h<0) return 0;
    int A,B;
    A = 2*w - h;
    B = 2*h - w;
    if(A % 3 != 0 || B % 3 != 0 ) return 0;
    A/=3;
    B/=3;
    if(A<0 || B<0) return 0;
    return pascal[A+B][A];
}

void process(int tcase)
{
    int w,h,r;
    int A,B;
    vector<pair<int,int> > V;
    cin >> w >> h >> r;

    w--;h--;

    int ret=0;
    V.resize(r);

    for(int i=0;i<r;i++)
    {
	cin >> V[i].first >> V[i].second;
	V[i].first--;
	V[i].second--;
    }

    sort(V.begin(),V.end());

    for(int i=0;i<BIT(r);i++)
    {
	int curx=0,cury=0;
	int xxx = 1;
	int flag = 1;
	for(int j=0;j<r;j++) if(i & (1<<j))
	{
	    flag *= -1;
	    xxx = (xxx * get_move(V[j].first - curx,V[j].second - cury)) % MOD;
	    curx = V[j].first;
	    cury = V[j].second;
	}
	xxx = (xxx * get_move(w - curx, h - cury)) % MOD;
	ret = (ret + xxx * flag) % MOD;
    }

    ret = (ret + MOD) % MOD;
    cout << "Case #" << tcase << ": " << ret << endl;
}

int main(void)
{
    for(int i=0;i<=100;i++)
    {
	pascal[i][0] = pascal[i][i] = 1;
	for(int j=1;j<i;j++)
	    pascal[i][j] = (pascal[i-1][j-1] + pascal[i-1][j]) % MOD;
    }
    int T;
    cin >> T;
    for(int t=1;t<=T;t++)
    {
        process(t);
    }
}
