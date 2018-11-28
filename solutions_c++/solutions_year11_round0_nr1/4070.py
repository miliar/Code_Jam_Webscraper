#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <algorithm>
#include <vector>
using namespace std;

int o;
int b;
int N;
int Cases;


int F;
int s;
char r;
int q;
int T;

char c;
int u;
main () {
	FILE *fin  = fopen ("in.in", "r");
	FILE *fout = fopen ("out.out", "w");

fscanf( fin, " %d", &Cases);
for (int i = 0; i < Cases; i++) {

o=1;
b=1;
F=0;
r=0;
T=0;
fscanf( fin, " %d", &N);
for (int i = 0; i < N; i++) {
int j;


fscanf( fin, " %s", &c);
if (c=='O') {
 fscanf( fin, " %d", &j);
 if (c==r) {
 T+=abs(o-j)+1;
 F+=abs(o-j)+1;

 }
 else
 {
 T-=abs(o-j);
   if (T<0) {
	  T=abs(T)+1;
	  F+=T;
   }
   else
   {
	   F++;
	   T=1;
   }
 }
 r=c;
 o=j;
}
else
{
 fscanf( fin, " %d", &j);
 if (c==r) {
 T+=abs(b-j)+1;
 F+=abs(b-j)+1;

 }
 else
 {
   T-=abs(b-j);
	  if (T<0) {
	  T=abs(T)+1;
	  F+=T;
   }
   else
   {
	   F++;
       T=1;
   }
 }
 r=c;
 b=j;

}
}
fprintf (fout, "Case #%d: %d\n",i+1,F);
}
	return 0;
}


