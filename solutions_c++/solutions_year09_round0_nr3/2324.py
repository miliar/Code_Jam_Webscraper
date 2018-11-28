// ViszinisA

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

char c[500] = {};
char usefull[] = " acdejlmotw"; // 11
char z[] = "welcome to code jam"; // 19
int subs, char_count;

int inarray(char a)
{
	for (int j=0; j<11; j++) {
		if (a==usefull[j]) return 1;
	}
	return 0;
};

void find(int start, int letter)
{
	int pos;
	//cout << start << ";" << letter << ";" << char_count-(18-letter) << ";" << char_count << endl;
	pos = start;
	while (pos<char_count-(18-letter))
	{
		if (c[pos] == z[letter] && letter == 18)
		{
			subs++;
		} else if (c[pos] == z[letter]) {
			find (pos+1,letter+1);
		}
		pos++;
	}
};

int main ()
{
	FILE * pfin, * pfout;
	pfin = fopen ("c.in", "r");
	pfout = fopen ("c.out", "w");

	char d;
	int i, j, rows;

	//fscanf (pfin, "%d %d %d\n", &l, &d, &n);
	
	fscanf (pfin, "%d\n", &rows);
	
	for(i=1;i<=rows;i++)
	{
		if (i>1)
		{
			fprintf (pfout, "\n");
		}
		subs = 0;
		char_count = 0;
		do {
			d = fgetc (pfin);
			if (d == '\n') break;
			if (inarray (d))
			{
				c[char_count] = d;
				char_count++;
			}
		} while (d != EOF);
		find (0,0);
		//cout << "Case #" << i << ":" << subs;
		fprintf (pfout, "Case #%d: %04d",i,subs);
	}

	fclose (pfin);
	fclose (pfout);
	system ("Pause");
	return 0;
}
