#include <stdio.h>
#include <string>
#include <map>
#include <set>

using namespace std;

char s[1000];

int main()
{
	int n,m,i,q,j;
	map<string,int> x;
	set<int> y;
	gets(s);
	sscanf(s,"%d",&n);
	for (j=1;j<=n;++j)
	{
		q=0;
		gets(s);
		sscanf(s,"%d",&m);
		x.clear();
		for (i=0;i<m;++i)
		{
			gets(s);
			x[(string)s]=i;
		}
		gets(s);
		sscanf(s,"%d",&m);
//		printf(">> %s %d\n",s,m);
		y.clear();
		for (i=0;i<m;++i)
		{
			gets(s);
			map<string,int>::iterator z = x.find((string)s);
			if (z!=x.end())
			{
//				printf("HERE %d\n",z->second);
				y.insert(z->second);
				if (y.size()==x.size())
				{
					y.clear();
					y.insert(z->second);
					++q;
				}
			}
		}
		printf("Case #%d: %d\n",j,q);
	}
}
