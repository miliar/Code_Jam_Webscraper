
/* Automatic counting */
# include <iostream>
# include <cstdio>
# include<cmath>
using namespace std;
double rem(double a,double b)
{
return a-b*( (int) a/b);
}
long int gcd(long int a,long int b)
{
if(a<0)
{a=-a;}
if(b<0)
{b=-b;}
long int r2=a;
long int r1=b;
long int c;
if(b<a)
{
r2=b;
r1=a;
}
while(r2>0)
{
c=r2;
r2=(r1%r2);
r1=c;
}
return r1;
}
int main()
{

FILE * pfile;
FILE * ofile;
pfile = fopen ("data2" , "r");
ofile = fopen ("output2" , "w");
int C,N;
long int T,min,t;
fscanf(pfile, "%d", &C);
for(int j=0;j<C;j++)
{
 fscanf(pfile, "%d", &N);
 T=0;
 for(int i=0;i<N;i++)
 {
 fscanf(pfile, "%ld", &t);

 if(i==0){min=t;}
 else
 {
 T=gcd(T,t-min);
 if(t<min)
 {min=t;}
  }

  }
 min=min%T; 
if(min>0){ min=T-min;}
fprintf(ofile,"Case #%d: %ld \n",j+1,min);
}

fclose(pfile);
fclose(ofile);
return 0;
}


