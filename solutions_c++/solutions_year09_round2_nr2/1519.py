#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct item
{
	char aChar;
	int n;
};

char *convert(int num)
{
	char *arr = new char[25];
	int index = 0;
	while(num > 0)
	{
		arr[index++] = (num % 10) + 0x30;
		num /= 10;
	}
	/*char aux;
	for(int i = 0; i < (index / 2); i++)
	{
		aux = arr[index - 1 - i];
		arr[index - 1 - i] = arr[i];
		arr[i] = aux;
	}*/
	//ver

	arr[index] = 0;
	return arr;
}

int isInItems(item *pItems, int size, char ch)
{
	for(int w = 0; w < size; w++)
		if(pItems[w].aChar == ch)
			return w;
	return -1;
}

bool isValid(int n, item *pItems, int size)
{
	char *arr = convert(n);
	item *pAux = (item*)malloc(size * sizeof(item));
	memcpy(pAux, pItems, size * sizeof(item));
	for(int x = 0; x < size; x++)
		pAux[x].n = 0;
	int arrLen = strlen(arr);
	int res;
	for(int i = 0; i < arrLen; i++)
	{
		res = isInItems(pAux, size, arr[i]);
		if(res != -1)
			pAux[res].n++;
		else if(arr[i] != '0')
		{
			delete[] arr;
			free(pAux);
			return false;
		}
	}
	for(int ind = 0; ind < size; ind++)
	{
		if((pItems[ind].n != pAux[ind].n) && (pAux[ind].aChar != '0'))
		{
			delete[] arr;
			free(pAux);
			return false;
		}
	}
	delete[] arr;
	free(pAux);
	return true;
}

int buscar(item *pItems, int size, int n)
{
	bool isValidInt = false;
	while(!isValidInt)
		isValidInt = isValid(++n, pItems, size);
	return n;
}

item *convertToItems(int num, int *size)
{
	item *pItems = new item[25];
	memset(pItems, 0, 25 * sizeof(item));
	int index = 0;
	int res;
	int nMod;
	while(num > 0)
	{
		nMod = (num % 10) + 0x30;
		res = isInItems(pItems,25,nMod);
		if(res == -1)
		{
			pItems[index].aChar = nMod;
			pItems[index].n++;
			index++;
		}
		else
			pItems[res].n++;
		num /= 10;
	}
	/*item aux;
	for(int i = 0; i < (index / 2); i++)
	{
		aux = pItems[index - i];
		pItems[index - i] = pItems[i];
		pItems[i] = aux;
	}*/
	//ver
	*size = index;
	return pItems;
}

int main(int argc, char *argv[])
{
	if(argc != 2)
		return -1;
	FILE *fInput = fopen(argv[1],"rb");
	if(!fInput)
	{
		printf("No encuentro el archivo\n");
		return -2;
	}
	FILE *fOutput = fopen("output.out", "wb");
	
	int nCases;
	fscanf(fInput, "%d\n", &nCases);
	char buf[75];
	for(int aCase = 0; aCase < nCases; aCase++)
	{
		int n;
		fscanf(fInput, "%d\n", &n);
		int size;
		item *pItems = convertToItems(n, &size);
		
		sprintf(buf,"Case #%d: %d\r\n", aCase + 1, buscar(pItems, size, n));
		printf(buf);
		fputs(buf,fOutput);
		delete[] pItems;
	}
	fflush(fOutput);
	fclose(fInput);
	fclose(fOutput);
	return 0;
}
