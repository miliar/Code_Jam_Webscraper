#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void main()
{
	FILE *In, *Out;
	In = fopen("in.txt", "a+");
	Out = fopen("out.txt", "w");

	int NumCases;
	char* str = new char [10000];
	fgets(str, 10000, In);
	NumCases = atoi(str);
	long int Res = 0;
	int *Turns;
	int* OrangeButtons;
	int* BlueButtons;

	for (int Case = 1; Case <= NumCases; Case++)
	{
		Res = 0;
		fgets(str, 10000, In);

		int currTurn = 0;
		int oTurn = 0;
		int bTurn = 0;

		int NumTurns = 0;
		int NumBTurns = 0;
		int NumOTurns = 0;

		char* tmpstr = new char [10];

		for (int i=0; i<strlen(str); i++)
		{
			if (str[i]=='O')
			{
				NumTurns++;
				NumOTurns++;
			}
			if (str[i] == 'B')
			{
				NumTurns++;
				NumBTurns++;
			}
		}
		Turns = new int [NumTurns];
		OrangeButtons = new int [NumOTurns];
		BlueButtons = new int [NumBTurns];

		for (int i=0; i<strlen(str); i++)
		{
			if (str[i] == 'O')
				Turns[currTurn++] = 0;
			if (str[i] == 'B')
				Turns[currTurn++] = 1;
		}


		int i = 0;
		int j = 0;
		while (i<strlen(str))
		{
			if (str[i] == 'O')
			{
				i+=2;
				j=0;
				while ((str[i]!=' ')&&(str[i]!='\0'))
				{
					tmpstr[j++] = str[i++];
				}
				tmpstr[j] = '\0';
				OrangeButtons[oTurn++] = atoi(tmpstr);
			}
			if (str[i] == 'B')
			{
				i+=2;
				j=0;
				while ((str[i]!=' ')&&(str[i]!='\0'))
				{
					tmpstr[j++] = str[i++];
				}
				tmpstr[j] = '\0';
				BlueButtons[bTurn++] = atoi(tmpstr);
			}
			i++;
		}

		currTurn = 0;
		oTurn = 0;
		bTurn = 0;

		int t=0;
		int oPos = 1;
		int bPos = 1;
		while (currTurn<NumTurns)
		{
			t++;
			if (oPos < OrangeButtons[oTurn])
				oPos++;
			else
				if (oPos > OrangeButtons[oTurn])
					oPos--;
				else 
					if (Turns[currTurn] == 0)
					{
						currTurn++;
						oTurn++;
						if ((bPos==BlueButtons[bTurn])&&(Turns[currTurn]==1))
							continue;
					}
			if (bPos < BlueButtons[bTurn])
				bPos++;
			else
				if (bPos > BlueButtons[bTurn])
					bPos--;
				else 
					if (Turns[currTurn] == 1)
					{
						currTurn++;
						bTurn++;
					}
		}

		Res = t;

		fprintf(Out, "Case #%d: %d\n", Case, Res);
		delete Turns;
		delete OrangeButtons;
		delete BlueButtons;
		delete tmpstr;
	}

	fclose (In);
	fclose (Out);
	delete [] str;
}