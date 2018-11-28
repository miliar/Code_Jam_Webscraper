#include <fstream>
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>

using namespace std;

char pic [52][52];

int main () 
{
	ifstream in("in.in");
	ofstream out("out.out");
	
	int T;
	
	in >> T;
	
	for(int i = 0; i < T; ++i)
	{	
		int R, C;
		in >> R >> C;
	
		string row;
		for(int j = 0; j < R; ++j)
		{
			in >> row;
			for(int k = 0; k < C; ++k)
				pic[j][k] = row[k];
		}
		
//  		for(int j = 0; j < R; ++j)
//  		{
//  			for(int k = 0; k < C; ++k)
//  				cout << pic[j][k];
//  			cout << "\n";
//  		}
//  		cout << "\n";

		//input done, do processing
		bool impossible = false;
		
		for(int j = 0; j < R; ++j) //for each tile, greedily place a red one
		{
			for(int k = 0; k < C; ++k)
			{	
// 				cout << "j: " << j << "     k:" << k << "   " << pic[j][k] << "\n";
				
				if(pic[j][k] == '#') //try place a red one here
				{
// 					cout << "Derp\n";
					
					if((j+1 >= R) || (k+1 >= C))
					{
						impossible = true;
						break;
					}
					
					if((pic[j][k+1] == '#') &&
						(pic[j+1][k] == '#') &&
						(pic[j+1][k+1] == '#'))
					{
						pic[j][k] = '/';
						pic[j][k+1] = '\\';
						pic[j+1][k] = '\\';
						pic[j+1][k+1] = '/';
					}
					else
					{
						impossible = true;
						break;
					}
					
				}
			}
			
			if(impossible)
			{
				out << "Case #" << i+1 << ":\nImpossible\n";
				break;
			}
		}
		
		if(!impossible)
		{
			out << "Case #" << i+1 << ":\n";
			for(int j = 0; j < R; ++j)
			{					
				for(int k = 0; k < C; ++k)
					out << pic[j][k];
				out << "\n";	
			}
		}
		
	}
}