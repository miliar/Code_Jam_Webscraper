#include<fstream>
#include <string>
using namespace std;

#ifndef loop(size)
#define loop(size) for ( int i=0 ; i < size ; i++ )
#endif

int main()
{
	const string alpha = "yhesocvxduiglbkrztnwjpfmaq";
	ifstream in;  ofstream out;
	in.open("in.txt");
	int T ;
	char ** result;
	in>>T;
	string * input = new string[T];
	result = new char*[T];
	int * size = new int [T];
	getline ( in , input[0]);

	for ( int i=0 ; i < T ; i++ )
	{
		getline ( in , input[i]);
	}
	in.close();
	
	for ( int i=0 ; i < T ; i++ )
	{
		size[i] = input[i].length();
		result[i] = new char[size[i]];
		for ( int j=0 ; j < size[i]; j++ )
		{
			if ( input[i][j] == ' ' )
				result[i][j] = ' ';
			else
				result[i][j] = alpha[input[i][j] - 'a'];
		}
	}
	out.open("Out.txt");

	for ( int i=0 ; i < T; i++ )
	{
		out<<"Case #"<<i+1<<": ";
		for ( int j=0 ; j < size[i] ; j++ )
			out<<result[i][j];
		out<<endl;
	}
	out.close();
	return 0;
}

