#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	fstream infile("A-large.in");
	fstream outfile("A-large.out");
    int T;
	infile >> T;
	int cs = 1;

	while(T)
	{
		int R,C;
		infile >> R >> C;
		vector<vector<char> > v;
		v.resize(R);
		for(int i = 0; i < R; i++)
			v[i].resize(C,' ');
		for(int i = 0; i < R;i++)
			for(int j = 0; j < C; j++)
			{
				char ch;
				infile >> ch;
				v[i][j] = ch;
			}

		/*vector<vector<char> > v2;
		v2.resize(R);
		for(int i = 0; i < R; i++)
			v2[i] = v[i];*/

		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
			{
				if(v[i][j] == '#')
				{
					if(i+1 < R && j+1 < C && v[i][j+1] == '#' && v[i+1][j] == '#' && v[i+1][j+1] == '#')
					{
						v[i][j] = '/';
						v[i][j+1] = '\\';
						v[i+1][j] = '\\';
						v[i+1][j+1] = '/';
					}
				}
			}

		bool isPossible = true;
		for(int i = 0; isPossible && i < R; i++)
			for(int j = 0; isPossible && j < C; j++)
			{
				if(v[i][j] == '#')
				{
					outfile << "Case #" << cs << ":" << endl << "Impossible" << endl;
					isPossible = false;
					break;
				}
				if(!isPossible)
					break;
			}

		if(isPossible)
		{
			outfile << "Case #" << cs << ":" << endl;
			for(int i = 0; i < R; i++)
			{
				for(int j = 0; j < C; j++)
					outfile << v[i][j];
				outfile << endl;
			}
		}

		cs++;
		T--;
	}

	infile.close();
	outfile.close();
	
	return 0;
}

