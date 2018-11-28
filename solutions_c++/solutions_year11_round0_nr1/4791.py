#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int main()
{
	int t, n = 1;

	scanf("%d\n", &t);

	while(n <= t)
	{
		int nn, o[100], b[100];

		char c;

		scanf("%d ", &nn);

		int ans = 0, ol = 1, bl = 1, ot = 0, bt = 0;

		for(int i = 0; i < nn; i++)
		{
			scanf("%c ", &c);

			int l;

			scanf("%d ", &l);

			if(c == 'O')
			{
				int j = abs(ol - l) - ans + ot;

				if(j <= 0)
					ans += 1;
				else
					ans += j + 1;

				ot = ans;

				ol = l;
			}
			else if(c == 'B')
                        {
			//	cout<<c<<" "<<l<<"\n";
                                int j = abs(bl - l) - ans + bt;

                                if(j <= 0)
                                        ans += 1;
                                else
                                        ans += j + 1;

                                bt = ans;

                                bl = l;
                        }

		}

//		int ans = 0;

		

		printf("Case #%d: %d\n", n, ans);
		n++;
	}

	return 0;
}
