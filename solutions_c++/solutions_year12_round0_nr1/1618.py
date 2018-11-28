#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#define MAXN 30
#define PB push_back
#define MP make_pair
#define ST first
#define ND second

#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(a,b,c) for(int a=b;a<=(c);a++)
#define FORD(a,b,c) for (int a=b;a>=(c);a--)
#define VAR(v,n) __typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();i++)

using namespace std;

typedef long long LL;  

string s;
int t,dl;
char zmiana[MAXN] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'}; 

int main()
{
	scanf("%d ",&t);
	FOR(j,1,t)
	{
		getline(cin,s);
		int dl =  s.length();
		//printf("%d\n",dl);
		printf("Case #%d: ",j);
		REP(i,dl) if (s[i] >= 'a' && s[i] <= 'z') 
			printf("%c",zmiana[int(s[i]-'a')]);
				else printf(" ");
		puts("");
	}
	return 0;
}
