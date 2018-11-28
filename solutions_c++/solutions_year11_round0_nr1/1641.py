#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
	int T;scanf("%d",&T);
	for (int kase=1;kase<=T;++kase)
	{
		int where[2]={1,1};
		int when [2]={0,0};
		int n;
		scanf("%d",&n);
		for (int q=0;q<n;++q)
		{
			char buf[2]; int pos;
			scanf("%s %d",buf,&pos);
			int mover = (buf[0] == 'B');
			when[mover] = max(when[mover] + abs(where[mover]-pos), max(when[0],when[1])) + 1;
			where[mover] = pos;
		}
		printf("Case #%d: %d\n",kase,max(when[0],when[1]));

	}
	return 0;
}
