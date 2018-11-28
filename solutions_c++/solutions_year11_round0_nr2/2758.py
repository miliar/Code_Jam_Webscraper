#include<stdio.h>
#include<conio.h>
#include<string.h>

#define INPUTFILE "B-small.in"
#define OUTPUTFILE "B-small.out"

int t=0;
FILE *in;
FILE *out;

char CStr[36][3];
char DStr[28][2];
long DFlag[2];

int Combine(char *curr, char next, int listCount)
{
	int i;
	for(i=0;i<listCount;i++)
	{
		int currIndex = strchr(CStr[i], *curr) - CStr[i];
		int nextIndex = strrchr(CStr[i], next) - CStr[i];
		if(currIndex < 2 && nextIndex < 2 && currIndex != nextIndex && currIndex >= 0 && nextIndex >= 0)
		{
			char ret = *curr;
			*curr = CStr[i][2];
			return ret;
		}

	}
	curr++;
	*curr = next;
	return 0;
}

void RefreshFlags(char curr, int listCount)
{
	int i;
	for(i=0; i<listCount; i++)
	{
		int index = strchr(DStr[i], curr) - DStr[i];
		if(index >= 0)
		{
			DFlag[index] |= ( 1 << i );
		}
		index = strrchr(DStr[i], curr) - DStr[i];
		if(index >= 0)
		{
			DFlag[index] |= ( 1 << i );
		}

	}
}

void ClearFlag(char curr, int listCount)
{
	int i;
	for(i=0; i<listCount; i++)
	{
		int index = strchr(DStr[i], curr) - DStr[i];
		if(index >= 0)
		{
			DFlag[index] &= ~( 1 << i );
		}
		index = strrchr(DStr[i], curr) - DStr[i];
		if(index >= 0)
		{
			DFlag[index] &= ~( 1 << i );
		}

	}

}

void main(void)
{
	clrscr();

	in = fopen(INPUTFILE,"r");
	out = fopen(OUTPUTFILE,"w");

	fscanf(in, "%d", &t);
	for(int ti=0; ti<t; ++ti)
	{
		int C, D, N;
		char outString[100];
		char NStr[100];
		char *ptr;

		memset(DFlag, 0, sizeof(long) * 2);
		fscanf(in, "%d", &C);

		for(int ci=0; ci<C; ci++)
		{
			memset(CStr[ci],0,3);
			fscanf(in, "%s", CStr[ci]);
		}

		fscanf(in, "%d", &D);

		for(int di = 0; di<D; di++)
		{
			memset(DStr[di],0,2);
			fscanf(in, "%s", DStr[di]);
		}

		memset(NStr, 0, 100);
		memset(outString, 0, 100);

		fscanf(in, "%d", &N);
		fscanf(in, "%s", NStr);

		ptr = outString;

		for(int ni=0;ni<N;ni++)
		{
			if(outString[0] == 0)
			{
				*ptr = NStr[ni];
				RefreshFlags(*ptr, D);
			}
			else
			{
				char last;
				if(!(last = Combine(ptr, NStr[ni], C)))
					ptr++;
				else
				{
					if(!strchr(outString, last))
					{
						ClearFlag(last, D);
					}
				}
				RefreshFlags(*ptr, D);
				if(DFlag[0] & DFlag[1] != 0)
				{
					ptr = outString;
					memset(outString, 0, 100);
					memset(DFlag, 0, sizeof(long) * 2);
				}
			}
		}

		fprintf(out, "Case #%d: [", ti+1);

		ptr = outString;
		while(*ptr != 0)
		{
			if(*(ptr+1) == 0)
			{
				fprintf(out, "%c", *ptr);
			}
			else
			{
				fprintf(out, "%c, ", *ptr);
			}
			ptr++;
		}
		fprintf(out, "]\n");
	}
	fclose(in);
	fclose(out);
	printf("Done.");
	getch();
}