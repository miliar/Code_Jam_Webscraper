#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <iomanip>
#include <cstdio>

using namespace std;

string readline(istream & fin, int nmax = 1024)
{
	char *c = new char[nmax];
	fin.getline(c,nmax);
	string s(c);
	delete c;
	return s;
}

const string impossible = "Impossible";
typedef map< int,int,greater<int> > InputMap;

string test_case(istream &fin)
{
	int P, K, L;
	fin >> P >> K >> L;
	readline(fin);
	int i;

	InputMap input;

	for(i=0;i<L;++i)
	{
		int X;
		fin >> X;
		input[X]++;
	}
	readline(fin);

	vector<int> output(K);

	i=0;
	
	double x = 0;

	for( InputMap::iterator j = input.begin(); j != input.end(); ++j )
	{
		for(int k = 0; k < j->second; ++k)
		{

			if(++output[i]>P)
				return impossible;
				
			x += output[i] * j->first;

			if((++i)==K)
				i=0;
		}
	}


	char str[1024];

	sprintf(str,"%.0lf",x);

	return string(str);
}



int main(int argc, char* argv[])
{
	if (argc < 2) return -1;

	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	int N;

	fin >> N;
	readline(fin);

	for (int i = 1; i <= N; ++i)
	{
		fout << "Case #" << i <<": "<< test_case( fin ) << "\n";
	}

	return 0;
}