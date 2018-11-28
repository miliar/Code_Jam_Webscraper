//Welcome to code jam - Google Code Jam 2009 - Qualification Round

#include <stdio.h>
#include <iostream.h>

const char input[] = "welcome to code jam";
const int max = 10000;
const int lenMax = 512;



int main()
{
	freopen("codejam3.in", "r", stdin);
	freopen("codejam3.out", "w", stdout);

	int testCnt;
	scanf("%d\n", &testCnt);
	
	int len = strlen(input);
	
	int i;
	for(i = 1; i <= testCnt; ++i)
	{
		char *text = new char[lenMax];
		cin.getline(text, lenMax);
		
		int *posCnt = new int[len+1];
		
		int j;
		for(j = 0; j <= len; ++j) posCnt[j] = 0;
		posCnt[0] = 1;
		
		for(j = 0; text[j]; ++j)
		{
			int k;
			for(k = 0; k < len; ++k) 
				if(text[j] == input[k])
					posCnt[k+1] = (posCnt[k+1] + posCnt[k]) % max;
		}
		
		printf("Case #%d: %04d\n", i, posCnt[len]);
	}
	
	return 0;
}
