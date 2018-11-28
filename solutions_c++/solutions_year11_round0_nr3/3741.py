#include<iostream>
#include<fstream>
using namespace std;

int T,N;
long long C,sum,xsum,min;
int main()
{
	ifstream in ("C.in");
	ofstream out ("C.out");
	in>>T;
	for(int t=0;t<T;t++)
	{
		sum=0;
		xsum=0;
		long long min=1000*1000+10;
		in>>N;
		for(int i=0;i<N;i++)
		{
			in>>C;
			if(C<min)
				min=C;
			sum+=C;
			xsum=xsum^C;	
		}
		out<<"Case #"<<t+1<<": ";
		if(xsum!=0)
			out<<"NO"<<endl;
		else
			out<<sum-min<<endl;
		
	}
	return 0;
}
