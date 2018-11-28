#include <stdio.h>
#include <string.h>

#define MSG_SIZE 19
char szWelcome[] = {"welcome to code jam"};
char szText[600]="";
int g_nTextSize = 0;


void FindString(int nPoint, int nNext, unsigned long* pnCount);
int main(int argc, char* argv[])
{
	if(argc < 2)
		return 0;

	FILE* fp = fopen(argv[1], "r");
	FILE* fout = fopen("c:\\Out.txt", "w+");

	if(fp != NULL && fout != NULL)
	{
		int nCase;
		fscanf(fp,"%d\n", &nCase);
		//fgets(szText, 500, fp);
		for(int i=0; i<nCase; i++)
		{
			if(fgets(szText, 550, fp) != NULL)
			{
				int nPoint =0, nNext =0;
				unsigned long	nCount=0;
				//bFirst = false;

				g_nTextSize = strlen(szText);

				FindString(nPoint, nNext, &nCount);
				fprintf(fout, "Case #%d: %0.4u\n", i+1, nCount);
			}
		}
	}

	return 0;
}

void FindString(int nPoint, int nNext, unsigned long* pnCount)
{
	if(nPoint < MSG_SIZE)
	{
		char ch = szWelcome[nPoint];
		while(nNext< g_nTextSize)
		{
			if(szText[nNext] == ch)
			{
				//printf("%s\n", szText+nNext);
				if(ch == 'm' && nPoint == MSG_SIZE -1)
				{
					(*pnCount)++;
				}
				else
				{
					FindString(nPoint+1, nNext, pnCount);
				}
			}

			nNext++;
		}
	}
}