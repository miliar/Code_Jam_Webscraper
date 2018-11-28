

#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;

int main()
{
	int n,x,y,i=1;
	fstream f;
	ofstream g;
	f.open("input.txt", ios::in);
	g.open("output.txt",ios::in);
	f>>n;
	while(n!=0)
	{
		f>>x; f>>y;
		float z;
		z=(y+1)/(pow(double(2),x));
		if(z==int(z))
			g<<"Case #"<<i<<":"<<" ON"<<endl;
			else
				g<<"Case #"<<i<<":"<<" OFF"<<endl;
		n--; i++;
	}
	f.close();
	g.close();
	return 0;
	}