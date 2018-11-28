#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

void nextno( char* num )
{
	for( int i=0; num[i]; ++i )
	{
		switch(num[i])
		{
		case '0': 
			num[i] = '1';
			return;
		case '1': num[i] =  '2';
			return;
		case '2': num[i] =  '3';
			return;
		case '3': num[i] =  '4';
			return;
		case '4': num[i] =  '5';
			return;
		case '5': num[i] =  '6';
			return;
		case '6': num[i] =  '7';
			return;
		case '7': num[i] =  '8';
			return;
		case '8': num[i] =  '9';
			return;
		case '9': num[i] =  '0';
			break;
		}
	}
	strcat( num, "1" );
}

bool validate( char* nos, char* str )
{
	char buff[50];
	int len = strlen(str);
	strcpy( buff, nos );
	for( int i=0;i<len; ++i)
	{
		if( str[i] != '0' )
		{
			int j;
			for( j=0; buff[j]; ++ j )
			{
				if( str[i] == buff[j] )
				{
					buff[j] = '0';
					break;
				}
			}
			if( buff[j] == NULL )
				return false;
		}
	}
	for( int k=0; buff[k]; ++ k )
	{
		if( buff[k] != '0' )
			return false;
	}
	return true;
}

int main()
{
	ifstream in;
	ofstream out;
	in.open("inA.txt",ios::in);
	out.open("outA.txt",ios::out);
	char str[4096];
	char str1[4096];
	char nos[50];
	int N;
	int j = 0;
	in >> N;
	for( int ite=1; ite<=N; ++ite) {
		in >> str;
		cout << str << endl;
		strrev(str);
		cout << str << endl;
		j = 0;
		for( int i=0; str[i]; ++i )
		{
			if( str[i] != '0' )
				nos[j++] = str[i];
		}
		nos[j] = '\0';
		cout << str << endl;
		cout << nos << endl;
		
		for( ;;)
		{
			nextno( str );
			if( validate( nos, str ) == true )
				break;
		}
		strrev(str);
		out << "Case #"<< ite << ": " << str << endl;
		cout << endl;
	}
	in.close();	
	out.close();
	return 0;
}