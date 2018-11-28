#include <cstdio>
#include <string>

using namespace std;

string phrase = "welcome to code jam";

int main()
{
	FILE* input = fopen("codejam.in", "r");
	FILE* output = fopen("codejam.out", "w");
	int n;
	fscanf(input, "%d\n", &n);
	int i;
	for (i = 0; i < n; i++)
	{
		char line[701];
		char temp;
		int length = 0;
		fscanf(input, "%c", &temp);
		while (temp != '\n')
		{
			line[length] = temp;
			length++;
			fscanf(input, "%c", &temp);
		}
		line[length] = 0;
		int answer[2][701];
		int c = 0;
		int j, k;
		for (j = 0; j < strlen(line); j++)
		{
			answer[0][j] = 0;
			answer[1][j] = 1;
		}
		for (j = 0; j < phrase.length(); j++)
		{
			c = 0;
			for (k = 0; k < strlen(line); k++)
			{
				if (line[k] == phrase[j])
				{
					c+=answer[(j+1)%2][k];
					c%=10000;
				}
				answer[j%2][k] = c;
			}
		}
		char templol[10];
		sprintf(templol, "%d", answer[(j+1)%2][k-1]+10000);
		fprintf(output, "Case #%d: %s\n", i+1, &templol[1]);
	}
}