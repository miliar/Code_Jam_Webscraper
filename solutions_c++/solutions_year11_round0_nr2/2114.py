#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>
using namespace std;

#define FRsmall(x,y) freopen(#x"-small-attempt"#y".in","r",stdin);freopen(#x"-small-attempt"#y".out","w",stdout);
#define FRlarge(x) freopen(#x"-large.in","r",stdin);freopen(#x"-large.out","w",stdout);

int c[26][26];
int d[26][26];

int main()
{
	//freopen("B.in","r",stdin);
	//FRsmall(B,0)
	FRlarge(B)

	int T,TC=0,C,D,N,i,j,p,f;
	char q,w,e;
	char s[110];
	int t[110];
	scanf("%d",&T);
	while(++TC<=T)
	{
		printf("Case #%d: ",TC);
		scanf("%d",&C);
		memset(c,-1,sizeof(c));
		for(i=0;i<C;i++)
		{
			scanf(" %c%c%c",&q,&w,&e);
			c[q-'A'][w-'A']=c[w-'A'][q-'A']=e-'A';
		}
		scanf("%d",&C);
		memset(d,0,sizeof(d));
		for(i=0;i<C;i++)
		{
			scanf(" %c%c",&q,&w);
			d[q-'A'][w-'A']=d[w-'A'][q-'A']=1;
		}
		p=0;
		scanf("%d %s",&N,s);
		for(i=0;i<N;i++)
		{
			t[p++]=s[i]-'A';
			if(p>=2 && ~c[t[p-2]][t[p-1]])
			{
				t[p-2]=c[t[p-2]][t[p-1]];
				p--;
			}
			for(j=0;j<p;j++)if(d[t[p-1]][t[j]])p=0;
		}
		putchar('[');
		f=0;
		for(i=0;i<p;i++)
		{
			if(f)printf(", ");else f=1;
			putchar('A'+t[i]);
		}
		putchar(']');
		putchar('\n');
	}
	return 0;
}
