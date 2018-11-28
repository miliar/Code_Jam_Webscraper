#include <stdio.h>
#include <stdlib.h>

char **words;
int L,D;

bool isLetterInWords(char **wordsArr, char *let,int count, int pos)
{
	bool isIn = false;
	for(int d = 0; d < D; d++)
	{
		if(words[d] != NULL)
		{
			bool partialIn = false;
			for(int j = 0; j < count; j++)
			{
				if(words[d][pos] == let[j])
				{
					partialIn = true;
					isIn = true;
				}
			}
			if(!partialIn)
				wordsArr[d] = NULL;
		}
	}
	return isIn;
}

int main(int argc, char *argv[])
{
	if(argc != 2)
		return -1;
	FILE *pFile;
	if((pFile = fopen(argv[1],"rb")) == NULL)
		return -2;
	int N;
	fscanf(pFile,"%d %d %d\n", &L,&D,&N);
	words = new char*[D];
	for(int i = 0; i < D; i++)
	{
		words[i] = new char[L];
		for(int let = 0; let < L; let++)
		{
			fscanf(pFile,"%c",&words[i][let]);
			printf("%c", words[i][let]);
		}
		printf("\n");
		fgetc(pFile);//\n
		//fgetc(pFile);//\n
	}
	FILE *output = fopen("output.txt","wb");
	//Dictionary built.
	int aChar;
	char letters[35];
	bool goOn = true;
	for(int i = 0; i < N; i++)
	{
		int index = 0;
		char **wordsAux = new char*[D];
		for(int x = 0; x < D; x++)
			wordsAux[x] = words[x];
		goOn = true;
		for(int wds = 0;(wds < L) && goOn; wds++)
		{
			aChar = fgetc(pFile);
			if(aChar != '(')
			{
				if(!isLetterInWords(wordsAux, (char*)&aChar,1, wds))
					goOn = false;
			}
			else
			{
				aChar = fgetc(pFile);
				int cant = 0;
				while(aChar != ')')
				{
					letters[cant++] = aChar;
					aChar = fgetc(pFile);
				}
				isLetterInWords(wordsAux,letters,cant,wds);
			}
		}
		aChar = fgetc(pFile);
		while((aChar != '\n') && (aChar != EOF))
			aChar = fgetc(pFile);
		//fgetc(pFile);

		int count = 0;
		if(goOn)
		{
			for(int x = 0; x < D; x++)
			{
				if(wordsAux[x] != NULL)
					count++;
			}
		}
		char buf[25];
		sprintf(buf,"Case #%d: %d\r\n",i + 1,count);
		fputs(buf,output);
		printf(buf);
		delete[] wordsAux;
	}
	fflush(output);
	fclose(output);
	getchar();
	return 0;
}
