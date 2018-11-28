#include <iostream>
#include <vector>
using namespace std;

int CycleArray(char listC[], int size, int cycle)
{
	int* list = new int[size];

	int* newList = new int[size];

	for(int i=0; i<size; i++)
	{
		list[i] = listC[i]-'0';
	}

	for(int i=0; i<size; i++)
	{
		if(i+cycle < size)
			newList[i] = list[i+cycle];
		else
			newList[i] = list[i+cycle-size];
	}
	
	for(int i=0; i<size; i++)
	{
		listC[i] = newList[i]+'0';
	}

	return 1;

}

int CharNumber(int number)
{
	for(int i=0; i<9; i++)
	{
		if(number/(int)pow(10.0,(double)i) == 0)
			return i;
	}

	return -1;
}

int Shifting(int number, int shifting)
{
	char Array[30];

	itoa(number,Array,10);

	int ArraySize = 0;

	for(int j=0; j<30; j++)
	{
		if(Array[j] >= 48)
			ArraySize++;
	}

	CycleArray(Array,ArraySize,shifting);

	return atoi(Array);
}


void main()
{
	FILE* Input = fopen("in.in","r");
	FILE* Output = fopen("out.txt","w+");

	int T = 0;
	int A = 0;
	int B = 0;

	int FinalResult = 0;

	int CharNumb = 0;
	int ShiftNumb = 0;

	fscanf(Input, "%d\n", &T);

	for(int l=0; l<T; l++)
	{
		fscanf(Input, "%d %d", &A, &B);
		CharNumb = CharNumber(B);

		FinalResult = 0;

		for(int i=A; i<=B-1; i++)
		{
			for(int k=0; k<CharNumb; k++)
			{
				ShiftNumb = Shifting(i,k);
				if(ShiftNumb <= B && ShiftNumb > i)
					FinalResult++;
			}
		}

		fprintf(Output, "Case #%d: %d\n", l+1, FinalResult);
	}

	fclose(Output);
}