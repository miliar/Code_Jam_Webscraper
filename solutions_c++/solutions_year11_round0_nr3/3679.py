//---------------------------------------------------------------------------

#pragma hdrstop
#include <stdio.h>
#include <iso646.h>
#include <tchar.h>
//---------------------------------------------------------------------------

#pragma argsused
int _tmain(int argc, _TCHAR* argv[])
{
FILE *fin;
FILE *fout;
int i,j,s,min,summ;
int T;
int N;
int c[1200];

fin=fopen("C-large.in","rt");
fout=fopen("b.txt","wt");

fscanf(fin,"%d",&T);
for (i = 0; i < T; i++) {
s=0;
summ=0;
min=100000000;
fscanf(fin,"%d",&N);
for (j = 0; j < N; j++) {
fscanf(fin,"%d",&c[j]);
summ+=c[j];
if (c[j]<min) {
min=c[j];
}
}
for (j = 0; j < N; j++) {
s=s xor c[j];
}
if (s==0)
{
fprintf(fout,"%s","Case #");
fprintf(fout,"%d: ",i+1);
fprintf(fout,"%d\n",summ-min);
}
else
{
fprintf(fout,"%s","Case #");
fprintf(fout,"%d: NO\n",i+1);
}
}


fclose(fin);


fclose(fout);
}
//---------------------------------------------------------------------------
