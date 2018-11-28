#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

typedef vector<int> vi;
typedef vector<ll> vll;
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
#define Sort(a) sort(All(a))
#define Eo(x) { cerr << #x << " = " << (x) << endl; } 
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }


#define MAX 101
int data[MAX][MAX];
int data2[MAX][MAX];
int calc()
{
    int res=0;
    Rep(i,MAX)
        Rep(j,MAX)
    {
        res=max(res,data[i][j]);
    }
    return res;
}
void solve(int test)
{
    Fill(data,0);
    int R;
    cin>>R;
    Rep(i,R)
    {
        int x1,x2,y1,y2;
        cin>>x1>>y1>>x2>>y2;
        For(i,x1,x2)
            For(j,y1,y2)
            data[i][j]=1;
    }
    int res=0;
    while(calc()!=0)
    {
        memcpy(data2,data,sizeof(data));
    Rep(i,MAX)
        Rep(j,MAX)
    {
        if(data[i][j]==1)
        {
        if((data[i-1][j]==0)&&(data[i][j-1]==0))
            data2[i][j]=0;
        }
        if(data[i][j]==0)
        {
            if((data[i-1][j]>0)&&(data[i][j-1]>0))
                data2[i][j]=1;
        }

    }
    memcpy(data,data2,sizeof(data));
    res++;
    }
   

	cout<<"Case #"<<test<<": "<<res<<endl;
}


int main() {
	freopen("a.in", "rt", stdin);
	freopen("output2.txt", "wt", stdout);
	int N;
	cin>>N;
	char buf[90];
	gets(buf);
	For(test,1,N)
	{
		solve(test);	
	}
}