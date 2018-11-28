#include <iostream>
#include <memory.h>

using namespace std;

FILE *inp = fopen("C-small.in", "rt"),
	*out = fopen("C-small.out", "wt");

int p[19][500], s[19][500], l[19];
char str[501];
int len = 1;

inline void add(int i, int v)
{
	p[i][l[i]++] = v;
}

int main(int argc, char *argv[])
{
	int n = 0;
	fscanf(inp, "%d\n", &n);
	for (int cs = 0; cs < n; cs++)
	{
		memset(str, 0, len * sizeof(char));
		memset(p, -1, 19*500 * sizeof(int));
		memset(s, 0, 19*500 * sizeof(int));
		memset(l, 0, 19 * sizeof(int));
		len = 0;

		do
		{
			fscanf(inp, "%c", &str[len++]);
		}while (str[len-1] != '\n');

		for (int i = 0; i < len; i++)
		{
			switch(tolower(str[i]))
			{
			case 'w':
				add(0, i);
				break;
			case 'e':
				add(1, i);
				add(6, i);
				add(14, i);
				break;
			case 'l':
				add(2, i);
				break;
			case 'c':
				add(3, i);
				add(11, i);
				break;
			case 'o':
				add(4, i);
				add(9, i);
				add(12, i);
				break;
			case 'm':
				add(5, i);
				add(18, i);
				break;
			case ' ':
				add(7, i);
				add(10, i);
				add(15, i);
				break;
			case 't':
				add(8, i);
				break;
			case 'd':
				add(13, i);
				break;
			case 'j':
				add(16, i);
				break;
			case 'a':
				add(17, i);
				break;
			}
		}
		

		for (int i = 0; i < l[18]; i++) s[18][i] = 1;
		for (int i = 17; i >= 0; i--)
			for (int j = 0; j < l[i]; j++)
				for (int k = l[i+1] - 1; (k >= 0) && (p[i][j] < p[i+1][k]); k--)
						s[i][j] += s[i+1][k];

		int answ = 0;
		for (int i = 0; i < l[0]; i++)
				answ = (answ + s[0][i]) % 10000;
		fprintf(out, "Case #%d: %4.4d\n", cs + 1, answ);
	}
	
	return 0;
}