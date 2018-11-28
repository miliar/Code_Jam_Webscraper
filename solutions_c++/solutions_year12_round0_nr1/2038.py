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
char alp[4][100] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv",
"yeq"};
char alp_to[4][100] = {"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up",
"aoz"};
map<char,char> mp;
vector<char> v;
char buf[10000];
int main() 
{ 
	FOR(i,4)
	{
		int L = strlen(alp[i]);
		FOR(j,L)
		{
			if (alp[i][j] >='a' && alp[i][j] <='z')
			{
				mp[alp[i][j]] = alp_to[i][j];
				v.push_back(alp_to[i][j]);
			}
		}
	}
	mp['z'] = 'q';
	sort(ALL(v));
	v.resize(unique(ALL(v)) - v.begin());
	//mp['q'] = 'z';
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int n;
	scanf("%d",&n);
	gets(buf);
	FOR(i,n)
	{
		gets(buf);
		FOR(j,strlen(buf))
		{
			if (buf[j] >= 'a' && buf[j] <= 'z')
				buf[j] = mp[buf[j]];
		}
		printf("Case #%d: ",i+1);
		puts(buf);
	}
	return 0; 
}
