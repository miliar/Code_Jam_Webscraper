#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int findLen(int a)
{
int len = 0;
while(a)
{
a = a/10;
len++;
}
return len;
}
int main()
{
int i = 1;
int t;
int mult;
int len;
int l;
int rem;
int new_a;
int a,b;
int temp;
int count;
FILE *iFile = fopen("C-small-attempt1.in", "r");
FILE *oFile = fopen("output.txt", "w");
if (iFile == NULL) {
perror("Failed to open file \"input.txt\"");
return EXIT_FAILURE;
}
if (oFile == NULL) {
perror("Failed to open file \"output.txt\"");
return EXIT_FAILURE;
}
fscanf (iFile,"%d",&t);
while(t--)
{
fscanf(iFile,"%d %d",&a,&b);
len = findLen(a);
mult = pow(10,len-1);
count = 0;
while(a<=b)
{
l = len;
if(l > 1)
{
    temp = a;
while(l)
{
rem = temp % 10;
temp = temp/10;
new_a = mult * rem + temp;
//printf("%d ",new_a);
if(new_a > a && new_a <= b)
{
count++;
//printf("%d %d %d\n",a,new_a,b);
}
temp = new_a;
l--;
}
//puts("\n");
}
a++;
}
fprintf(oFile,"Case #%d: %d\n",i,count);

i++;
}
fclose(iFile);
fclose(oFile);
return 0;
}
