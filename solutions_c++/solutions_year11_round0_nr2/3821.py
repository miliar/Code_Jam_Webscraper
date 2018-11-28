#include <iostream>
#include <string>
#include <cstring>

using namespace std;
int t,C,D,N;
char invo[105],ans[105],tt;
string com,comp;
int used[105];

int main()
{
	int i,ca = 1,len;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&t);

	while(t--)
	{
		com = comp = "zz"; len = 1;
		memset(used,0,sizeof(used));

		scanf("%d",&C);
		if(C == 1) cin>>com;
 
		scanf("%d",&D);
		if(D == 1) cin>>comp;

		scanf("%d",&N);
		scanf("%c",&tt);
		for(i = 1;i <= N;++i) scanf("%c",&invo[i]);

		ans[0] = 'z';

		for(i = 1;i <= N;++i)
		{
			if(invo[i] == com[0] && ans[len-1] == com[1] || invo[i] == com[1] && ans[len-1] == com[0])
			{
				if(used[ans[len-1]-'A'] > 0) --used[ans[len-1]-'A'];

				ans[len-1] = com[2];

				++used[com[2]-'A'];

				continue;
			}

			else 
			{
				ans[len++] = invo[i]; used[invo[i]-'A']++;
			}

			if(used[comp[0]-'A'] && used[comp[1]-'A']) 
			{

				for(int ix = 1;ix < len;++ix)
				{
					int ttt = ans[ix]-'A';
					if(used[ttt] > 0) --used[ttt];
				}
				len = 1;
			}
		}


		printf("Case #%d: [",ca++);

		for(i = 1;i < len;++i) 
		{
			if(i > 1) printf(", ");
			printf("%c",ans[i]);
		}
		printf("]\n");
	}

	return 0;
}