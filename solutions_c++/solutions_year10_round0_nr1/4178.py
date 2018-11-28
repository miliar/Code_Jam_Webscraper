#include <stdio.h>
#include <math.h>
#include <iostream.h>
#include <fstream.h>

ifstream in("A-large-2.in");
ofstream out("A-large-2.out");

long long T;
int main (void)
{
in>>T;
int n=0; long long k=0; long long number=0; 
for (long long i=1; i<=T; i++)
{
    in>>n; in>>k;
    number=(long long)pow(2, n);
    if (k%number==(number-1)) out<<"Case #"<<i<<": ON"<<endl;
    else out<<"Case #"<<i<<": OFF"<<endl;   
}
in.close(); out.close();
return 2;    
}
