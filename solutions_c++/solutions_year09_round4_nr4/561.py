#include <algorithm> 
#include <iostream> 
#include <sstream> 
#include <cstring> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <string> 
#include <cmath> 
#include <queue> 
#include <map> 
#include <stack>
#include <set> 

using namespace std; 

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long ll; 

#define sz size() 
#define pb push_back 
#define MAX 0x3FFFFFFF 
#define all(x) (x).begin(),(x).end() 
#define For(i,n) for(int i=0, _n=(n);i<_n;++i) 
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i) 

int a[100][3];
int b[100];

double calc(int x, int y)
{
	double dis = sqrt((double)(a[x][0]-a[y][0])*(a[x][0]-a[y][0])+(a[x][1]-a[y][1])*(a[x][1]-a[y][1]));
	dis += a[x][2] + a[y][2];
	return dis/2;
}

int main()
{
	freopen("D-small-attempt4.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int tn;
	int ti=0;
	scanf("%d",&tn);
	while(tn--)
	{
		int n;
		scanf("%d",&n);
		For(i,n) scanf("%d %d %d",&a[i][0],&a[i][1],&a[i][2]);
		if(n == 1)
		{
			printf("Case #%d: %.9lf\n", ++ti,(double)a[0][2]);
			continue;
		}
		if(n == 2)
		{
			printf("Case #%d: %.9lf\n", ++ti,(double)max(a[0][2],a[1][2]));
			continue;
		}
		double r1 = max(calc(0,1),(double)a[2][2]);
		double r2 = max(calc(0,2),(double)a[1][2]);
		double r3 = max(calc(1,2),(double)a[0][2]);
		if(r1>r2) r1 = r2;
		if(r1>r3) r1 = r3;
		printf("Case #%d: %.9lf\n", ++ti,r1);
	}
}
/*
5
3
20 10 2
20 20 2
40 10 3
3
20 10 3
30 10 3
40 10 3

*/