#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define sz(a) a.size()
#define rep(i,n) for(i=0; i<n; i++)
#define forr(i,a,b) for(i=a; i<=b; i++)
#define ford(i,a,b) for(i=a; i>=b; i--)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define X first
#define Y second
typedef long long ll;
typedef vector<int> VI;

int i,j,k,m, U,N;
char s[100000], t[100000];
string a;
int p[5];

int main()
{
	freopen("d-small.in","r",stdin);//large
	freopen("d-small.out","w",stdout);
	scanf("%d",&N);
	rep(U,N)
	{
		scanf("%d%s",&k,&s);
		a=string(s); m=100000000;
//		printf("%d\n%s\n",k,s);
		rep(i,k) p[i]=i;
		do
		{
			j=0;
			while(j<sz(a))
			{
				rep(i,k) t[j+i]=s[j+p[i]];
				j+=k;
			}
			j=1;
			rep(i,sz(a)-1) if(t[i]!=t[i+1]) j++;
			if(j<m) m=j;
		} while(next_permutation(p,p+k));
		printf("Case #%d: %d\n",U+1,m);
	}
	getchar();
	return 0;
}
