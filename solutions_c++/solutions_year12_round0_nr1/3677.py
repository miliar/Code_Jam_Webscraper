#include <stdio.h>
using namespace std;

int main()
{
	FILE *fin = fopen("infil.txt", "r");
	FILE *fout = fopen("utfil.txt", "w");
	int antal;
	int caseNo = 1;
	char tMatrix[27];
	FILE *gFile;
	FILE *tFile;
	char gletter;
	char tletter;
	char inletter;

  int n = 0;
  int i;

  for (i=0; i<26;i++)
	  tMatrix[i] = '\0';
  tMatrix[26] = 'E';
  gFile=fopen ("translateIn.txt","r");
  tFile=fopen("translateOut.txt","r");
  if (gFile==NULL) perror ("Error opening translate in file");
  else
	  if (tFile==NULL) perror ("Error opening translate out file");
	  else
	  {
		do {
		  gletter = fgetc (gFile);
		  tletter = fgetc (tFile);
		  tMatrix[gletter-97] = tletter; 
		} while (gletter != EOF);
		fclose (gFile);
		fclose (tFile);
	  }
	  tMatrix['z'-97] = 'q';
	  tMatrix['q'-97] = 'z';
//	  printf ("Översättningstabell Googlerese -> other language\n");
//	  for (i=0; i <27; i++)
//	  {
//		  printf("%c %c\n",i+'a', tMatrix[i]); }

	if (fin==NULL) perror ("Error opening input file\n");
	else
	{
		fscanf(fin, "%d\n", &antal);
		for (i=0;i<antal; i++)
		{
			fprintf(fout,"Case #%d: ",caseNo);
			caseNo++;
			do {
				inletter = fgetc (fin);
				if(inletter != 'ÿ')
					fputc(tMatrix[inletter-97],fout); 
		} while (inletter != '\n' && inletter != EOF);
		}
		fclose (gFile);
		fclose (tFile);
		fclose (fin);
		fclose(fout);
	  }

	return 0;
}

