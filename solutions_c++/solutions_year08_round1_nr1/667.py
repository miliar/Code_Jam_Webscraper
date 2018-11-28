#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <deque>
using namespace std;

#define Max(a, b) (a > b ? a : b)
#define Min(a, b) (a < b ? a : b)

int CreatePermutation(int n, int *permutaion, int *state)
{
	int i=0,j;
	int temp;

	while(state[i]==i+1)
	{
		temp=*permutaion;
		for(j=0;j<=i;j++)
			permutaion[j]=permutaion[j+1];
		permutaion[i+1]=temp;
		state[i]=0;
		i++;
	}

	if(i==n-1)
		return 0;

	temp=*permutaion;
	for(j=0;j<=i;j++)
		permutaion[j]=permutaion[j+1];
	permutaion[i+1]=temp;
	state[i]++;
	return 1;
}

int Scalar(int* x, int* y, int *index, int n)
{
	int sum = 0;
	for(int i = 0; i < n; i++)
		sum += x[i] * y[index[i]];
	return sum;
}

int Smallest(int* x, int* y, int n)
{
	int * state = new int [n];
	int * perm = new int[n];
	for(int i = 0; i < n; i++)
	{
		perm[i] = i;
		state[i] = 0;
	}

	int scalmin = Scalar(x, y, perm, n);
	int scal;

	while(CreatePermutation(n, perm, state))
	{
		scal = Scalar(x, y, perm, n);
		if(scal < scalmin)
			scalmin = scal;
	}
	delete[] state;
	delete[] perm;
	return scalmin;
}

int main(int argc, char ** argv)
{
	int ncases;
	int *x = new int[800];
	int *y = new int[800];
	int n;

	int scal;

	FILE* fpin, * fpout;


	if(argc < 3)
	{
		printf("Requires in and out filename!\n");
		return 0;
	}

	fpin = fopen(argv[1], "r");
	fpout = fopen(argv[2], "w");

	fscanf(fpin, "%d", &ncases);
	for(int i = 0; i < ncases; i++)
	{
		fscanf(fpin, "%d", &n);
		for(int j = 0; j < n; j++)
			fscanf(fpin, "%d", x + j);
		for(int j = 0; j < n; j++)
			fscanf(fpin, "%d", y + j);
		scal = Smallest(x, y, n);
		fprintf(fpout, "Case #%d: %d\n", i + 1, scal);
	}



	fclose(fpin);
	fclose(fpout);


	return 0;
}

