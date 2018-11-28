#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>

using namespace std;
// boost::numeric::ublas::matrix<double> m;

const string text("welcome to code jam");
const int textlen = text.length();
string line;

boost::numeric::ublas::matrix<int> cache;

int count(int textfirst,int linefirst)
{
	if (textfirst == textlen)
		return 1;
	if (linefirst == line.length())
		return 0;

	if (cache(textfirst,linefirst)!=0)
		return cache(textfirst,linefirst) - 1;

	int result = 0;

	for(int i = linefirst; i<line.length(); i++)
	{
		if (line[i] == text[textfirst])
		{
			result += count( textfirst+1, i+1 );
			result %= 10000;
		}
	}
	
	cache(textfirst,linefirst) = result + 1;
	return result;
}

int main()
{
	int N;
	string dummy;
	cin >> N;
	getline(cin, dummy);

	for(int n = 0; n<N; n++)
	{
		string _line;
		getline(cin, _line);
		line.clear();
		
		// Strip useless chars
		for(int i = 0;i<_line.length(); i++)
		{
			char ch = _line[i];
			if (text.find(ch)!=string::npos)
				line+=ch;
		}
		
		cache = boost::numeric::ublas::zero_matrix<int>(textlen, line.length());

		// cout << "[" << line << "]" << endl;
		char out[100];
		sprintf( out, "%04d", count(0,0) );
		cout << "Case #" << n+1<< ": " << out << endl;
	}
	return 0;
}
