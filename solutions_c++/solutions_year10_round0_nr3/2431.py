#include<stdio.h>
#include<stdlib.h>
int main()
{
FILE *f1, *f2;
int test, r, k, n, g[15];
int i, j, sum, sum1, cnt;
f1=fopen("theme.in","r");
f2=fopen("theme.out","w+");
if(f1==NULL)
   printf("\nFILE CAN'T BE OPENED");
else {
while(test!=EOF){
fscanf(f1, "%d", &test);
int c=test;
if(test==EOF)
  exit(1);

while(test-- > 0){
fscanf(f1, "%d", &r);
fscanf(f1, "%d", &k);
fscanf(f1, "%d", &n);
for(i=0;i<n;i++)
   fscanf(f1, "%d", &g[i]);
sum=0;j=0;
for(i=0;i<r;i++)
   {
   sum1=0; cnt=0;         
   while(sum1<=k && cnt<=n){
     j%=n;
     sum1+=g[j];
     cnt++;
     if(sum1<=k && cnt<=n)
        j++;
     }
   sum1-=g[j];
   sum+=sum1;
   }
fprintf(f2, "Case #%d: %d\n", c-test, sum);
}

}}
fclose(f1);
fclose(f2);
return(0);
}
