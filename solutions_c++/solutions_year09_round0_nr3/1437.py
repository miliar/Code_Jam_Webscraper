#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <string>
#include <functional>
#include <sstream>
#include <fstream>
using namespace std;
#define FOR(i,a,b) for (i=(a);i<=(b);i++)
#define fori(it,v) for (it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(c) c.begin(),c.end()
#define pf push_front
#define popb pop_back
#define popf pop_front
typedef pair<int,int> ii;
FILE *in,*out;
int nr_cifre(int x)
{
	if (!x)
		return 1;
	int nr=0;
	while (x)
	{
		x/=10;
		nr++;
	}
	return nr;
}
char s[700];
int a[550][25];
const char * b=" welcome to code jam";
int main()
{
	int i,j,t,T,n,nr;
	in=fopen("test.in","r");
	out=fopen("test.out","w");
	fscanf(in,"%d\n",&t);
	FOR(T,1,t)
	{
		memset(a,0,sizeof(a));
		memset(s,0,sizeof(s));
		fgets(s+1,600,in);
		n=strlen(s+1);
		if (s[n]=='\n')
			n--;
		FOR(i,0,n)
			a[i][0]=1;
		FOR(i,1,n)
			FOR(j,1,19)
			{
				a[i][j]=a[i-1][j];
				if (b[j]==s[i])
					a[i][j]+=a[i-1][j-1];
				a[i][j]%=10000;
			}
		nr=nr_cifre(a[n][19]);
		fprintf(out,"Case #%d: ",T);
		FOR(i,1,4-nr)
			fprintf(out,"0");
		fprintf(out,"%d\n",a[n][19]);
	}
	fclose(in);
	fclose(out);
        return 0;
}
