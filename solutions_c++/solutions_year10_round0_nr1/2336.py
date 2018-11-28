#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
#include <iostream>

using namespace std;

int main()
{
  int i;
  int T, N;
  long int K;
  
  char filename[32]="A-large";
  cout<<filename<<endl;
  
  char infile[32], outfile[32];
  strcpy(infile, filename); strcpy(outfile, filename);
  strcat(infile, ".in"); strcat(outfile, ".out");
  FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
  
  fscanf(fp, "%d", &T);
  cout<<"T="<<T<<endl; 
 
  long int pow2N;
  for(i=1;i<=T;i++) 
    {
 
      fscanf(fp, "%d%ld", &N, &K);
      pow2N=1<<N;
      //      if ((K%(pow(2,N)))==(pow(2,N)-1))
      if (K%pow2N==(pow2N-1))
	fprintf(ofp, "Case #%d: ON\n", i);
      else
	fprintf(ofp, "Case #%d: OFF\n", i);
    }
  
  fclose(fp);
  fclose(ofp);

  return 0;
}
