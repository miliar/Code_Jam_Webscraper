
/* Automatic counting */
# include <iostream>
# include <cstdio>
# include<cmath>
using namespace std;

int main()
{
FILE * pfile;
FILE * ofile;
bool b;
pfile = fopen ("data" , "r");
ofile = fopen ("output" , "w");
unsigned int N,K,T,p;
fscanf(pfile, "%d", &T);
for(int i=0;i<T;i++)
{
fscanf(pfile, "%d", &N);
fscanf(pfile, "%d", &K);
p=(int)pow(2,N);
K=(K%p);
if(K==(p-1))
{
fprintf(ofile,"Case #%d: ON \n",i+1);
}
else
{
fprintf(ofile,"Case #%d: OFF \n",i+1);
}

}
fclose(pfile);
fclose(ofile);
return 0;


}
