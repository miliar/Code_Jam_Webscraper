#include<iostream>
#include<fstream>
#include<string>
#include <cstdlib>

using namespace std;

string B_FILE_NAME = "B-small-attempt1";

void fb(string& s, int rt, char c) {
	s[4]+=rt;
	if(s[4]>'9')
	{
		s[4]-=10;
		++s[3];
		if(s[3]>'9')
		{
			s[3]+=10;
			++s[1];
			if(s[1]>'9')
			{
				s[1]-=10;
				++s[0];
			}
		}
	}
	s += c;
}

void sort(string a[], const int b)
{
	for(int i=b-1; i>=0; --i)
	{
		for(int j=i;j<b-1; ++j)
		{
			if(a[j] > a[j+1])
			{
				string temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
			}
		}
	}
}

int main()
{
	string FileIn = "D:/" + B_FILE_NAME + ".in";
	string FileOut = "D:/" + B_FILE_NAME + ".out";
	ifstream infile(FileIn.c_str());
	int n;
	infile >> n;

	ofstream outfile(FileOut.c_str());
	for(int i=0; i<n; ++i)
	{
		// gets input
		int rt;
		infile >> rt;
		int a, b;
		infile >> a;
		infile >> b;
		string *at = new string[a+b];
		string *bt = new string[a+b];
		for(int j=0; j<a; ++j)
		{
			infile >> at[j];
			fb(at[j],0,'d');
			infile >> bt[j];
			fb(bt[j],rt,'a');
		}
		for(int j=a; j<a+b; ++j)
		{
			infile >> bt[j];
			fb(bt[j],0,'d');
			infile >> at[j];
			fb(at[j],rt,'a');
		}
		sort(at,a+b);
		sort(bt,a+b);
		int ca = 0;
		int cb = 0;
		int resa = 0;
		int resb = 0;
		for(int j=0; j<a+b; ++j)
		{
			if(at[j][5] == 'a')
			{
				--ca;
			}
			else
			{
				++ca;
				if(ca > resa)
				{
					resa = ca;
				}
			}
		}
		for(int j=0; j<a+b; ++j)
		{
			if(bt[j][5] == 'a')
			{
				--cb;
			}
			else
			{
				++cb;
				if(cb > resb)
				{
					resb = cb;
				}
			}
		}
		outfile << "Case #" << (i+1) << ": " << resa << " " << resb << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
