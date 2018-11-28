#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>



int check(int *v, int n);
void stringToIntArray(char *s, int *v, int n);


void stringToIntArray(char *s, int *v, int n)
{
  int iv, is, in;
  char num[6];
  in=0;
  iv=0;
  for(is=0 ; iv<n ; is++)
  {
	 if(s[is]==32 || s[is]==NULL)
	 {
		num[in]=NULL;
		in=0;
		v[iv]=atoi(num);
		iv++;
	 }
	 else
	 {
		num[in]=s[is];
		in++;
	 }
  }
}


int check(long k, int n)
{
  int state;
  int x;
  x=pow(2,n);
  state=(k%x==x-1);
  return state;
}

void main()
{
  FILE *in, *out;
  int T, N, num[2], i, K;
  char line[20], word[3], test[6];
  in=new FILE;
  in = fopen("small.in", "r");
  out = fopen("small.out", "w");
  fgets(line, 20, in);
  T=atoi(line);
  for(i=0 ; i<T ; i++)
  {
	 fgets(line, 20, in);
	 stringToIntArray(line, num, 2);
	 N = num[0];
	 K = num[1];
	 if(check(K, N))
		strcpy(test, ": ON");
	 else
		strcpy(test, ": OFF");
	 strcpy(line, "Case #");
	 itoa(i+1, word, 10);
	 strcat(line, word);
	 strcat(line, test);
	 if(i<T-1)
		strcat(line, "\n");
	 fputs(line, out);
  }

  fclose(in);
  fclose(out);
}
