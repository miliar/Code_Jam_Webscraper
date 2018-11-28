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
const int maxn=100000;

int64 n;
int tot,ans,ca;
int prime[maxn];

void init()
{
	tot=1;
	prime[1]=2;
	for (int i=3; i<=1000000; i++)
	{
		bool flag=true;
		int root=(int)sqrt(i);
		for (int j=2; j<=root; j++)
			if (i%j==0)
			{
				flag=false;
				break;
			}
		if (flag) prime[++tot]=i;
	}
}

void solve()
{
	cin>>n;
	if (n==1)
	{
		cout<<0<<endl;
	} else
	{
		ans=0;
		//cout<<endl;
		for (int i=1; i<=tot; i++)
		{
			int tmp=(int)(log(n)/log(prime[i])+eps);
			
			if (tmp>0) tmp--; else break;
			//cout<<tmp<<" ";
			ans+=tmp;
		}
		//cout<<endl;
		cout<<ans+1<<endl;
	}
}

int main()
{
  freopen("C.in","r",stdin);
  freopen("C.out","w",stdout);
	init();
	cin>>ca;
	for (int i=1; i<=ca; i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}

