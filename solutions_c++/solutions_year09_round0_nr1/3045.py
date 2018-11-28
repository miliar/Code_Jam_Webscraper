#include <iostream>
#include <string>
#include <ctime>
#include <set>
#include <fstream>

using namespace std;

int main()
{

	
	ofstream out("A-small.out");
	ifstream in("test.txt");
	
	int L, D, N;
	in >> L >> D >> N;

	/*
	for(int i =0; i < D; i ++)
	{
		string line;
		for(int j=0; j < L; j++)
		{
			line += (char) ('a' + rand()%26);
		}

		out << line << endl;
	}
	*/

		

	string dic[5000];
	
	for(int i=0; i < D; i++)
	{
		//cin >> dic[i];
		in >> dic[i];
	}
	int res[500];
	memset(res, 0, sizeof(int)*500);
	for(int i =0; i < N; i++)
	{
		string line;
		//cin >> line;
		in >> line;
		int test[27][27];
		memset(test, 0 , sizeof(int) * 27*27);
		int count = 0;
		for(int j=0; j<line.size(); j++)
		{
			if( line[j] == ')')
				break;
			if( line[j] == '(')
			{
				j++;
				while( line[j] != ')')
				{
					test[count][ line[j] - 'a' ] = 1;
					j++;
				}
				count++;

			}else
			{
				test[count][ line[j] - 'a' ] = 1;
				count ++;

			}
		}

		for(int j=0; j < D; j++)
		{
			int consist = 1;
			for(int k = 0; k < L; k++)
			{
				consist *= test[ k ][ dic[j][k] - 'a' ];
			}
			if( consist == 1){
				res[i] ++;
			}
		
		}

	}

	for(int i=0; i < N; i++)
	{
		out << "Case #" << i+1 << ": " << res[i] << endl;
	}

	return 0;
}

/*
*/