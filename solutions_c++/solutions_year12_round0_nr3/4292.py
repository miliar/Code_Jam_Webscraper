#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<sstream>

using namespace std;

string long_string(long);
long string_long(string);

int main()
{
	ifstream in("C-small-attempt1.in");
	ofstream out("out.txt");

	int T;
	int pair[50];
	long A[50];
	long B[50];

	for(int i = 0; i < 50; i++)
	{
		pair[i] = 0;
		A[i] = 0;
		B[i] = 0;
	}

	in	>>T;

	for(int i = 0; i < T; i++)
		in	>>A[i]>>B[i];

	for(int i = 0; i <T; i++)
	{
		for(long j = A[i];j <= B[i]; j++)
		{
			string s1 = long_string(j);
			for(int k = s1.length()-1; k > 0; k--)
			{
				string s = s1;
				rotate(s.begin(),s.begin()+k,s.end());
				long _new = string_long(s);
				if(_new > j && _new <= B[i])
					pair[i]++;
			}
		}
	}

	for(int i =0; i < T; i++)
		out	<<"Case #" << i+1 << ": " << pair[i] << endl;

	return 0;
}

string long_string(long T)
{
	string s;
	stringstream out;
	out << T;
	s = out.str();
	return s;
}

long string_long(string s)
{
	long T;
	stringstream convert(s);
	convert >> T;
	return T;
}