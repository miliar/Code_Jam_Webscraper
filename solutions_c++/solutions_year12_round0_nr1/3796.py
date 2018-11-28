#include <iostream>
using namespace std;

int main()
{
	char m[26];
	char v[26];
	char inp[200] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
	char out[200] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	int i = 0;
	while (inp[i] != '\0')
	{
		if (inp[i] != ' ') m[int(inp[i] - 97)] = out[i];
		i++;
	}
	m[25] = 'q';
	m[16] = 'z';

	for (i = 0; i < 26 ; i++)
	{
		v[m[i] - 97] = i + 97;
	}

	FILE *fpin;
	fpin = fopen("test.txt", "r");
	if (fpin == NULL)
	{
		cout<<"Eroare desc fisier";
		return -1;
	}
	FILE *fpout;
	fpout = fopen("output.txt", "w");

	char linie[102];
	int T;
	fgets(linie, 102, fpin);
	T = atoi(linie);
	int j;
	for (i = 0; i < T; i++)
	{
		fgets(linie, 102, fpin);
		j = 0;
		fprintf(fpout, "Case #%d: ", i + 1);
		while (linie[j] != '\n' && linie[j] != '\0')
		{
			if (linie[j] != ' ') fprintf(fpout, "%c", v[linie[j] - 97]);
			else fprintf(fpout, " ");
			j++;
		}
		fprintf(fpout, "\n");
	}

	fclose(fpin);
	fclose(fpout);

	return 0;
}