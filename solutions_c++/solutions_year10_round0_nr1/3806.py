#include <iostream>
using namespace std;
int t,n,k,i=1;
int ok()
{
   if(  (k%(1<<(n)))==((1<<(n))-1)   )
     return 1;
else return 0;

}

int main()
{
FILE * f1=fopen("1.in","r");
FILE * f2=fopen("1.out","w");
fscanf(f1,"%d",&t);
while(i<=t)
{
    fscanf(f1,"%d%d",&n,&k);
    fprintf(f2,"Case #%d: %s\n",i,ok()?"ON":"OFF");
    i++;
}
fclose(f1);
fclose(f2);
return 0;
}
