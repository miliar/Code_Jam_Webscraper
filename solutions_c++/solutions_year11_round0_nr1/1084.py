#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	int p, T, N;
	char r;
	ifstream in("input.txt");
	ofstream out("output.txt");	
	in>>T;
	for(int k=0; k<T; k++)
	{
		in>>N;
		int t=0, ot=0, bt=0, op=1, bp=1;
		for(int i=0; i<N; i++)
		{
			in>>r>>p;
			if (r=='O')
			{
				t+=max(abs(p-op)-t+ot+1,1);
				op=p;
				ot=t;
			}
			else
			{
				t+=max(abs(p-bp)-t+bt+1,1);
				bp=p;
				bt=t;
			}
		}
		out<<"Case #"<<(k+1)<<": "<<t<<endl;
	}
	return 0;
}

