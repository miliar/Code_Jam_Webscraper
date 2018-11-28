#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	string temp;
	getline( cin, temp );
	
	int n;
	n = atoi(temp.c_str());
//	cout << n << endl;
	for( int a = 0; a < n; a++ )
	{
		string line;
		long int count[19];
		for( int i = 0; i < 19; i++ )
		{
			count[i] = 0;
		}
		getline( cin, line );
//		cout << line << endl;

		/*
		   w = 0
		   e = 1,6,14
		   l = 2
		   c = 3,11
		   o = 4,9,12
		   m = 5,18
		   ' '= 7,10,15
		   t = 8
		   d = 13
		   j = 16
		   a = 17
		*/
//		bool flag = false;
		for( int i = 0; i < line.length(); i++ )
		{
#if 0
			if( flag )
			{
				flag = false;
				count[7] = count[6];
				count[10] = count[9];
				count[15] = count[14];
			}
#endif
			switch(line[i])
			{
//				case 'W':
				case 'w':
					count[0]++;
					break;
//				case 'E':
				case 'e':
					count[1]+=count[0];
					count[6]+=count[5];
					count[14]+=count[13];
					break;
//				case 'L':
				case 'l':
					count[2]+=count[1];
					break;
//				case 'C':
				case 'c':
					count[3]+=count[2];
					count[11]+=count[10];
					break;
//				case 'O':
				case 'o':
					count[4]+=count[3];
					count[9]+=count[8];
					count[12]+=count[11];
					break;
//				case 'M':
				case 'm':
					count[5]+=count[4];
					count[18]+=count[17];
					break;
//				case 'T':
				case 't':
					count[8]+=count[7];
					break;
//				case 'D':
				case 'd':
					count[13]+=count[12];
					break;
//				case 'J':
				case 'j':
					count[16]+=count[15];
					break;
//				case 'A':
				case 'a':
					count[17]+=count[16];
					break;
#if 0
				case ' ':
					count[7]=count[6];
					count[10]=count[9];
					count[15]=count[14];
					break;
#endif
				case ' ':
					count[7]+=count[6];
					count[10]+=count[9];
					count[15]+=count[14];
					break;
			}
		}
#if 0
		cout << "Count :";
		for( int i = 0; i < 19; i++ )
		{
			cout << count[i] << " ";
		}
		cout << endl;
#endif
		int ans = count[18]%10000;

		string output;
		for( int i = 1000; i >= 1; i/=10 )
		{
			output += ('0' + ans/i );
			ans -= (ans/i)*i;
		}


		cout << "Case #" << a+1 << ": " << output <<endl;
	}


	return 0;
}
