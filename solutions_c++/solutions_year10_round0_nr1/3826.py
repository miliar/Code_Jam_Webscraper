#include <stdio.h>
#include<fstream.h>
#include<string.h>
#include<conio.h>
#include<math.h>

int main(int argc, char *argv[])
{
	int N,i=1,d,j,q;
	double long T;
	long int K;
	ifstream f1("A-large.in");
	f1>>T;
	ofstream f2("A-largeanswer.in");
	for(i;i<=T;i++)
	{
		f1>>N>>K;
		if(N==1 && (K%2!=0))
		{
			d=1;
		}
		else
		{
		q = pow (2,N);
		if(q-1>K)
		{
		d=0;
		}
		else
		{
			j=(K%q);
			if((q-1)==j)
			d=1;
			else
			d=0;
		}
		}
		f2<<"Case #"<<i<<": "<<(d?"ON":"OFF")<<endl;
		
	}
f1.close();
f2.close();
	return 0;
}
