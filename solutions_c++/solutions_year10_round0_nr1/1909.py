#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <cctype>
#include <fstream>
#include <numeric>
#include <map>
#include <iterator>
#include <cstdlib>
#include <cstdio>
using namespace std;

#define INF 99999999
#define EPS 1e-7
#define MIN(a,b) ((a)<(b))?(a):(b)
#define MAX(a,b) ((a)>(b))?(a):(b)
#define REP(i,n) for(i=0; i<(n); i++)
#define FOR(i,a,b) for(i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()


#define SIZE 1000+10

#define IO freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);


int T,N,K;

int main()
{
	IO
	int tc,i;
	scanf("%d",&T);
	for(tc=1;tc<=T;tc++)
	{
		scanf("%d %d",&N,&K);
		int target = (1<<N)-1;
		printf("Case #%d: ",tc);
		printf("%s\n",(K%(target+1) == target)?"ON":"OFF");
	}
	return 0;
}

