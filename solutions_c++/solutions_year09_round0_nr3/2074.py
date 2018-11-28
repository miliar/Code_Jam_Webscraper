/*
 *  Google Code Jam 2009
 *  Qualification Round - Problem C - Welcome to Code Jam
 */


#include <stdio.h>
#include <string.h>

#define INPUT_FILE		"input.txt"
#define OUTPUT_FILE		"output.txt"
#define PASSWORD		"welcome to code jam"


int N, Len_pass;
long Sol[512];
int Pos[512];
char Text[512], Pass[128];


long Recursive(int pos, int pos_pass)
{
	int i;
	char ch;
	long sum = 0;

	if (pos_pass == 0)
		return 0;


	ch = Pass[pos_pass - 1];

	for (i = pos; i >= 0; i--)
		if (Text[i] == ch)
		{
			if (Sol[i] == 0)
			{
				Sol[i] = Recursive(i - 1, pos_pass - 1);
				Pos[i] = pos_pass - 1;
			}
			if (Pos[i] == pos_pass - 1)
				sum += Sol[i] % 10000;
		};

	return sum;
}

long Solve()
{
	int i, len_text = strlen(Text);

	memset(Sol, 0, sizeof(Sol));
	memset(Pos, 0, sizeof(Pos));

	/* start positions */
	for (i = 0; i < len_text; i++)
		if (Text[i] == Pass[0])
		{
			Sol[i] = 1;
		}

	Sol[len_text - 1] = Recursive(len_text - 2, Len_pass - 1);

	return Sol[len_text - 1];
}

int main()
{
	int i;

	strcpy(Pass, PASSWORD);
	strcat(Pass, "@");
	Len_pass = strlen(Pass);

	freopen(INPUT_FILE, "rt", stdin);
	freopen(OUTPUT_FILE, "wt", stdout);

	scanf("%d\n", &N);

	for (i = 0; i < N; i++)
	{
		gets(Text);
		strcat(Text, "@");

		long sol = Solve();

		printf("Case #%d: %04ld\n", i + 1, sol);
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}