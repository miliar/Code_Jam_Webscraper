#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MaxString 1000000

void main()
{
	FILE *In, *Out;
	In = fopen("in.txt", "a+");
	Out = fopen("out.txt", "w");

	char* str = new char [MaxString];
	char* res;
	char* tmpstr = new char[10];
	int LenRes;
	fgets(str, MaxString, In);
	int NumCases = atoi(str);
	int NumThirds;
	int NumPairs;
	int NumInvokes;

	for (int Case=1; Case <= NumCases; Case++)
	{
		LenRes = 0;
		res = new char [MaxString];

		//parse input string
		fgets(str, MaxString, In);

		// get the number of thirds
		int i = 0; // current symbol in the string
		int j = 0;
		while(str[i]!=' ')
			tmpstr[j++] = str[i++];
		tmpstr[j] = '\0';
		NumThirds = atoi(tmpstr);
		j=0;

		char** Thirds = new char* [NumThirds];
		for (int k=0; k<NumThirds; k++)
		{
			Thirds [k] = new char [3]; 
			i++;
			for (int m=0; m<3; m++)
				Thirds[k][m] = str[i++];
		}

		//get the number of pairs
		i++;
		while(str[i]!=' ')
			tmpstr[j++] = str[i++];
		tmpstr[j] = '\0';
		NumPairs = atoi(tmpstr);
		j=0;

		char** Pairs = new char* [NumPairs];
		for (int k=0; k<NumPairs; k++)
		{
			Pairs[k] = new char [2];
			i++;
			for (int m=0; m<2; m++)
				Pairs[k][m] = str[i++];
		}

		//start the invoke process
		i++;
		while(str[i]!=' ')
			tmpstr[j++] = str[i++];
		tmpstr[j] = '\0';
		NumInvokes = atoi(tmpstr);
		j=0;
		i++;

		LenRes = 1;
		res[0] = str [i++];

		while (i<strlen(str))
		{
			bool flag = false;
			// check if we can use the rule of third
			for (int k=0; k<NumThirds; k++)
			{
				if (((Thirds[k][0]==res[LenRes-1])&&(Thirds[k][1]==str[i]))||((Thirds[k][1]==res[LenRes-1])&&(Thirds[k][0]==str[i])))
				{
					res[LenRes-1] = Thirds[k][2];
					flag = true;
					break;
				}
			}
			//check if we can use pair rule
			if (!flag)
			{
				bool QQQ = true;
				for (int k=0; k<NumPairs; k++)
				{
					if ((Pairs[k][0]==str[i])||(Pairs[k][1]==str[i]))
					{
						char c;
						if (Pairs[k][0]==str[i])
							c = Pairs[k][1];
						else
							c = Pairs[k][0];
						for (int m=0; m<LenRes; m++)
						{
							if (res[m]==c)
							{
								QQQ = false;
								if ((i<strlen(str)-1))
								{
									LenRes = 1;
									res[0]=str[++i];
								}
								else LenRes = 0;
								break;
							}
						}
					}
				}
				if (QQQ) 
				{
					res[LenRes++] = str[i];						
				}
			}
			i++;
		}
		
		//output the result
		fprintf(Out, "Case #%d: [", Case);
		if (LenRes>1)
		{
			LenRes--;
			for (int l=0; l<LenRes-1; l++)
				fprintf(Out, "%c, ", res[l]);
			fprintf(Out, "%c] \n", res[LenRes-1]);
		}
		else fprintf(Out, "]\n");
		delete [] res;

		for (int i=0; i<NumThirds; i++)
			delete Thirds[i];
		delete Thirds;

		for (int i=0; i<NumPairs; i++)
			delete Pairs[i];
		delete Pairs;
	}

	fclose(In);
	fclose(Out);
}