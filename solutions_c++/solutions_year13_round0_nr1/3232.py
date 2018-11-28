#include <string>
#include <math.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include <iostream>
#include <fstream>
#include <limits.h>

typedef unsigned __int64 lint; 

#define F(i,b) for(lint i=0;i<(b);i++)
#define FIAN(i,a,n) for(lint i=a;i<n;i++)
#define FIANrev(i,a,n) for(lint i=a;i>n;i--)

using namespace std;

FILE * inputFile = fopen("D:\\Downloads\\Chrome\\A-small-attempt0.in", "r");
FILE * outputFile  = fopen("D:\\Downloads\\Chrome\\output.txt", "w");

float a[4][4];
char C;
string res;
string line;
float sum;

//lint calcToysByIterator(const lint &i, const lint &j){
//	if ((i==N)||(j==M)) return 0;
//	lint res = 0;
//	if (A[i]==B[j]){
//		if (a[i] > b[j]){
//			a[i] -= b[j];
//			res += b[j] + calcToysByIterator(i,j+1);
//			a[i] += b[j];
//		}
//		if (b[j] > a[i]){
//			b[j] -= a[i];
//			res += a[i] + calcToysByIterator(i+1,j);
//			b[j] += a[i];
//		}
//		if (b[j] == a[i]){
//			res += a[i] + calcToysByIterator(i+1,j+1);
//		}
//	}
//	else{
//		res += max(calcToysByIterator(i+1,j),calcToysByIterator(i,j+1));
//	}
//	return res;
//}

void oneStep()
{
	res = "Draw";
	

	F(i,4)
	{
		fscanf(inputFile, "%c", &C);
		F(j,4)
		{
			fscanf(inputFile, "%c", &C);
			if (C == 'X')
				a[i][j] = 1.0f;
			else if (C == 'O')
				a[i][j] = 0.0f;
			else if (C == '.')
			{
				res = "Game has not completed";
				a[i][j] = -10.0f;
			}
			else if (C == 'T')
				a[i][j] = 0.5f;
		}
	}

	F(i,4)
	{
		sum = 0.0f;
		F(j,4)
		{
			sum += a[i][j];
		}
		if (sum < 1.0f && sum >= 0.0f)
			res = "O won";
		else if (sum > 3.0f)
			res = "X won";
	}

	F(j,4)
	{
		sum = 0.0f;
		F(i,4)
		{
			sum += a[i][j];
		}
		if (sum < 1.0f && sum >= 0.0f)
			res = "O won";
		else if (sum > 3.0f)
			res = "X won";
	}

	{
		sum = 0.0f;
		F(i,4)
		{
			sum += a[i][i];
		}
		if (sum < 1.0f && sum >= 0.0f)
			res = "O won";
		else if (sum > 3.0f)
			res = "X won";
	}

	{
		sum = 0.0f;
		F(i,4)
		{
			sum += a[i][3 - i];
		}
		if (sum < 1.0f && sum >= 0.0f)
			res = "O won";
		else if (sum > 3.0f)
			res = "X won";
	}

	fprintf(outputFile, "%s", res.c_str());
	fprintf(outputFile, "\n");
	
		fscanf(inputFile, "%c", &C);
}

int main()
{
	time_t timer = time(NULL);
	printf("%s\n", ctime(&timer));

	unsigned int T;
	fscanf(inputFile, "%d", &T);

	F(t,T){
		//TODO: solve here!
		fprintf(outputFile, "Case #%d: ", t+1);
		oneStep();
		timer = time(NULL);
		printf("step %d - %s\n", t, ctime(&timer));
	}

	fclose(inputFile);
	fclose(outputFile);

	timer = time(NULL);
	printf("%s\n", ctime(&timer));
	// qDebug("Time elapsed: %d ms", time1.elapsed());
	return 0;
}