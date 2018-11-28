#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define MP make_pair
#define PB push_back
#define two(X) (1<<(X))
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)A.length())
#define random(x) (rand()%x)
#define randomize() (srand((int)time(0)))

typedef long long int64;
typedef vector<int> VI;
typedef vector<string> VS;

const int INF=0x7FFFFFFF;
const double eps=1e-8;
const double pi=acos(-1.0);
const int maxn=501;

class data
{
	public:
		int64 x,y;

	data operator +(const data &b)
	{
		data ret;
		ret.x=x+b.x;
		ret.y=y+b.y;
		return ret;
	}

	data operator -(const data &b)
	{
		data ret;
		ret.x=x-b.x;
		ret.y=y-b.y;
		return ret;
	}
};

int n,m,ca,p,ans;
int a[maxn][maxn];
int64 d[maxn][maxn];
data b[maxn][maxn],c[maxn][maxn],s[maxn][maxn];


bool check(int ans)
{
	data L,R,tmp;
	int64 t;
	for (int i=1; i<=n-ans+1; i++)
		for (int j=1; j<=m-ans+1; j++)
		{
			int x=i+ans-1, y=j+ans-1;
			L=s[x][y]-s[i-1][y]-s[x][j-1]+s[i-1][j-1];
			L=L-c[i][j]-c[i][y]-c[x][j]-c[x][y];
			//cout<<L.x<<" "<<L.y<<endl;
			tmp.x=i+x-1; tmp.y=j+y-1;
			t=d[x][y]-d[i-1][y]-d[x][j-1]+d[i-1][j-1];
			t=t-a[i][j]-a[i][y]-a[x][j]-a[x][y];
			R.x=tmp.x*t; R.y=tmp.y*t;
			if (L.x==R.x && L.y==R.y) return true;
		}
	return false;
}

void init()
{
    cin>>n>>m>>p;
    string st;
    for (int i=1; i<=n; i++)
    {
        cin>>st;
        for (int j=1; j<=m; j++)
        {
            a[i][j]=st[j-1]-'0'+p;
            b[i][j].x=i+i-1; b[i][j].y=j+j-1;
            c[i][j].x=b[i][j].x*a[i][j];
            c[i][j].y=b[i][j].y*a[i][j];
            s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+c[i][j];
            int64 tmp=d[i-1][j];
            tmp=tmp+d[i][j-1]-d[i-1][j-1]+a[i][j];
            d[i][j]=tmp;
        }
    }
}

int main()
{
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
	cin>>ca;
	for (int CA=1; CA<=ca; CA++)
	{
		cout<<"Case #"<<CA<<": ";
		init();
		if (n<m) ans=n; else ans=m;
		for (; ans>=2; ans--)
		{
			if (ans<3)
			{
				cout<<"IMPOSSIBLE"<<endl;
				break;
			}
			if (check(ans))
			{
				cout<<ans<<endl;
				break;
			}
		}
	}
}

