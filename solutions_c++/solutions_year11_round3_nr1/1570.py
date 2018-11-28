#include <iostream>
#include <fstream>
#include <vector>



using namespace std;

int main (int argc, char const* argv[])
{
	ifstream in ("A.in");
	ofstream out ("A.out");
	
	
	int T, R, C, blue;
	string s[60];
	in >> T;
	
	for (unsigned int t = 0; t < T; t += 1)
	{
	
		in >> R >> C;
		
		blue = 0;
		
		for (unsigned int i = 0; i < R; i += 1)
		{
			in >> s[i];
		}
		for (unsigned int i = 0; i < R; i += 1)
		{
			for (unsigned int j = 0; j < C; j += 1)
			{
				if(s[i][j] == '#')	blue++;
			}
		}
		for (unsigned int i = 0; i < R-1; i += 1)
		{
			for (unsigned int j = 0; j < C-1; j += 1)
			{
				if(s[i][j] == '#' && s[i+1][j] == '#' && s[i][j+1] == '#' && s[i+1][j+1] == '#')
				{
					blue -= 4;
					s[i][j] =(char)47;
					s[i+1][j+1] = (char)47;
					s[i][j+1] = (char)92;
					s[i+1][j] = (char)92;
				}
			}
		}
		out << "Case #" << t+1 << ":\n";
		if (blue != 0)
		{
			out << "Impossible\n";
		}
		else
		{
			for (unsigned int i = 0; i < R; i += 1)
			{
				out << s[i] << "\n";
			}
		}
	}
	
	return 0;
}











