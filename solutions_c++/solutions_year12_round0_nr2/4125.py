#include<iostream>
#include<fstream>
#include<string>
using namespace std;

ifstream fin;
ofstream fout;

int main()
{
	int T, X = 0 , i , N , S , p , output , t;
	string s;

	fin.open("B_large.in");
	fout.open("b_large.out");
	
	fin >> T;
	while(T--)
	{
		output = 0;
		fin >> N >> S >> p;
		for( i = 0 ; i < N ; ++i )
		{
			fin >> t;
			if(  p == 0  )
			{
				++output;
				continue;
			}
			else if(  t  >=  p*3-2  )
				++output;
			else if( S > 0 )
			{
				if(   p == 1   &&   t == 0   )//only p == 1, and t == 0 will be here
				{
					continue;
				}
				if(  t  >=  p*3-4  )
				{
					++output;
					--S;
				}
			}
		}
		fout << "Case #" << ++X << ": " << output << endl;
	}
	return 0;
} 

