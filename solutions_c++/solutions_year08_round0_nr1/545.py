#include <string>
#include <assert.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <map>

void main()
{
	unsigned int n,e,q,cnt,idx;

	char s[200];

	std::map<std::string,unsigned int> v_idx;
	std::vector<int> v_free;
	unsigned int nAvail;

	scanf("%d\n",&n);
	for (unsigned int i=1;i<=n;++i)
	{
		v_idx.clear();
		v_free.clear();
		cnt = 0;

		scanf("%d\n",&e);
		for (unsigned int j=0;j<e;++j)
		{
			gets(s);
			v_idx[s]=j;
			v_free.push_back(1);
		}
		nAvail = e;

 		scanf("%d\n",&q);
 		for (unsigned int j=0;j<q;++j)
 		{
 			gets(s);
			idx = v_idx[s];
			if (v_free[idx])
			{
				--nAvail;
				if (!nAvail) 
				{
					++cnt;
					for (unsigned int k=0;k<e;++k) v_free[k]=1;
					nAvail=e-1;
				}
				v_free[idx] = 0;
			}
 		}
		printf("Case #%d: %d\n",i,cnt);
	}
}