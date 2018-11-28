#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int res=0;
		int n,pos[102]={0},ch[102]={0};
		scanf("%d ",&n);
		for(int i=0;i<n;i++)
			scanf("%c %d ",&ch[i],&pos[i]);
		int posO=1,posB=1,free=0,last=0;
		for(int i=0;i<n;i++)
		{
			if (ch[i]=='O')
			{
				int need=max(0,abs(pos[i]-posO)-free*last)+1;
				res+=need;
				if (last==1) free=need;
				else free+=need;
				posO=pos[i];
				last=0;
			}
			else
			{
				int need=max(0,abs(pos[i]-posB)-free*(1-last))+1;
				res+=need;
				if (last==0) free=need;
				else free+=need;
				posB=pos[i];
				last=1;
			}
		}
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}