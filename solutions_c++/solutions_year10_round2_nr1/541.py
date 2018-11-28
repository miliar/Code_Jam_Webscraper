#include <cstdio>
#include <map>
#include <string>
#include <set>
using namespace std;

set<string> tree;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	scanf("%d\n",&t);

	for(int ti = 0;ti < t;ti++)
	{
		char buf[200];
		tree.clear();
		tree.insert("");
		int n,m;
		scanf("%d%d\n",&n,&m);
		for(int i=0;i<n;i++)
		{
			gets(buf);
			string st(buf);
			st = st + '/';
			for(int j=0;j<st.size();j++)
				if(st[j] == '/')
					tree.insert(st.substr(0,j));
		}
		int count = 0;
		for(int i=0;i<m;i++)
		{
			gets(buf);
			string st(buf);
			st = st + '/';
			for(int j=0;j<st.size();j++)
				if(st[j] == '/')
				{
					if(tree.count(st.substr(0,j)) == 0)
					{
						count++;
						tree.insert(st.substr(0,j));
					}
				}
		}
		printf("Case #%d: %d\n",ti+1,count);

//		for(set<string>::iterator it = tree.begin();it != tree.end();it++)	puts(it->c_str());		puts("");
		
	}
	return 0;
}
