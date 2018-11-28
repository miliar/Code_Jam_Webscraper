#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	int N;
	int Pd;
	int Pg;
	int Dall;
	ifstream fin;
	ofstream fout;
	fin.open("A-small.in");
	fout.open("Asmall-answer.txt");
	fin>>T;
	for (int i=1;i<=T;i++)
	{
		fin>>N;
		fin>>Pd;
		fin>>Pg;
		if (Pg==0)
		{
			if (Pd!=0)
			{
				fout<<"Case #"<<i<<": Broken"<<endl;
				continue;
			}
			else
			{
				fout<<"Case #"<<i<<": Possible"<<endl;
				continue;
			}

		}

		if (Pg==100)
		{
			if (Pd!=100)
			{
				fout<<"Case #"<<i<<": Broken"<<endl;
				continue;
			}
			else
			{
				fout<<"Case #"<<i<<": Possible"<<endl;
				continue;
			}

		}

		Dall=100;
		if (Pd%2==0)
		{
			Pd=Pd/2;
			Dall=Dall/2;
		}

		if (Pd%2==0)
		{
			Pd=Pd/2;
			Dall=Dall/2;
		}

		if (Pd%5==0)
		{
			Pd=Pd/5;
			Dall=Dall/5;
		}

		if (Pd%5==0)
		{
			Pd=Pd/5;
			Dall=Dall/5;
		}

		if (Dall<=N)
		{
			fout<<"Case #"<<i<<": Possible"<<endl;
		}
		else
		{
			fout<<"Case #"<<i<<": Broken"<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}