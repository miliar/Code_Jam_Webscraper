#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

ifstream ifs ("A-small.in", ifstream::in);
ofstream ofs ("A-small.out", ofstream::out|ofstream::trunc);

int T,N;

struct rope
{
	int start;
	int end;
};

int getNextNumb()
{
	char c[16];
	int i=0;
	c[0]=ifs.get();
    do
	{
		i++;
		c[i]=ifs.get();
	}
	while ((c[i]!='\n')&&(c[i]!=' ')&&(c[i]!=EOF));
	int number=0;
	std::string conv(c,i);
	std::istringstream ss( conv );
	ss >> number;
	return number;
}


double calcInt(rope arr[],int n)
{
	double res=0;
	for (int k=0;k<n;k++)
	{
		if (((arr[k].start-arr[n].start)*(arr[k].end-arr[n].end))<0) {res++;}
	}
	return res;
}

int main ()
{
	T=getNextNumb();
	for(int j=0;j<T;j++)
	{
		N=getNextNumb();
		double inter=0;
		rope *arrRp = new rope[N];
		for(int i=0;i<N;i++)
		{
			arrRp[i].start=getNextNumb();
			arrRp[i].end=getNextNumb();
			inter+=calcInt(arrRp,i);
		}
		ofs.write("Case #",6);
		string s;
		stringstream out;
		out << (j+1);
		s = out.str();
		ofs.write(s.c_str(),s.length());
		ofs.put(':');
		ofs.put(' ');

		string s2;
		stringstream out2;
		out2 << (inter);
		s2 = out2.str();
		ofs.write(s2.c_str(),s2.length());

		ofs.put('\n');
	}
	system("pause");
	return 0;
}
