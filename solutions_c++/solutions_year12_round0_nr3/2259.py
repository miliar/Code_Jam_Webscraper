#include <iostream>
#include <string.h>
#include <math.h>
#include <map>
using namespace std;

class Circular
{
public:
	int count;
	int num[6];

	Circular():count(0){memset(num,0,sizeof(int)*6);}

	void FillCircular( int myNum )
	{
		int aux = myNum;
		
		int noOfDigits = log10((float)aux)+1;

		int p = pow((double)10,noOfDigits-1);

		for(int i=1;i<noOfDigits;i++)
		{
			aux = (aux%p)*10 + aux/p;
			if(aux>myNum && IsUnique(aux))
			{
				num[count] = aux;
				count++;
			}
		}
	}

	bool IsUnique(int a)
	{
		for(int i=0;i<count;i++)
		{
			if(num[i]==a)
				return false;
		}
		return true;
	}
};


int main()
{
	FILE* inFP = fopen("C-large.in","rb");
	FILE* outFP = fopen("3large.out","wb");

	Circular* C = new Circular[2000001];

	for(int i=1;i<=2000000;i++)
	{
		C[i].FillCircular(i);
	}


	int T;
	fscanf(inFP,"%d",&T);

	for(int t=1;t<=T;t++)
	{
		int A,B;
		fscanf(inFP,"%d",&A);
		fscanf(inFP,"%d",&B);
		int count = 0;
		for(int i=A;i<=B;i++)
		{
			for(int j=0;j<C[i].count;j++)
			{
				if(C[i].num[j]<=B)
				{
					count++;
				}
			}
		}
		fprintf(outFP,"Case #%d: %d\n",t,count);
	}


	delete[] C;
	fclose(inFP);
	fclose(outFP);
	return 0;
}
