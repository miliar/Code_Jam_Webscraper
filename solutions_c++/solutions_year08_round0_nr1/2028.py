
#include <cstdlib>
#include <cmath>
#include <vector>
#include <iterator>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <limits>
#include <istream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdarg>

using namespace std;

typedef vector<string> vector_string;

// Tokenizes a string:
void  tokenize( const string &inString, const string &inDelimiters, vector_string	&outTokens );
// Parses one text file:
void  tokenize_next_line(ifstream &inf, std::vector<std::string> &outTokens )
{
	string str;
	std::getline(inf,str);
	tokenize(str," \t",outTokens);
}


// SOLVE THE PROBLEM FOR ONE TEST CASE =========================================
void  test_case(int case_num, ifstream &f )
{
	//vector_string	strs;	// Strings from input 
	string			str;

	map<string,int>		Ss;

	// Read Ss:
	getline(f,str);
	int  nSs = atoi(str.c_str());
	for (int i=0;i<nSs;i++)
	{
		getline(f,str);
		Ss[ str ] = i;
	}

	// Read Qs:
	getline(f,str);
	int  nQs = atoi(str.c_str());
	
	set<int>	def;
	def.insert(nQs+1);

	vector< set<int> >   apars(Ss.size(), def );	// Apariciones
	for (int i=0;i<nQs;i++)
	{
		getline(f,str);
		map<string,int>::iterator it = Ss.find(str);
		if ( it!=Ss.end())
		{
			apars[it->second].insert(i);
		}
	}

	// Recorrer cogiendo el mas largo primero:
	int nChanges = -1;
	int pos = 0;
	while (pos<nQs)
	{
		int  best_q = 0;
		int  best_pos = pos;
		for (unsigned q=0;q<Ss.size();q++)
		{
			for (set<int>::iterator it=apars[q].begin();it!=apars[q].end();it++)
			{
				if (*it>=pos)
				{
					if (*it>best_pos)
					{
						best_pos = *it;
						best_q = q;
					}
					break;
				}
			}
		}
		pos = best_pos;
		
		nChanges++;
	}
	if (nChanges<0) nChanges=0;


	cout << "Case #" << case_num << ": " << nChanges << endl;
}

// The MAIN ----------------------------------
int main(int argc, char**argv)
{
	const char *file_open = "A-large.in";
	if (argc>1)
		file_open = argv[1];

	// Open file:
	ifstream	f( file_open  );
	assert(!f.fail());

	vector_string	strs;	// Strings from input 

	tokenize_next_line(f, strs);
	size_t	N = atoi( strs[0].c_str());

	// Each test case:
	for (size_t i=0;i<N;i++)
		test_case(i+1,f);

	return 0;
}




/*---------------------------------------------------------------
						my_strtok
---------------------------------------------------------------*/
char * my_strtok( char *str, const char *strDelimit, char **context )
{
#if defined(_MSC_VER) && (_MSC_VER>=1400)
	// Use a secure version in Visual Studio 2005:
	return ::strtok_s(str,strDelimit,context);
#else
	// Use standard version:
	return ::strtok(str,strDelimit);
#endif
}

/*---------------------------------------------------------------
						tokenize
---------------------------------------------------------------*/
void  tokenize(
	const std::string			&inString,
	const std::string			&inDelimiters,
	std::vector<std::string>	&outTokens )
{
	char	*nextTok,*context;

	outTokens.clear();

	nextTok = my_strtok ((char*)inString.c_str(),inDelimiters.c_str(),&context);
	while (nextTok != NULL)
	{
		outTokens.push_back( std::string(nextTok) );
		nextTok = my_strtok (NULL,inDelimiters.c_str(),&context);
	};
}

