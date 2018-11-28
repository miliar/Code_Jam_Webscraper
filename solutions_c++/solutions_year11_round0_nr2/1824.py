#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>
#include <assert.h>
using namespace std;

#define forn(i,n) for(int i=1;i<=n;i++)
char c[5],v[5],m[105];
char ans[105];
int va[26][26];
char ch[26][26];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,C,D,N;
	scanf("%d",&t);
	forn(tcase,t)
	{
		memset(ch,0,sizeof(ch));
		memset(va,0,sizeof(va));
		scanf("%d",&C);
		while(C--)
		{
			scanf("%s",c);
			ch[c[0]-'A'][c[1]-'A']=ch[c[1]-'A'][c[0]-'A']=c[2];
		}
		scanf("%d",&D);
		while(D--)
		{
			scanf("%s",v);
			va[v[0]-'A'][v[1]-'A']=va[v[1]-'A'][v[0]-'A']=1;
		}
		scanf("%d%s",&N,m);
		int k=1;
		for(int i=0;i<N;i++)
		{
			ans[k]=m[i];
			if(k<2) { k++;continue;}
			if(ch[ans[k-1]-'A'][ans[k]-'A'])
			{
				ans[k-1]=ch[ans[k-1]-'A'][ans[k]-'A'];
				k--;
			}
			else
				for(int j=0;j<k;j++)
					if(va[ans[k]-'A'][ans[j]-'A']) { k=0;break;}
			k++;
		}
		printf("Case #%d: [",tcase);
		if(k!=1)
			printf("%c",ans[1]);
		for(int i=2;i<k;i++)
			printf(", %c",ans[i]);
		printf("]\n");
	}
	return 0;
}