#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
using namespace std; 

const int inf = 1000*1000*1000; 
#define CL(x,a) memset(x,a,sizeof(x)); 
#define ALL(v) (v).begin(),(v).end() 
#define PII pair<int,int> 
#define PDI pair<double,int> 
#define MP(a,b) make_pair(a,b) 
#define FOR(i,n) for(int i=0;i<n;i++) 
typedef long long LL; 
typedef vector<int> vi; 
typedef vector< vi > vvi; 
typedef vector< vector<PII > > vvpii; 

int T;
int X,S,R,n;
double t;
int main() 
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int test = 1; test <= T; test++)
	{
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&n);
		map<int,int> mp;
		double free = X;
		FOR(i,n)
		{
			int a,b,w;
			scanf("%d%d%d",&a,&b,&w);
			mp[w]+=b-a;
			free-=b-a;
		}
		mp[0]=free;
		double res = 0;
		for (map<int,int>::iterator it = mp.begin();it != mp.end();it++)
		{
			double w = it->first;
			double free = it->second;
			if ((free+0.0)/(R+w) <= t +1e-10)
			{
				res += (free + 0.0)/(R+w);
				t -= (free+0.0)/(R+w);
			}
			else
			{
				res += t;
				free -= (R+w) * t;
				t = 0;
				res += free/(S+w);
			}
		}
		printf("Case #%d: %.8lf\n",test,res);
	}
	return 0; 
}