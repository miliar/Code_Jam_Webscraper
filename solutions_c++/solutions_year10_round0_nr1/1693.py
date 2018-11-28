#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iostream>

using namespace std;

vector<int> tokenize_str(const string & str,
							const string & delims)
{
	using namespace std;
	// Skip delims at beginning, find start of first token
	string::size_type lastPos = str.find_first_not_of(delims, 0);
	// Find next delimiter @ end of token
	string::size_type pos     = str.find_first_of(delims, lastPos);

	// output vector
	vector<int> tokens;

	while (string::npos != pos || string::npos != lastPos)
	{
		// Found a token, add it to the vector.
		string temp = str.substr(lastPos, pos - lastPos);
		int tempint = atoi(temp.c_str());
		tokens.push_back(tempint);
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
	ifstream in("d:/A-small-practice.in");
	ofstream out("d:/A-small-practice.out",ios::out);
    if (! in.eof() )
    {
      getline (in,line);
    }
	int Ntc = atoi(line.c_str());
	for (int i=1;i <= Ntc ;i++)
    {
		if (! in.eof() )
            getline (in,line);
		string delim=" ";
		vector <int> TTwo;
        TTwo = tokenize_str(line,delim);
		int N = TTwo[0];
		int T = TTwo[1];
		int iVal=1<<N;
		if((T+1)%iVal == 0)
			out<<"Case #"<<i<<": ON"<<endl;
		else
			out<<"Case #"<<i<<": OFF"<<endl;
    }
out.close();
in.close();
return 0;
}


/*	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16
s	1P	0P	1P	0P	1P	0P	1P	0P	1P	0P	1P	0P	1P	0P	1P	0P
s	0P	1N	1P	0N	0P	1N	1P	0N	OP	1N	1P	0N	0P	1N	1P	0N
s	0N	0N	0P	1N	1N	1N	1P	0N	0N	0N	0P	1N	1N	1N	1P	0N
s	0N	0N	0N	0N	0N	0N	0P	1N	1N	1N	1N	1N	1N	1N	1P	0N
*/