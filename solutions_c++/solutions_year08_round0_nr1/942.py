#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

bool stoi( string &str, int &n )
{
	int res = 0;
	for( int i = 0; i != str.length(); i++ )
	{
		if ( str[i] - '0' > 9 || str[i] - '0' < 0 )
			return false;
		res = res * 10 + str[i] - '0';
	}
	n = res;
	return true;
}
	 
int find ( vector<string> &vec_str, string &str, int start_pos)
{
	int pos = start_pos;
	for( vector<string>::iterator it = vec_str.begin()+start_pos; it != vec_str.end(); it++, pos++ )
	{
		if ( *it == str )
			return pos;
	}
	return -1;
}

int main(int argc, char* argv[])
{
	//define file stream
	ofstream outfile;
	ifstream infile;	

	//the file name;
	string filename;

	if ( argc == 2 )
		filename = argv[1];
	else 
	{
		if ( argc == 1 )
			cout<<"please enter the name of the input data file:";
		else
			cout<<"the arguments number is wrong, please enter the name of input data file:";
		cin>>filename;
	}
	
	//open output file and input file
	outfile.open("output");
	infile.open(filename.c_str());
	
	if ( !infile )
	{
		cout<<"error, the input data file is invalid"<<endl;
		exit(0);
	}
	
	//the string that is used to read each line of input data file
	string line;
	//case num
	int case_num;
	
	case_num = 0;
	
	getline(infile, line);
	if( !stoi( line, case_num ) )
	{
		cout<<"error, the case num is invalid"<<endl;
		exit(0);
	}

	int server_num;
	int query_num;

	vector<string> server;
	vector<string> query;

	for(int i = 0; i != case_num; i++ )
	{
		//initiate variables
		server_num = 0;
		query_num = 0;
		server.clear();
		query.clear();

		//get the server num
		getline(infile, line);
		
		if( !stoi(line, server_num) )
		{
			cout<<"error, the case #"<<i+1<<"'s server num is not valid"<<endl;
			exit(0);
		}
		
		//read each server name
		for( int j = 0; j != server_num; j++ )
		{
			getline(infile, line);
			server.push_back( line );
		}
		
		//get the query num;
		getline(infile, line);
		
		if ( !stoi(line, query_num) )
		{
			cout<<"error, the case #"<<i+1<<"'s query num is not valid"<<endl;
			exit(0);
		}
		
		//read each query
		for( int j = 0; j != query_num; j++ )
		{
			getline(infile, line);
			query.push_back( line );
		}

		//the num of switch
		int swi = 0;

		//pos
		int pos;
		//start pos
		int start_pos = 0;

		while( true )
		{	
			//flag of finish find
			bool flag_finish = false;

			//record the max server name serial in query
			unsigned int x = 0;
			for( vector<string>::iterator it = server.begin(); it != server.end(); it++ )
			{
				pos = find( query, *it, start_pos );
				if ( pos == -1 )
				{
					flag_finish = true;
					break;
				}
				if ( pos > x )
					x = pos;
			}
			if ( flag_finish )
				break;
			else
			{
				start_pos = x;
				swi++;
			}
		}
		
		outfile<<"Case #"<<i+1<<": "<<swi<<endl;
	}
	
}

