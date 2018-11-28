// CodeJam 2011 - Qualification Round - Bot trust
#include <fstream>
#include <iostream>
using namespace std;

int main()
{
   int T, R, C;
   char **tile;
   ifstream infile("A-large.in");
   ofstream outfile("A-large.out");
   char ch;
   
   infile >> T;
   for(int i=1; i<=T; i++)
   {
	infile >> R; infile >> C;
	tile = new char*[R];
	for(int j=0; j<R; j++)
	{
		tile[j] = new char[C];
		for(int k=0; k<C; k++)
		{
			infile >> ch;
			tile[j][k] = ch;
		}
	}
	bool flag = true;
	for(int j=0; ((j<R) && flag); j++)
	{
		cout << "i="<<i<<"  R="<<R<<"  C="<<C<<"   j="<<j<<endl;
		for(int k=0; ((k<C) && flag); k++)
		{
			cout<<k<<" ";
			if(tile[j][k] == '.') continue;
			if(tile[j][k] == '#')
			{
				if((k > C-2) || (j > R-2))
				{
					flag = false;
					continue;
				}
				if(((k<C-1) && tile[j][k+1]=='#') && ((j<R-1) && tile[j+1][k]=='#') && ((j<R-1) && (k<C-1) && tile[j+1][k+1]=='#'))
				{
					tile[j][k] = '/'; tile[j][k+1] = '\\';
					tile[j+1][k] = '\\'; tile[j+1][k+1] = '/';
				}
				else
				{
					flag = false;
					continue;
				}
			}
		}
		cout<<endl;
	}

	outfile << "Case #" << i << ":" << endl;
	if(!flag) outfile << "Impossible" << endl;
	else
	{
		for(int j=0; j<R; j++)
		{
			for(int k=0; k<C; k++)
			{
				outfile << tile[j][k];
			}
			outfile << endl;
		}
	}
	//for(int k=0; k<C; k++)
	//	delete[] tile[k];
	delete[] tile;
   }
   infile.close();
   outfile.close();
   return 0;
}

