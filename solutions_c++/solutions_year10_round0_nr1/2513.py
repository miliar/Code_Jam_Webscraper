#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
FILE *f1, *f2;
int test, n;
long int k;
f1=fopen("snapr.in","r");
f2=fopen("snapr.out","w+");
if(f1==NULL)
   printf("\nFILE CAN'T BE OPENED");
else {
while(test!=EOF){
fscanf(f1, "%d", &test);
int c=test;
if(test==EOF)
  exit(1);

while(test-- > 0){
fscanf(f1, "%d", &n);
fscanf(f1, "%ld", &k);
long int num = pow(2,n);
if((k+1)% num==0)
  fprintf(f2, "Case #%d: ON\n", c-test);
else
  fprintf(f2, "Case #%d: OFF\n", c-test);
}

}}
fclose(f1);
fclose(f2);
return(0);
}
