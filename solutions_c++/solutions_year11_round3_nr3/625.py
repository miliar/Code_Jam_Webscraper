#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
		
int main()
{
	int cases;
	int N,L,H,notes[10000];

	scanf("%d",&cases);
	
	for(int iD=1;iD<=cases;iD++)
	{
		printf("Case #%d: ",iD);
		scanf("%d %d %d",&N,&L,&H);
		for(int i=0;i<N;i++)
			scanf("%d",&notes[i]);
		
		bool ok=false;
		int ans;
		for(int f=L;f<=H;f++)
		{
			bool good=true;
			for(int i=0;good && i<N;i++)
				if(notes[i]%f && f%notes[i]) good=false;
			if(good)
			{
				ok=true;
				ans=f;
				break;
			}	
		}

		if(ok) printf("%d\n",ans);
		else printf("NO\n");
	}

	return 0;
}

