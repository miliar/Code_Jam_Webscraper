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
int a[300],b[300];
char s[300];
int main()
{
	long long sum,put;
	int n,i,T,t,baz,ce,first;
	in=fopen("test.in","r");
	out=fopen("test.out","w");
	fscanf(in,"%d\n",&t);
	FOR(T,1,t)
	{
		baz=ce=0;
		first=1;
		sum=0;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		memset(s,0,sizeof(s));
		fgets(s+1,100,in);
		n=strlen(s+1);
		if (s[n]=='\n')
			n--;
		FOR(i,1,n)
		{
			if (!a[s[i]])
			{
				baz++;
				a[s[i]]=1;
				if (first)
				{
					b[s[i]]=1;
					first=0;
				}
				else
				{
					b[s[i]]=ce;
					if (!ce)
						ce=2;
					else
						ce++;
				}
			}
		}
		put=1;
		if (baz==1)
			baz++;
		for(i=n;i>=1;i--)
		{
			sum+=put*b[s[i]];
			put*=baz;
		}
		fprintf(out,"Case #%d: %lld\n",T,sum);

	}
	fclose(in);
	fclose(out);
        return 0;
}
