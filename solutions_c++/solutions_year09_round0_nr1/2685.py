#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string.h>

using namespace std;

typedef struct str16
{
	char data[16];
}Str16;

typedef struct str28
{
	char data[28];
}Str28;



int main()
{
	ifstream inStream;
	ofstream outStream("output3.txt", ios_base::out | ios_base::app);
	
	int i_L, i_D, i_N;
	char enter = '\n';
	
	inStream.open("A-large.in");

	if (inStream.fail())
	{
		cerr << "Input file opening failed.\n";
		exit(1);
	}

	inStream >> i_L;
	inStream >> i_D;
	inStream >> i_N;
	

	vector<Str16 > ds;
	vector<Str28> *cs = new vector<Str28>[i_N];

	for(int i = 0 ; i <=  i_D ; ++i)
	{
		Str16 buf;
		inStream.getline(buf.data, 16 , enter);
		if( i ==0 ) continue;
		ds.push_back(buf);
	}



	for(int i = 0 ; i < i_N ; ++i)
	{
		char buf[1024];
		Str28 st;
		memset(st.data, 0x00, 28);
		inStream.getline(buf, 1024 , enter);
		bool shared = false;
		cout << "i_N : " << i_N << endl;
		for(int j = 0, k = 0; j < strlen(buf) ; ++j)
		{
			if( buf[j] == '(')
			{
				st.data[k++] = buf[++j];
				shared = true;
			}
			else if(buf[j] == ')')
			{
				shared = false;
				cs[i].push_back(st);
				memset(st.data, 0x00, 28);
				k=0;
			}
			else if(shared)
			{
				st.data[k++] = buf[j];
			}			
			else 
			{
				st.data[k++] = buf[j];
				cs[i].push_back(st);
				memset(st.data, 0x00, 28);
				k=0;
			}
			
		}
		
	}

	for( int i = 0 ; i < i_N ; ++i)
	{
		int count = 0;
		for( int j = 0 ; j < i_D ; ++j)
		{
			bool check = true;
			for(int k = 0 ; k < i_L ; ++k)
			{
				char tmp[2] = {0};
			
				tmp[0] =  ds[j].data[k] ;
					
				if(!strstr(cs[i][k].data, tmp))
				{
					check = false;
					break;
				}
			}
			if(check)
				count++;
		}
		outStream << "Case #" << i+1 << ": " << count << "\n";
	}

	inStream.close();


	return 0;
	
}

