#include <iostream>
using namespace std;
#include <fstream>
using std::ifstream;
using std::ofstream;

int mod(int a)
{
 if(a<0)
  return (-1)*a;
 else
  return a;
}

int main()
{
    ifstream indata;
    indata.open("A-large.in");
    ofstream outdata;
	int t;
    indata>>t;
	int o[t];
	for(int i=1; i<=t; i++)
	{
     o[i]=0;
     int n,o_p=1,b_p=1,o_m=0,b_m=0,p;
     char c;
     indata>>n;
     for(int j=1; j<=n; j++)
     {
      indata>>c;
      indata>>p;
      if(c=='O')
      {
       if((mod(p-o_p)+1)>b_m)
       {
        o_m=o_m+mod(p-o_p)+1-b_m;
        o[i]=o[i]+mod(p-o_p)+1-b_m;
       }
       else
       {
        o_m=o_m+1;
        o[i]=o[i]+1;
       }
       o_p=p;
       b_m=0;
      }
      else if(c=='B')
      {
       if((mod(p-b_p)+1)>o_m)
       {
        b_m=b_m+mod(p-b_p)+1-o_m;
        o[i]=o[i]+mod(p-b_p)+1-o_m;
       }
       else
       {
        b_m=b_m+1;
        o[i]=o[i]+1;
       }
       b_p=p;
       o_m=0;
      }
     }
    }
    indata.close();
    outdata.open("A-large.txt");
    for(int i=1; i<=t; i++)
     outdata<<"Case #"<<i<<": "<<o[i]<<"\n";
    outdata.close(); 
}
