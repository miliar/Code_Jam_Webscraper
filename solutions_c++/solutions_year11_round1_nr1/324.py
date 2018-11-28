#include <fstream>
#include <iostream>

using namespace std;

fstream fin, fout;

void process()
{
	long long n;
	int pd, pg;

	fin >> n >> pd >> pg;
	if (pd == 100 && pg == 100)
	{
		fout << "Possible";
		return ;
	}

	if (pd == 100 && pg != 0)
	{
		fout << "Possible";
		return ;
	}

	if (pd == 100 && pg == 0)
	{
		fout << "Broken";
		return ;
	}

	if (pg == 100 && pd != 0)
	{
		fout << "Broken";
		return;
	}

	if (pg == 100 && pd == 0)
	{
		fout << "Broken";
		return;
	}

	if (pd == 0 && pg == 0)
	{
		fout << "Possible";
		return;
	}

	if (pd == 0 && pg != 0)
	{
		fout << "Possible";
		return;
	}

	if (pd != 0 && pg == 0)
	{
		fout << "Broken";
		return;
	}

	int a = 0;
	int b = 0;
	for (int i = 0; i < 2; ++i)
		if (pd % 2 == 0)
		{
			pd /= 2;
			a++;
		}
	for (int i = 0; i < 2; ++i)
		if (pd % 5 == 0)
		{
			pd /= 5;
			b++;
		}
	int temp = 1;
	for (int i = a; i < 2; ++i)
		temp *= 2;
	for (int i = b; i < 2; ++i)
		temp *= 5;
	if (temp > n)
		fout << "Broken";
	else
		fout << "Possible";
}

int main()
{
	fin.open("in.txt", fstream::in);
	fout.open("out.txt", fstream::out);

	int testcase;
	fin >> testcase;
	for (int i = 1; i <= testcase; ++i)
	{
		fout << "Case #" << i << ": ";
		process();
		fout << endl;
	}

	fin.close();
	fout.close();
	return 0;
}
