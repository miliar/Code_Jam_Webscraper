#include <cstdio>
#include <algorithm>
using namespace std;


int qt, goal, add, test, result, curr; 
int divi, mod;

int main()
{
	scanf("%d", &test);
	
	for(int i=1; i<=test; i++)
	{
		scanf("%d%d%d", &qt, &add, &goal);
		for(int j=0; j<qt; j++)
		{
			scanf("%d", &curr);
			divi=curr/3;
			mod=curr%3;
			if(curr>=goal)
			{
				if(divi>=goal) result++;
				else if(mod>0 && divi+1>=goal) result++;
				else if(mod==0 && add>0 && divi+1>=goal){ result++; add--; }
				else if(mod==2 && add>0 && divi+2>=goal){ result++; add--; }
			}	
		}
		printf("Case #%d: %d\n", i, result);
		result=0;
	}
	
	return 0;
}
