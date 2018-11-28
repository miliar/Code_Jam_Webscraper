#include<iostream.h>
#include<fstream.h>
#include<vector>
#include<functional>   

typedef __int64 longint;

int main()
{
	ifstream is;
	ofstream os;
	
	is.open("A-large.in");
	os.open("outA");
	
	int t,n;
	longint k;

	is>>t;
	for(int rc=1; rc<=t; rc++)
	{
		is>>n;
		is>>k;

		int res = 1;
		longint m = 1;
		
		for(int i=0; i<n; i++)
		{
			if((k & m) == 0)
			{
				res = 0;
				break;
			}
			m = m<<1;
		}

		os<<"Case #"<<rc<<((res == 1) ? ": ON" : ": OFF")<<endl;
		//cout<<"Case #"<<rc<<((res == 1) ? ": ON" : ": OFF")<<endl;
	}

	os.flush();

	is.close();
	os.close();
	
	return 0;
}