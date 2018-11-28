#include <stdio.h>
#include <string.h>
#include <windows.h>
#include <algorithm>
#include <vector>

using namespace std;


int Cases;
int buff[1000];
int x;
int N;
int F;
main () {
	FILE *fin  = fopen ("in.in", "r");
	FILE *fout = fopen ("out.out", "w");

fscanf( fin, " %d", &Cases);
for (int i = 0; i < Cases; i++) {

ZeroMemory(buff,1000);
x=0;
F=0;
fscanf( fin, " %d", &N);
for (int i=0; i < N; i++) {
fscanf( fin, " %d", &buff[i]);
x^=buff[i];
}
if (x!=0) {
fprintf (fout, "Case #%d: NO\n",i+1);
}
else
{
	sort(buff,buff+N);
	for (int i = 1; i < N; i++) {
       F+=buff[i];
	}
	fprintf (fout, "Case #%d: %d\n",i+1,F);
}
}
	return 0;
}

