// Marcin Wrochna
// g++ -O2
// IDE: geany
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PI;
#define MP make_pair
#define REP(x,n) for(int x=0; x<(int)(n); ++x)
#define REB(b,x,n) for(int x=b; x<(int)(n); ++x)
#define REPD(x,n) for(int x=(n)-1; x>=0; --x)
#define PB push_back
#define XX first
#define YY second
const int INF = 1000000001;
const double EPS = 10e-9;

void doit() {
	char num[22];
	scanf("%s\n",num+1);
	num[0]='0';
	int n=strlen(num);
	for(int i=1; i<n; i++)
	{
		int minv=INF,minp=n-i;
		for(int j=n-i; j<n; j++)
		{
			if(num[n-i-1]<num[j] && num[j]<minv)
			{
				minv=num[j];
				minp=j;
			}
		}
		if(num[n-i-1]<num[minp])
		{
			swap(num[n-i-1],num[minp]);
			sort(num+n-i,num+n);
			if(num[0]=='0') printf("%s\n", num+1);
			else printf("%s\n", num);
			return;
		}
		//printf("%d\n", i);
	}
	exit(1);
}

int main()
{
	int NCase;
	scanf("%d\n",&NCase);
	REP(ncase,NCase) {
		printf("Case #%d: ", ncase+1);
		doit();
	}

	return 0;
}
