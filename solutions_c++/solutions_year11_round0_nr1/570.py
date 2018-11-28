#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);

	for(int t=1; t<=T; t++)
	{
		int N,x;
		char c;

		queue<int> O, B, who;
		
		scanf("%d", &N);
		for(int i=0; i<N; i++)
		{
			scanf(" %c %d", &c, &x);
			if(c=='O')
			{
				who.push(1);
				O.push(x);
			}
			else
			{
				who.push(2);
				B.push(x);
			}
		}

		int xB = 1, xO = 1, tB, tO;
		bool bB = !B.empty(), bO = !O.empty(), stop = false;

		int bWho = who.front(); who.pop();
		if(bB){ tB = B.front(); B.pop(); }
		if(bO){ tO = O.front(); O.pop(); }

		int step = 0;

		while(!stop)
		{
			if(bWho==1) // orange pushes
			{
				if(bB)
				{
					if(xB<tB)xB++;
					else if(xB>tB)xB--;
				}
				if(xO==tO) // push it!
				{
					if(who.empty())stop = true;
					else
					{
						bWho = who.front();
						who.pop();
						if(O.empty())bO = false;
						else
						{
							tO = O.front();
							O.pop();
						}
					}
				}
				else if(xO<tO)xO++;
				else xO--;
			}
			else	// blue pushes
			{
				if(bO)
				{
					if(xO<tO)xO++;
					else if(xO>tO)xO--;
				}
				if(xB==tB) // push it!
				{
					if(who.empty())stop = true;
					else
					{
						bWho = who.front();
						who.pop();
						if(B.empty())bB = false;
						else
						{
							tB = B.front();
							B.pop();
						}
					}
				}
				else if(xB<tB)xB++;
				else xB--;
			}

			++step;
		}

		printf("Case #%d: %d\n", t, step);
	}

	return 0;
}