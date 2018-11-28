#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
	
int main()
{
	ifstream f;
	f.open("C-small-attempt0.in.in");
	int tc;
	f >> tc;
	for(int i=0; i<tc; i++)
	{
		int N;
		f >> N;
		int candy[N];
		for(int j=0; j<N; j++)
		{
			f >> candy[j];
		}

		int seangets=0;
		for(int k=1; k<pow(2,N)-1; k++)
		{
			int sean=0, patrick=0, seanr=0;
			for(int l=0; l<N; l++)
			{
				if(k & 1<<l)
					sean ^= candy[l], seanr+=candy[l];
				else
					patrick ^= candy[l];
			}
			if(sean == patrick && seanr > seangets)
			{
				seangets = seanr;
			}
		}

		cout << "Case #" << i+1 << ": ";
		if(seangets)
			cout << seangets;
		else
			cout << "NO";

		cout << endl;
	}
}

