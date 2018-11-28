#include <cstdio>
#include <cstdlib>
#include <iostream>
using std::cout;
using std::endl;
int main()
{
	FILE* infid = fopen("large.in","r");
	FILE* outfid = fopen("large.out","w");
	int cases;
	int pd,pg;
	long long n;
	fscanf(infid,"%d",&cases);
	for(int cc=1; cc<=cases; ++cc)
	{
		bool ok = false;
		fscanf(infid,"%lld%d%d",&n,&pd,&pg);
		for(int dw=1; dw<=n && dw <=100; ++dw)
		{
			if(pg==0 && pd >0)
			{
				 continue;
			}
			if(pg == 100 && pd < 100)
			{
				continue;
			}
			if(dw*pd % 100 ==0)
			{
				ok = true;
			}
		}
		if(n >100)
		{
			ok = true;
		}
		if(pg==0 && pd >0)
		{
			ok = false;
		}
		if(pg == 100 && pd < 100)
		{
			ok = false;
		}
		if(ok)
		{
			fprintf(outfid,"Case #%d: Possible\n",cc);
		}
		else
		{
			fprintf(outfid,"Case #%d: Broken\n",cc);
		}
		
	}
	return 0;
}
