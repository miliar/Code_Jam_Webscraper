//The text number

#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const char input[] = "codejam22.in";
const char output[] = "codejam22.out";

const int cifreCntMax = 21;

int main()
{
	freopen(input, "r", stdin);
	freopen(output, "w", stdout);
	
	int t;
	scanf("%d", &t);
	
	int i;
	for(i = 1; i <= t; ++i)
	{
		char *numar = new char[cifreCntMax + 1];
		scanf("%s",  numar);
		
		int len = strlen(numar);
		int j;
		for(j = len - 1; j && numar[j-1] >= numar[j]; --j);
		if(j)
		{
			sort(numar+j, numar+len);
			int k;
			for(k = j; numar[k] <= numar[j-1]; ++k) ;
			int aux = numar[j-1]; numar[j-1] = numar[k]; numar[k] = aux;
			printf("Case #%d: %s\n", i, numar);
		}
		else
		{
			sort(numar, numar+len);
			int k;
			for(k = 0; numar[k] == '0'; ++k);
			printf("Case #%d: %c0", i, numar[k]);
			for(j = 0; j < k; ++j)
				printf("%c", numar[j]);
			if(k < len-1) printf("%s\n", numar+k+1);
			else printf("\n");
		}
		
	}
	
	return 0;
}
