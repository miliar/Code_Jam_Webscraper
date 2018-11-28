//---------------------------------------------------------------------------

#define SMALL 1

//---------------------------------------------------------------------------

#include <conio>
#include <stdio>
#include <string>
#include <math>

#include <vector>
#include <list>
#include <slist>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <hash_map>
#include <set>
#include <hash_set>

#include <numeric>
#include <algorithm>

using namespace std;

//---------------------------------------------------------------------------

float power(float x, int y)
{
	if (y == 0) return 1;
	float t = power(x, y / 2);
	if ((y % 2) == 0)
	{
		return t * t;
	}
	else
	{
		return t * t * x;
	}
}


unsigned int pwr(float base, unsigned int exp)
{
unsigned int result = 1;

while(exp--)
result *= base;

return result;
}
/*
float power(x, y)
{
	if (y == 0) return 1;
	long double t = power(x, y / 2);
	if ((y % 2) == 0)
	{
		return t * t;
	}
	else
	{
		return t * t * x;
	}
}

*/
//---------------------------------------------------------------------------

int main(int argc, char* argv[])
{
  int T;
  long int n;
//  char n[10];
  FILE * inFile, * outFile;

#ifdef SMALL
  inFile = fopen ("C:\\Round1A\\C-small.in","r");
  outFile = fopen ("C:\\Round1A\\C-small.out","w");
#else
  inFile = fopen ("C:\\Round1A\\C-large.in","r");
  outFile = fopen ("C:\\Round1A\\C-large.out","w");
#endif

float base = 5.2360679774997896964091736687313;
//float base = 5.23606797;//74997896964091736687313;

double cache[31];
cache[0] = 1;
printf ("%f\n", cache[0]);
for (int j = 1; j <= 30; j++) {
cache[j] = cache[j-1] * base;
printf ("%f\n", cache[j]);
}

 char char_cache[31][4] =
{
"001",
"005",
"027",
"143",
"751",
"935",
"607",
"903",
"991",
"334",
"041",
"908",
"271",
"920",
"047",
"558",
"453",
"437",
"316",
"401",
"631",
"091",
"534",
"324",
"880",
"504",
"744",
"340",
"700",
"400",
"000"
};


  if (inFile!=NULL)
  {
	fscanf (inFile, "%d", &T);
	for (int i = 1; i <= T; i++)
	{
	  fscanf (inFile, "%d", &n);
//	  float ex = n;
//	  float temp = pow(base, ex);
//	  int x = (int) temp;
//	  long int x = (((long int)pow(base, n)));
//	  x = x % 1000;
//	  fprintf(outFile, "Case #%d: %03d\n", i, (((int)pow(base, n)) % 1000));
//temp = (int) temp % 1000;
//temp = temp - (((float)((int)(temp / 1000))) * 1000);
//temp = temp - (((float)((int)(temp / 1000))) * 1000);

//int x = Int(temp);
//int x = (int) y;
//x = x % 1000;
//	  fprintf(outFile, "Case #%d: %03d\n", i, x);
//double x;
// modf(temp, &x);// - (((int) (temp / 1000)) * 1000);
//int y = (int) x;
// int x = pow(base, n);

//	  fprintf(outFile, "Case #%d: %03.0f\n", i, temp);

//	  fprintf(outFile, "Case #%d: %03d\n", i, x%1000);

	  fprintf(outFile, "Case #%d: %s\n", i, char_cache[n]);

	}

	fclose (inFile);
	fclose (outFile);
  }

  printf("Problem C Solved\n");

  getch();
  return 0;
}
//---------------------------------------------------------------------------

