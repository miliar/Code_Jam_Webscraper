#include <stdio.h>
#include <string.h>
#include <fstream>>
#include <math.h>



FILE *istream,*ostream;
int i,j,w,o,yp,y;
unsigned long int n,k;
char a[4];



int main()
{
istream=fopen("B-small.in","r");
ostream=fopen("B-small.out","w");


fscanf(istream,"%d\n",&w);
for(j=1;j<=w;j++)
{
fscanf(istream,"%d %d",&n,&k);
if (k % int(pow(2.0,double(n))) == pow(2.0,double(n))-1) strcpy(a,"ON"); else strcpy(a,"OFF");

fprintf(ostream,"Case #%d: %s\n",j,a);
}

fclose(istream);
fclose(ostream);

return 0;
}
