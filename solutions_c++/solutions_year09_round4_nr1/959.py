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
#include <list>

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
	int N;
	scanf("%d",&N);
	list<int> a;
	REP(i,N)
	{
		int b=0;
		char str[42];
		scanf(" %s", str);
		REP(j,N) if(str[j]=='1') b=j;
		a.PB(b);
	}
	int result=0;
	REP(i,N)
	{
		int j=0;
		for(list<int>::iterator it=a.begin(); it!=a.end(); it++)
		{
			if((*it)<=i)
			{
				result+=j;
				a.erase(it);
				break;
			}
			j++;
		}
	}
	printf("%d\n", result);
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
