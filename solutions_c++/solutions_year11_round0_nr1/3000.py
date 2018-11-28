#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T,N;
	char color;
	int ans, target;
	int Po, Pb, To, Tb;
	int i;

	freopen("D:\\VC2005\\google\\2011\\P1\\p1.in","r",stdin);
	freopen("D:\\VC2005\\google\\2011\\P1\\p1.out","w",stdout);

	scanf("%d\n", &T);
	
	for(i=1;i<=T;i++)
	{
		ans = 0;
		Po = 1;
		Pb = 1;
		To = 0;
		Tb = 0;

		scanf("%d", &N);
		while(N--)
		{
			scanf(" %c %d", &color, &target);
			//printf("%c %d\n", color, target);
			if(color=='O')
			{
				if(To >= abs(target-Po))
				{
					ans++;
					Tb++;
				}
				else
				{
					ans = ans + abs(target-Po) - To + 1;
					Tb = Tb + abs(target-Po) - To + 1;
				}
				Po = target;
				To = 0;
			}
			else
			{
				if(Tb >= abs(target-Pb))
				{
					ans++;
					To++;
				}
				else
				{
					ans = ans + abs(target-Pb) - Tb + 1;
					To = To + abs(target-Pb) -Tb + 1;
				}
				Pb = target;
				Tb = 0;
			}
		}
		scanf("\n");
		printf("Case #%d: %d\n", i, ans);
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
