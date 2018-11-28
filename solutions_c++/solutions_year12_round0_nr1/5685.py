#include <stdio.h>
#include <stdlib.h>


const int length = 26;
const int max    = 1024;
char map[length] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'
 };

int main(void)
{
	int i, j = 0;
	int max_loop, loop;
	char buffer[max];
	char result[max];
	FILE *fread  = fopen("H:\\A-small-attempt3.in","r");
	FILE *fwrite = fopen("H:\\A-small-attempt3.out", "w");

	fgets(buffer, 20, fread);
	max_loop = atoi(buffer);

	for(loop = 0; loop < max_loop; loop++){
		j++;
		fgets(buffer, max, fread);
		for(i = 0 ; i < max; i++)
		{
			if(buffer[i] >= 'a' && buffer[i] <= 'z')	
				buffer[i] = map[buffer[i]-'a'];
		}
		printf("Case #%d: %s", j, buffer);
		sprintf(result, "Case #%d: %s", j, buffer);
		fputs(result, fwrite);
	}
	
	fclose(fread);
	fclose(fwrite);

	return 0;
}

