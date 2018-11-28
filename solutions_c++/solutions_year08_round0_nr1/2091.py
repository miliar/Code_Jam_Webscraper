#include<stdio.h>
#include<string>
#include<map>
using namespace std;
int main()
{
	int t,k;
	int s,q;
	int cnt;
	char qy[101];
	scanf("%d",&t);
	for (k=1;k<=t;++k)
	{
		map<string,bool> m;
		scanf("%d",&s);
		getchar();
		for (int i=0;i<s;++i)
		{
			gets(qy);
			m[qy]=false;
		}
		scanf("%d",&q);
		getchar();
		cnt=0;
		int used=0;
		for (int i=0;i<q;++i)
		{
			gets(qy);
			string tmp(qy);
			if (!m[tmp]) { m[tmp]=true; ++used; }
			if (used==s) {
				used=1;
				++cnt;
				for (map<string,bool>::iterator it=m.begin();
					it!=m.end();++it)
				{
					if (it->first==tmp) continue;
					it->second=false;
				}
			}
		}
		printf("Case #%d: %d\n",k,cnt);
	}
	return 0;
}
