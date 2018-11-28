#include <fstream>
#include <iostream>

using namespace std;

ifstream in;
ofstream out;

string str[102];
int n;

double oowp(int t);
double owp(int t);
double wp(int t);
double wp2(int from, int to);
double rpi(int t);

void work()
{
	in>>n;
	for (int i = 0; i < n; i++)
	{
		string tmp;
		in>>tmp;
		str[i] = tmp;
	}
	for (int i = 0; i < n; i++)
	{
		out<<rpi(i)<<endl;
	}
}
int main()
{
	in.open("small.in");
	out.open("small.out");
	int t;
	in>>t;
	for (int i = 0; i < t; i++)
	{
		out<<"Case #"<<i + 1<<":"<<endl;
		work();
	}
	in.close();
	out.close();
	return 0;
}

double oowp(int t)
{
	double res = 0.0;
	int size = 0;
	for (int i = 0; i < n; i++)
	{
		if (i == t) continue;
		if (str[t][i] != '.')
		{
			size += 1;
			res += owp(i);
		}
	}
	return res / size;
}
double owp(int t)
{
	double res = 0.0;
	int size = 0;
	for (int i = 0; i < n; i++)
	{
		if (i == t) continue;
		if (str[t][i] != '.')
		{
			res += wp2(i,t);
			size += 1;
		}
	}
	return res / size;
}

double wp2(int from, int to)
{
	double res = 0.0;
	int size = 0;
	for (int i = 0; i < n; i++)
	{
		if (i == from || i == to)
			continue;
		if (str[from][i] == '1')
			res += 1.0;
		if (str[from][i] != '.')
			size += 1;
	}
	return res / size;
}

double wp (int t)
{
	double res = 0.0;
	int size = 0;
	for (int i = 0; i < n; i++)
	{
		if (i == t)
			continue;
		if (str[t][i] == '1')
			res += 1.0;
		if (str[t][i] != '.')
			size += 1;
	}
	return res / size;
}

double rpi(int t)
{
	/*
	cout<<"box"<<endl;
	cout<<wp(t)<<endl;
	cout<<owp(t)<<endl;
	cout<<oowp(t)<<endl;
	*/
	return 0.25 * wp(t) + 0.5 * owp(t) + 0.25 * oowp(t);
}


