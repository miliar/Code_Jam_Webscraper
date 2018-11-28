#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, char** argv)
{
	ifstream entrada("C-small-attempt0.in");
	ofstream salida("Output1.in");
	int t,r,k,n;
	entrada>>t;
	
	for(int i=0;i<t;i++)
	{
		entrada>>r>>k>>n;
		int matriz[n];
		
		for (int j=0;j<n;j++)
		{
			entrada>>matriz[j];
			}

		int total=0;
		int czo=0;
		for(int j=0;j<r;j++)
		{
          for(int h=0,f=0;(h+matriz[czo])<=k && f<n ;f++)
          {
			  h=h+matriz[czo];
			  total+=matriz[czo];
			  czo=(czo+1)%n;
			  
			  }
         }
		salida<<"Case #"<<i+1<<": "<<total<<endl;
	}

	return 0;
}
