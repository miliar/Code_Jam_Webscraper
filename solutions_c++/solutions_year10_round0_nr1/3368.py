#include <iostream>
#include <math.h>

using namespace std;

void main()
{
  FILE *in  = fopen("big.in","r");
  FILE *out = fopen("big.out","w");

  int T, N;
	long K;
	int c = 1;
  fscanf(in,"%d",&T);
  while (T--)
  {
		fscanf(in,"%d",&N);
		fscanf(in,"%d",&K);
		fprintf(out,"Case #%d: %s\n",c++,((K+1) % (int)pow(2.0,N) == 0) ? "ON" : "OFF");
	 } 
}