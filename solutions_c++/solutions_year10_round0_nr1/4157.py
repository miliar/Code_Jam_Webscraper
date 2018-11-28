#include <fstream>
#include <algorithm>
#include <iostream>
#include <stdio.h>

using namespace std;
int main(){
   FILE *inf = fopen("F:\Delphi/A-large.in", "r");
   FILE *outf = fopen("F:\Delphi/output.txt", "w");
       int n,m,t,i;
       fscanf(inf, "%d", &t);
	   for (i=1; i<=t; i++) {
			fscanf(inf, "%d %d",&n,&m);
			int p;
			p = (1 << n);
            int q = (m % p);
			if (q==(p-1)) 
			 fprintf(outf, "%s%d%s\n", "Case #",i,": ON");
			else fprintf(outf, "%s%d%s\n", "Case #",i,": OFF");
	   }
   fclose(inf);
   fclose(outf);
  return 0;

} 