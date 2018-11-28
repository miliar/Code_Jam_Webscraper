#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int n;
int nt;

char who[100][10];
int pos[100];

int getNext(char ch, int from)
{
	while(from < n && who[from][0] != ch) from++;
	return from;
}

int main()
{
	scanf("%d", &nt);
	
	for(int tt = 1; tt <= nt; tt++)
	{	
		printf("Case #%d: ", tt);
		
		scanf("%d", &n);
		
		for(int i = 0; i < n; i++) scanf("%s %d", who[i], &pos[i]);
		
		int posO = 1, posB = 1;
		int cmdO = getNext('O', 0), cmdB = getNext('B', 0);
		
		int T = 0;
		
		while(cmdO != n || cmdB != n)
		{
			T++;
			
			bool was_push = false;
			
			if (cmdO != n && pos[cmdO] != posO)
			{
				// move
				if (posO < pos[cmdO]) posO++; else posO--;
				//printf("O: move to %d\n", posO);
			}
			else
			if (cmdO != n && cmdO < cmdB)
			{
				// push
				//printf("O: push %d\n", posO);
				was_push = true;
			}
			else
			{
				// stay
				//printf("O: stay at %d\n", posO);
			}

			if (cmdB != n && pos[cmdB] != posB)
			{
				// move
				if (posB < pos[cmdB]) posB++; else posB--;
				//printf("B: move to %d\n", posB);
			}
			else
			if (cmdB != n && cmdB < cmdO)
			{
				// push
				//printf("B: push %d\n", posB);
				was_push = true;
			}
			else
			{
				// stay
				//printf("B: stay at %d\n", posB);
			}
			
			if (was_push)
			{
				// fetch next instructions
				if (cmdO != n && posO == pos[cmdO] && cmdO < cmdB) cmdO = getNext('O', cmdO + 1);
				else
				if (cmdB != n && posB == pos[cmdB] && cmdB < cmdO) cmdB = getNext('B', cmdB + 1);
			}
		}
		
		printf("%d\n", T);		
	}
	
	return 0;
}
