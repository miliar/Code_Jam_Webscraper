#include <iostream>
#include <fstream>
#include <cmath>
#include <sstream>



using namespace std;

ifstream ifs ("A-large.in", ifstream::in);
ofstream ofs ("A-large.out", ofstream::out|ofstream::trunc);

long unsigned int getnextnumb()
{
	char c[256];
	int i=0;
	c[0]=ifs.get();
    do
	{
		i++;
		c[i]=ifs.get();
	}
	while ((c[i]!='\n')&&(c[i]!=' ')&&(c[i]!=EOF));
	long unsigned int number=0;
	std::string conv(c,i);
	std::istringstream ss( conv );
	ss >> number;
	return number;
}

bool onOrOff (unsigned long int Nf, unsigned long int Kf)
{
	for(unsigned short int l=0;l<Nf;l++)
	{
		if (!(Kf&0x1)) return 0;
		Kf>>=1;
	}
	return 1;
}

int main(int argc, char *argv[])
{
	const unsigned long int T=getnextnumb();
	unsigned long int N,K;
	for (unsigned long int i=0;i<T;i++)
	{
		N=getnextnumb();
		K=getnextnumb();
		ofs.write("Case #",6);
		std::string s;
		std::stringstream out;
		out << (i+1);
		s = out.str();
		ofs.write(s.c_str(),s.length());
		ofs.put(':');
		ofs.put(' ');
		if (onOrOff(N,K)) ofs.write("ON",2);
		else ofs.write("OFF",3);
		ofs.put('\n');
	}
	system("pause");
	return 0;
}	