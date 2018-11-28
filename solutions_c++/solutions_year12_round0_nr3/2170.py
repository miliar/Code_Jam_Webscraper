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
#include <memory.h>
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

int a,b;
int res;
int ar[10];
int Pow[10];
void process(int x)
{
	int xx = x;
	int sz = 0;
	while(xx > 0)
	{
		sz++;
		xx/=10;
	}
	int t;
	int tsz=0;
	for (int i=1;i<sz;i++)
	{
		if (x % Pow[i] < Pow[i-1])
			continue;
		t = x / Pow[i];
		t+= (x % Pow[i]) * Pow[sz-i];
		if (t > x && t <= b)
		{
			//printf("%d %d\n",x,t);
			ar[tsz++] = t;
			//res+=1;
		}
	}
	for (int i=0;i+1<tsz;i++)
	{
		x=i;
		for (int j=i+1;j<tsz;j++)
		{
			if (ar[j] > ar[x])
			{
				x = j;
			}
		}
		swap(ar[x],ar[i]);
	}
	tsz = unique(ar,ar+tsz)-ar;
	res+=tsz;
}
void Solve()
{
	scanf("%d%d",&a,&b);
	res= 0;
	//printf("\n");
	for (int i=a;i<b;i++)
	{
		process(i);
	}
	printf("%d\n",res);
}
int main() 
{
	Pow[0] = 1;
	for (int i=1;i<10;i++)
		Pow[i] = Pow[i-1]*10;
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		printf("Case #%d: ",i+1);
		Solve();
		cerr << "Solved " << i+1 << endl;
	}
	return 0; 
}
