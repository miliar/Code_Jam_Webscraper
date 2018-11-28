#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
using namespace std;

int calulate(const char* stra,const int lena,const char* strb,const int lenb)
{
	int res = 0;
	int occur = 0;

	if (lenb <= 0)
	{
		return 1;
	}
	else if (lenb == 1)
	{
		for (int i = 0; i < lena; i++)
		{
			if (stra[i] == strb[0])
			{
				res++;
			}
		}

		return res;
	}

	if (lena < lenb)
	{
		return 0;
	}
	else if (lena == lenb)
	{
		for (int i = 0; i < lena; i++)
		{
			if (stra[i] != strb[i])
			{
				return 0;
			}
		}
		return 1;
	}

	// now lenb is at least 2 and lena > lenb

	for (int i = 0; i <= lena - lenb + 1; i++)
	{
		if (stra[i] == strb[0])
		{
			res += calulate(stra + i + 1,lena - i - 1,strb + 1,lenb - 1);
		}
	}

	return res;
}

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int n;
	fin >> n;
	fin.get();

	const char* compare_str = "welcome to code jam";
	int compare_len = 19;

	for (int order = 1; order <= n; order++)
	{
		char buf[501];

		fin.getline(buf,501);
/*
		ch = fin.get();
		while (ch != '\n' && (!fin.eof()))
		{
			temp += ch;
			ch = fin.get();
		}*/


		int res = calulate(buf,strlen(buf),compare_str,compare_len);

		char outcome[4];

		for (int i = 0; i < 4; i++)
		{
			outcome[4 - i - 1] = (res % 10) + '0';
			res /= 10;
		}

		fout << "Case #" << order << ": " << outcome[0] << outcome[1] << outcome[2] << outcome[3] << endl;
	}

	fout.close();
	fin.close();

	return 0;
}