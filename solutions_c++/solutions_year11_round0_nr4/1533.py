#line 5 "code.cpp"
#include <string>
#include <vector>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define sqr(x) (x)*(x)
#define For(i,n,m) for(int i=n;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef vector<vector<pair<int,int> > > adjL;
using namespace std;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	cin >>cases;
	rep(a,cases)
	{
		int rslt=0;
		int elements[1100];
		bool taken[1100];
		mem(taken,false);
		int n;
		cin>>n;
		rep(i,n)
			cin>>elements[i+1];
		rep(i,n)
		{
			if(elements[i+1]==i+1)
				taken[i+1]=true;
			else
			{
				if(taken[i+1])
					continue;
				int curIndex=i+1,startValue=elements[i+1],curValue=elements[startValue];
				int cnt=0;
				while(startValue!=curValue)
				{
					cnt++;
					taken[curValue]=true;
					curValue=elements[curValue];
				}
				rslt+=cnt+1;
				taken[curValue]=true;
			}
		}
		printf("Case #%d: %d.000000\n",a+1,rslt);
	}
	return 0;
}