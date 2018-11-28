#include <stdio.h>
#include <fstream.h>
#include <string.h>
#include <math.h>

bool Run(unsigned long n,int today,int total)
{
	unsigned long k;
	if(today == total)
		return true;
	if(today != 100 && total == 100)
		return false;
	if(today != 0 && total == 0)
		return false;
	for(k=1;k<=n;k++)
	{
		if( (k*today)%100 == 0)
		{
			for(int j = k;j<=1000;j++)
			{
				if( (j*total)%100 == 0)
					return true;
			}
		}
	}

	return false;	 
}

void main()
{
	ifstream in;
	ofstream out;

	in.open("D:\\input.in",ios::in,0);
	out.open("D:\\out.out",ios::out,0);

	int num;
	int index = 1;

	in>>num;

	while(num > 0)
	{
		num--;

		unsigned long n;
		int today,total;
		in>>n;
		in>>today;
		in>>total;
		bool b = Run(n,today,total);

		if(b)
			out<<"Case #"<<index<<": "<<"Possible"<<endl;
		else
			out<<"Case #"<<index<<": "<<"Broken"<<endl;
		index++;
	}

	in.close();
	out.close();
}




	
