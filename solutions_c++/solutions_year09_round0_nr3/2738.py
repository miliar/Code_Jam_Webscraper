#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

unsigned int stateCounts[19];

void resetStates()
{
	int i = 0;
	while (1)
	{
		if (i == 19)
			break;

		stateCounts[i] = 0;

		i++;
	}
}

string solveString(string & str)
{
	char m;

	int i = 0;
	while (1)
	{
		if (i == str.size())
			break;
		m = str[i];

		switch(m)
		{
		case 'w':
			stateCounts[0]++;
			break;
		case 'e':
			stateCounts[1] += stateCounts[0];
			stateCounts[6] += stateCounts[5];
			stateCounts[14] += stateCounts[13];
			break;
		case 'l':
			stateCounts[2] += stateCounts[1];
			break;
		case 'c':
			stateCounts[3] += stateCounts[2];
			stateCounts[11] += stateCounts[10];
			break;
		case 'o':
			stateCounts[4] += stateCounts[3];
			stateCounts[9] += stateCounts[8];
			stateCounts[12] += stateCounts[11];
			break;
		case 'm':
			stateCounts[5] += stateCounts[4];
			stateCounts[18] += stateCounts[17];
			break;
		case ' ':
			stateCounts[7] += stateCounts[6];
			stateCounts[10] += stateCounts[9];
			stateCounts[15] += stateCounts[14];
			break;
		case 't':
			stateCounts[8] += stateCounts[7];
			break;
		case 'd':
			stateCounts[13] += stateCounts[12];
			break;
		case 'j':
			stateCounts[16] += stateCounts[15];
			break;
		case 'a':
			stateCounts[17] += stateCounts[16];
			break;
		default:
			break;
		}

		i++;
	}

	stateCounts[18] = stateCounts[18] % 10000;

	string solution;
	solution.resize(4);

	i = 0;
	while (1)
	{
		if (i == 4)
			break;

		solution[3 - i] = stateCounts[18] % 10 + 48;
		stateCounts[18] /= 10;

		i++;
	}

	return solution;
}

int main()
{
	FILE * input = fopen("C-small-attempt1.in","r+");
	FILE * output = fopen("output","w+");

	if (input == NULL)
		return 0;

	int strCount;

	fscanf(input,"%d\n",&strCount);

	char key;
	string str;

	int i = 0;
	while (1)
	{
		if (i == strCount)
			break;

		resetStates();
		str.resize(0);

		while (1)
		{
			if (fscanf(input,"%c",&key) != 1)
				break;
			if (key == '\n' || key == EOF)
				break;

			str += key;
		}

		fprintf(output,"Case #%d: %s\n",i+1,solveString(str).c_str());

		i++;
	}

	fclose(input);
}