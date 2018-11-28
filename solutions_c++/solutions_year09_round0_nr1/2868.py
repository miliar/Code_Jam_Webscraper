#include <map>
#include <algorithm>
#include <string>
#include <set>
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
	ifstream inp("C:/GoogleCodeJam/Sample.txt");
    ofstream out("C:/GoogleCodeJam/Output.txt",ios::out);
    if (! inp.eof() )
    {
      getline (inp,line);
    }
	vector <int> firstLine;
	vector <string> dictwordset;
	vector <string> testcaseset;
    string delim=" ";
    firstLine = tokenize_str(line,delim);

    for (int i=0;i<firstLine[1] && (! inp.eof()) ;i++)
    {
 		getline (inp,line);
		dictwordset.push_back(line);
    }
    for (int j=0;j<firstLine[2] && (! inp.eof()) ;j++)
	{
		getline (inp,line);
		vector <int> position;
		testcaseset.push_back(line);
	}
	for ( int k =0 ; k < testcaseset.size(); k++ )
	{
		string tc = testcaseset[k];
		vector <string> pattern;
		int pos=0;
		string pat;
		bool isbegin=false;
		bool isend=false;
		for ( int j =0; j<tc.size(); j++ )
		{
		   if(tc[j] == '(')
		   {
			  pat="";
              isbegin=true;
			  continue;
		   }
		   else if(tc[j] == ')')
		   {
			   isbegin=false;
			   pattern.push_back(pat);
			   pos++;
			   continue;
		   }
		   if (isbegin)
		   {
			   string temp = tc.substr(j,1);
			   pat.append(temp);
		   }
		   else 
		   {
			   string temp = tc.substr(j,1);
			   pattern.push_back(temp);
			   pos++;
		   }
		}

		out<<"Case #"<<k+1<<": ";
		int count = 0;
		for ( int x =0 ; x < dictwordset.size(); x++ )
		{
			string word = dictwordset[x];
			int sum = 0;
			for ( int n = 0; n < pattern.size() ; n++ )
			{
				if( pattern[n].find(word[n]) != string::npos )
 			    {
					sum++;
				}
			}
			if ( sum == pattern.size() )
				count++;
		}

		out<<count<<endl;
     }
out.close();
inp.close();
return 0;
}
