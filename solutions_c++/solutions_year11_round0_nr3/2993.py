#include "iostream"
#include "fstream"
#include "string"
using namespace std;
int main()
{
	ifstream is;
	ofstream ost;
	
	//is.open("test");
	is.open("C-small-attempt1.in");
	//is.open("C-large.in");
	ost.open("output");
	
	int T, N;
	
	is>>T;
	for(int rc=1; rc<=T; rc++)
	{
		unsigned long arr[1000];
		unsigned long xa, xb, a, b;
		unsigned long tval, res = 0;
		
		is>>N;
		
		for(int i=0; i<N; i++) { is>>arr[i]; }
		
		for(int x=0; x<N; x++)
		{
			for(int i=0; i<N; i++)
			{
				xa=a=0;
				for(int j=i; j>0; j--)
				{
					xa = xa ^ arr[j];
					a = a + arr[j];
					
					xb=b=0;
					for(int k=i+1; k<N; k++) { xb = xb ^ arr[k]; b = b + arr[k]; }
					for(int k=j-1; k>=0; k--) { xb = xb ^ arr[k]; b = b + arr[k]; }
					
					if(xa == xb) { tval = (a>b?a:b); res = (res>tval?res:tval); }				
				}			
			}	
			int z=0;
			unsigned long v = arr[0];
			for(z=0; z<N-1; z++)
				arr[z] = arr[z+1];
			arr[z] = v;
		}
			
		if(res > 0)
		{
			cout<<"Case #"<<rc<<": "<<res<<endl;
			ost<<"Case #"<<rc<<": "<<res<<endl;
		}
		else
		{
			cout<<"Case #"<<rc<<": NO"<<endl;
			ost<<"Case #"<<rc<<": NO"<<endl;
		}
	}
	
	ost.flush();

	is.close();
	ost.close();
	
	return 0;
}