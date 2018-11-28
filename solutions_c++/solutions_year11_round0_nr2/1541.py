#include <cstdio>
#include <memory.h>
#include <vector>
using namespace std;
char create[26][26];
int  oppost[26][26];
int main()
{
	int T; scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		memset(create,0,sizeof(create));
		memset(oppost,0,sizeof(oppost));
		int n,m,k;
		scanf("%d",&n);
		for (int q=0;q<n;++q)
		{
			char buf[5];
			scanf("%s",buf);
			create[buf[0]-'A'][buf[1]-'A'] = buf[2];
			create[buf[1]-'A'][buf[0]-'A'] = buf[2];
		}
		scanf("%d",&m);
		for (int q=0;q<m;++q)
		{
			char buf[5];
			scanf("%s",buf);
			oppost[buf[0]-'A'][buf[1]-'A'] = 1;
			oppost[buf[1]-'A'][buf[0]-'A'] = 1;
		}
		scanf("%d",&k);
		char buf[105];
		vector<char> ret;
		scanf("%s",buf);
		for (int q=0;q<k;++q)
		{
			if (ret.empty()) ret.push_back(buf[q]);
			else if (create[ret.back()-'A'][buf[q]-'A'])
			{
				int i = ret.back()-'A';
				ret.pop_back();
				ret.push_back(create[i][buf[q]-'A']);
			}
			else
			{
				//CLEAR CHECK
				int cls = 0;
				for (int w=0;w<(int)ret.size();++w)
					if (oppost[ret[w]-'A'][buf[q]-'A'])
						cls = 1;
				if (cls) ret.clear();
				else     ret.push_back(buf[q]);
			}
		}
		printf("Case #%d: [",kase);
		for (int q=0;q<(int)ret.size();++q)
		{
			if (q>0) printf(", ");
			printf("%c",ret[q]);
		}
		printf("]\n");
	}
	return 0;
}

