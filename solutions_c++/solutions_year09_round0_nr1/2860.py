#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("inA.txt",ios::in);
	out.open("outA.txt",ios::out);
	long L,D,N;
	in >> L >> D >> N ;
	char* buff = new char[4096];
	char* buff2 = new char[4096];
	vector<string> dict;
	for( int i=0; i<D; ++i )
	{
		in >> buff ;
		dict.push_back( string(buff) );
	}
	for( int j=0; j< dict.size(); ++j )
		cout << dict.at(j) << endl;
	cout << endl;
	vector<string> pattern;
	int k = 0;
	bool inbrac = false;
	for( int ite=1; ite<=N; ++ite) {
		k = 0;
		buff2[0] = 0;
		pattern.clear();
		in >> buff;
		for( int j=0; buff[j]; ++j )
		{
			if( buff[j] == '(' )
			{
				inbrac = true;
				if( strlen(buff2) > 0 )
				{
					pattern.push_back( string( buff2 ) );
					k = 0;
					buff2[0] = 0;
				}
			}
			else if ( buff[j] == ')' )
			{
				inbrac = false;
				if( strlen(buff2) > 0 )
				{
					pattern.push_back( string( buff2 ) );
					k = 0;
					buff2[0] = 0;
				}
			}
			else
			{
				buff2[k++] = buff[j];
				buff2[k] = 0;
				if( inbrac )
				{
				}
				else
				{
					pattern.push_back( string( buff2 ) );
					k = 0;
					buff2[0] = 0;
				}
			}
		}
		for( int j=0; j< pattern.size(); ++j )
			cout << pattern.at(j) << endl;
		cout << endl;
		const char* ptr1 = NULL;
		int found = 0;
		found = 0;
		for( int k=0; k< dict.size(); ++k )
		{
			ptr1 = dict.at(k).c_str();
			int l;
			for( l=0; l<L; ++l )
			{
				if( strchr( pattern.at(l).c_str(), ptr1[l] ) == NULL )
					break;
			}
			if( l == L )
				++found;
		}
		out << "Case #"<< ite << ": " << found << endl;
	}
	delete[] buff;
	delete[] buff2;
	in.close();	
	out.close();
	return 0;
}