#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
	freopen("a.in","r",stdin);
	freopen("fix(out).txt","w",stdout);
	int j,k,b;
	int t,n,m,res;
	string buf,ck;
	char c[10000];
	scanf("%d",&t);
	set <string> s;
	for(int g=1; g<=t; g++)
	{
		res = 0;
		s.clear();
		scanf("%d%d",&n,&m);
		for(j=0; j<n; j++)
		{
			scanf("%s",c);
			buf = string(c);
			for(k=1; k<buf.size(); k++)
			{
				if(buf[k] == '/' || (k+1) == buf.size())
				{
					b = (k+1) == buf.size() ? 1 : 0;
					s.insert(buf.substr(0,k+b));
				}
			}
		}
		for(j=0; j<m; j++)
		{
			scanf("%s",c);
			buf = string(c);
			for(k=1; k<buf.size(); k++)
			{
				if(buf[k] == '/' || (k+1) == buf.size())
				{
					b = (k+1) == buf.size() ? 1 : 0;
					ck = buf.substr(0,k+b);
					if(s.find(ck)==s.end()) res++;
					s.insert(ck);
				}
			}
		}
		printf("Case #%d: %d\n",g,res);
	}
	return 0;
}