#include <cstdio>
#include <algorithm>
using namespace std;

int C, D, N;
char** toNoneBase = NULL;
char** opposing = NULL;
bool** opposingRelevant = NULL;
char* charStack = NULL;
int charStackFill = 0;

inline bool isOpposing(char c)
{
	for(int i = 0; i < D; i++) 
	{
		if(opposing[i][0] == c)
		{
			if(opposingRelevant[i][1] == true)
			{
				charStackFill = 0;
				for(int j = 0; j < D; j++) 
				{
					opposingRelevant[j][0] = false;
					opposingRelevant[j][1] = false;
				}
				return true;
			}
			opposingRelevant[i][0] = true;
		}
		if(opposing[i][1] == c)
		{
			if(opposingRelevant[i][0] == true)
			{
				charStackFill = 0;
				for(int j = 0; j < D; j++) 
				{
					opposingRelevant[j][0] = false;
					opposingRelevant[j][1] = false;
				}
				return true;
			}
			opposingRelevant[i][1] = true;
		}
	}
	return false;
}

inline void processNextChar(char c)
{
	// Builds non-base element?
	if(charStackFill > 0)
	{
		for(int i = 0; i < C; i++) 
		{
			if((toNoneBase[i][0] == c && toNoneBase[i][1] == charStack[charStackFill-1]) ||
				(toNoneBase[i][1] == c && toNoneBase[i][0] == charStack[charStackFill-1])) 
			{
				charStack[charStackFill-1] = toNoneBase[i][2];
				
				// Check whole new string for opposing
				for(int j = 0; j < D; j++) 
				{
					opposingRelevant[j][0] = false;
					opposingRelevant[j][1] = false;
				}
				
				for(int k = 0; k < charStackFill; k++)
				{
					isOpposing(charStack[k]);
				}
				return;
			}
		}
	}
	
	if(isOpposing(c)) return;
	
	charStack[charStackFill] = c;
	charStackFill++;
}

int main ()
{
	int T, TC = 1, CC, DC, NC;
	char nonBase[3], oppose[2];
	char elem;
	for(scanf("%d", &T); TC <= T; TC++)
    {
		NC = 1;
		scanf("%d", &C);
		if(C > 0) toNoneBase = new char*[C];
		for(CC = 1; CC <= C; CC++)
		{
			toNoneBase[CC-1] = new char[3];
			scanf(" %c%c%c ", &toNoneBase[CC-1][0], &toNoneBase[CC-1][1], &toNoneBase[CC-1][2]);
		}
		scanf("%d", &D);
		if(D > 0) 
		{
			opposing = new char*[D];
			opposingRelevant = new bool*[D];
		}
		for(DC = 1; DC <= D; DC++)
		{
			opposing[DC-1] = new char[2];
			opposingRelevant[DC-1] = new bool[2];
			scanf(" %c%c ", &opposing[DC-1][0], &opposing[DC-1][1]);
			opposingRelevant[DC-1][0] = false;
			opposingRelevant[DC-1][1] = false;
		}
		scanf("%d ", &N);
		charStack = new char[N];
		charStackFill = 0;
		for(NC = 1; NC <= N; NC++)
		{
			scanf("%c", &elem);
			processNextChar(elem);
		}
		
		// Generate output for this case
		printf("Case #%d: [", TC);
		for(int i = 0; i < charStackFill; i++)
		{
			printf("%c", charStack[i]);
			if(i < (charStackFill-1)) printf(", ");
		}
		printf("]\n");
		
		// Cleanup
		for(int i = 0; i < C; i++) {
			delete toNoneBase[i];
		}
		delete toNoneBase;
		toNoneBase = NULL;
		for(int i = 0; i < D; i++) {
			delete opposing[i];
			delete opposingRelevant[i];
		}
		delete opposing;
		delete opposingRelevant;
		opposing = NULL;
		opposingRelevant = NULL;
		delete charStack;
	}

    return 0;
}
