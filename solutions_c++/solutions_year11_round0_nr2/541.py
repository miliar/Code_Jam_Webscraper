#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int C,D,N;
		scanf("%d ",&C);
		char a,b,c;
		map < pair <char,char>,char > f;
		for(int i=0;i<C;i++)
		{
			scanf("%c %c %c ",&a,&b,&c);
			f[make_pair(b,a)]=f[make_pair(a,b)]=c;
		}
		scanf("%d ",&D);
		set < pair <char,char> > op;
		for(int i=0;i<D;i++)
		{
			scanf("%c %c ",&a,&b);
			op.insert(make_pair(a,b));
			op.insert(make_pair(b,a));
		}
		scanf("%d ",&N);
		vector <char> v;
		for(int i=0;i<N;i++)
		{
			scanf("%c ",&a);
			bool cl=false;
			if (v.size()>0&&f.count(make_pair(a,v.back())))
			{
				a=f[make_pair(a,v.back())];
				v.pop_back();
				v.push_back(a);
				cl=true;
			}
			else
			{
				for(int j=0;j<v.size();j++)
					if (op.count(make_pair(a,v[j])))
					{
						v.clear();
						cl=true;
						break;
					}
			}
			if (!cl) v.push_back(a);
		}
		printf("Case #%d: [",t);
		if (v.size()>0) printf("%c",v[0]);
		for(int i=1;i<v.size();i++)
			printf(", %c",v[i]);
		printf("]\n");
	}
	return 0;
}