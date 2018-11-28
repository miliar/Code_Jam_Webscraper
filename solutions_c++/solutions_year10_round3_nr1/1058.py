#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <list>

using namespace std;

#define INTVAR int
vector<INTVAR> tokenize_str(const string & str,
							const string & delims)
{
	using namespace std;
	// Skip delims at beginning, find start of first token
	string::size_type lastPos = str.find_first_not_of(delims, 0);
	// Find next delimiter @ end of token
	string::size_type pos     = str.find_first_of(delims, lastPos);

	// output vector
	vector<INTVAR> tokens;

	while (string::npos != pos || string::npos != lastPos)
	{
		// Found a token, add it to the vector.
		string temp = str.substr(lastPos, pos - lastPos);
		INTVAR tempint = atoi(temp.c_str());
		tokens.push_back(tempint);
		// Skip delims.  Note the "not_of". this is beginning of token
		lastPos = str.find_first_not_of(delims, pos);
		// Find next delimiter at end of token.
		pos     = str.find_first_of(delims, lastPos);
	}

	return tokens;
}

vector<string> tokenize_str2(const string & str,
							const string & delims)
{
	using namespace std;
	// Skip delims at beginning, find start of first token
	string::size_type lastPos = str.find_first_not_of(delims, 0);
	// Find next delimiter @ end of token
	string::size_type pos     = str.find_first_of(delims, lastPos);

	// output vector
	vector<string> tokens;

	while (string::npos != pos || string::npos != lastPos)
	{
		// Found a token, add it to the vector.
		string temp = str.substr(lastPos, pos - lastPos);
		tokens.push_back(temp);
		// Skip delims.  Note the "not_of". this is beginning of token
		lastPos = str.find_first_not_of(delims, pos);
		// Find next delimiter at end of token.
		pos     = str.find_first_of(delims, lastPos);
	}

	return tokens;
}
int main()
{
	string line;
	ifstream inp("d:/A-large.in");
	ofstream out("d:/A-large.out",ios::out);
    if (! inp.eof() )
    {
      getline (inp,line);
    }
	int Ntc = atoi(line.c_str());
	for (int i=1;i <= Ntc ;i++)
    {
		INTVAR total=0;
		if (! inp.eof() )
            getline (inp,line);
		int N = atoi(line.c_str());
		vector <int> A,B;
		string delim=" ";
		for (int j=0;j<N;j++)
		{
			getline (inp,line);
			vector <INTVAR> TTwo = tokenize_str(line,delim);
			A.push_back(TTwo[0]);
			B.push_back(TTwo[1]);
		}

		for (int a=0;a<N;a++)
		{
			for (int b=a+1;b<N;b++)
			{
				if((A[a]>A[b] && B[a]<B[b]) ||
				    (A[a]<A[b] && B[a]>B[b]))
				{
					total++;
				}
			}
		}
		out<<"Case #"<<i<<": "<<total<<endl;
    }
out.close();
inp.close();
return 0;
}


