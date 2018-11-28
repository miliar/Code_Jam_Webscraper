
/* Automatic counting */
# include <iostream>
# include <cstdio>
# include<cmath>

const int size=10;
using namespace std;
int main()
{

FILE * pfile;
FILE * ofile;
pfile = fopen ("data3" , "r");
ofile = fopen ("output3" , "w");
int T,R,k,N,mon;
int g[size],nos[size],ppl[size];
fscanf(pfile, "%d", &T);
for(int j=0;j<T;j++)
{
 mon=0;
 fscanf(pfile, "%d", &R);
 fscanf(pfile, "%d", &k);
 fscanf(pfile, "%d", &N);
 for(int i=0;i<N;i++)
 {
 fscanf(pfile, "%d", &g[i]);
 nos[i]=0;
 ppl[i]=0;
 }

for(int i=0;i<N;i++)
{
int t=g[i];
int l=0; 
while(t<=k&&(l<N))
{
l++;
ppl[i]=t;
t=t+g[((i+l)%N)];
}
nos[i]=l; 
}
int index=0;
for(int i=0;i<R;i++)
{
mon=mon+ppl[index];
index=((index+nos[index])%N);
}
fprintf(ofile,"Case #%d: %d\n",j+1,mon);
}

fclose(pfile);
fclose(ofile);
return 0;
}


