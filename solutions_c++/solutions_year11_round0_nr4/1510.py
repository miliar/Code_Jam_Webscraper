#include <iostream>
using namespace std;

#include <fstream>
using std::ifstream;
using std::ofstream;

int main()
{
    ifstream indata;
    ofstream outdata;
	int t;
	indata.open("D-large.in");
    indata>>t;
	int o[t];
	for(int i=1; i<=t; i++)
	{
     o[i]=0;
     int n;
     indata>>n;
     int a[n];
     for(int j=1; j<=n; j++)
     {
      indata>>a[j];
      if(j!=a[j])
       o[i]=o[i]+1;
     }
    }
    indata.close();
    outdata.open("D-large.txt");
    for(int i=1; i<=t; i++)
     outdata<<"Case #"<<i<<": "<<o[i]<<"\n";
    outdata.close(); 
}
