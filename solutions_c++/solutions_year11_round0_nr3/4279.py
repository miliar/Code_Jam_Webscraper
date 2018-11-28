#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int nbTest;
int plus_petit;
int total = 0;
int xor_courant;

int main()
{
	scanf("%d", &nbTest);
	for(int test = 0; test < nbTest; test++)
	{
		int nbBonbons;
		scanf("%d", &nbBonbons);
		
		int v_init;
		total = 0;
		scanf("%d", &v_init);
		xor_courant = v_init;
		plus_petit = v_init;
		total += v_init;
		
		for(int i = 1; i < nbBonbons; i++)
		{
			int v;
			scanf("%d", &v);
			xor_courant = v ^ xor_courant;
			plus_petit = min(plus_petit, v);
			total += v;
		}
		
		if(xor_courant == 0)
			printf("Case #%d: %d\n", test+1, total - plus_petit);
		else
			printf("Case #%d: NO\n", test+1);
	}
	
	
	return 0;
	
}