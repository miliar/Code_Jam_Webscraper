#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>


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
	ifstream inp("d:/A-small-practice.in");
	ofstream out("d:/A-small-practice.out",ios::out);
    if (! inp.eof() )
    {
      getline (inp,line);
    }
	int Ntc = atoi(line.c_str());
	for (int i=1;i <= Ntc ;i++)
    {
		INTVAR total=0;
		pair<set<string>::iterator,bool> ret;
		if (! inp.eof() )
            getline (inp,line);
		string delim=" ";
		vector <INTVAR> TTwo;
        TTwo = tokenize_str(line,delim);
		INTVAR N = TTwo[0];
		INTVAR M = TTwo[1];
		set <string> dictdir;
		string delim2="/";
		for ( int a=0;a<N;a++)
		{
			getline (inp,line);
			vector <string> v = tokenize_str2(line,delim2);
			string tempdir="";
			for(int b=0;b<v.size();b++)
			{
				tempdir.append("/");
				tempdir.append(v[b]);
				dictdir.insert(tempdir);
			}
		}
		for ( int a1=0;a1<M;a1++)
		{
			getline (inp,line);
			vector <string> v2 = tokenize_str2(line,delim2);
			string tempdir="";
			for(int c=0;c<v2.size();c++)
			{
				tempdir.append("/");
				tempdir.append(v2[c]);
				ret = dictdir.insert(tempdir); 
				if (ret.second==true)
					total++;
			}
		}
		out<<"Case #"<<i<<": "<<total<<endl;
    }
out.close();
inp.close();
return 0;
}


