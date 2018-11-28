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

int n,m;
char ar[10][10];
const int dx[8]={1,0,-1,0,1,1,-1,-1};
const int dy[8]={0,-1,0,1,1,-1,-1,1};
const int q[4][2] = {{1,3},{0,2},{5,7},{4,6}};
void Solve()
{
	scanf("%d%d",&n,&m);
	FOR(i,n)
		scanf("%s",ar[i]);
	FOR(i,n)
	{
		FOR(j,m)
		{
			if (ar[i][j] == '-')
				ar[i][j] = 0;
			if (ar[i][j] == '|')
				ar[i][j] = 1;
			if (ar[i][j] == '/')
				ar[i][j] = 2;
			if (ar[i][j] == '\\')
				ar[i][j] = 3;
		}
	}
	char w[5][5];
	int res=0;
	for (int z=0;z<(1<<(n*m));z++)
	{
		CL(w,0); bool ok = 1;
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<m;j++)
			{
				int nx = i + dx[q[ar[i][j]][(z&(1<<(m*i+j))) != 0]];
				int ny = j + dy[q[ar[i][j]][(z&(1<<(m*i+j))) != 0]];
				nx = (nx + n)%n;
				ny = (ny + m)%m;
				if (w[nx][ny] == 0)
					w[nx][ny] = 1;
				else
				{
					ok = 0;
					break;
				}
			}
			if (!ok)
				break;
		}
		res+=ok;
	}
	printf("%d",res);
}
int main() 
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		Solve();
		printf("\n");
	}
	return 0; 
}