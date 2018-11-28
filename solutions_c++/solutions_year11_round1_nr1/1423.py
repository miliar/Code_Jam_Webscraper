// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <map>
#include <vector>
#include <math.h>

using namespace std;

//#define INPUT_FILE "large_input.txt"
#define INPUT_FILE "small_input.txt"
//#define INPUT_FILE "in.txt"
#define OUTPUT_FILE "output.txt"

#define MAX_M 512
#define MAX_N 512

using namespace std;

map< int, int, greater<int> > chessmap;
vector<int> vec;
vector<int> vecCol;

FILE *fp;
FILE *fpout;

int get();

int main(int argc, char* argv[])
{
	fp = fopen(INPUT_FILE, "r");

	if(!fp) 
	{
		printf("Error : file input\n");
		return 0;
	}

	fpout = fopen(OUTPUT_FILE, "w");

	if(!fpout)
	{
		printf("Error : file output\n");
		return 0;
	}

	int T;	// num of test cases
	fscanf(fp, "%d", &T);

	int i;
	int ok;
	for(i=0; i<T; i++)
	{
		ok = get();
		//printf("%d\n", i);

		if(ok == 1)
			fprintf(fpout, "Case #%d: Possible\n", i+1);
		else
			fprintf(fpout, "Case #%d: Broken\n", i+1);
	}

	fclose(fp);
	fclose(fpout);

	return 0;
}

int get()
{
	int N, Pd, Pg;
	fscanf(fp, "%d %d %d\n", &N, &Pd, &Pg);

	int possible = 0;

	if(Pg == 100 && Pd != 100)
	{
		return 0;
	}

	if(Pg == 0 && Pd != 0)
	{
		return 0;
	}

	int i;
	long val;
	for(i=0; i<N; i++)
	{
		val = (i+1) * Pd;
		if(val % 100 == 0) {
			// i <- game¼ö
			// val / 100 <- 
			return 1;
		}
	}

	return possible;
}

long gcd(long a, long b) {

  while (b != 0) {
    int temp = a % b;
    a = b;
    b = temp;
  }

  return abs(a);
}