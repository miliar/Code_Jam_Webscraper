#include<iostream.h>
#include<fstream.h>
#include<conio.h>

int main()
{
  long i,n,k,snap,init;
  int s,tests,t;
  char state[2][4]={"OFF","ON"},str;
  ifstream ip("ip.txt");
  ofstream op("op.txt");
  ip>>tests;
  for(t=1;t<=tests;t++)
  {
    ip>>n;
    ip>>k;
    
    init=1;
    for(i=1;i<=n;i++)
    init*=2;
    if((k+1)%init==0)
    s=1;
    else
    s=0;
    op<<"Case #"<<t<<": "<<state[s]<<endl;
  }
  return 1;
}
