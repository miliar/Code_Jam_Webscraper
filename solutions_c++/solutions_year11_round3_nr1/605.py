# include <iostream>
# include <fstream>
# define MAX 100

using namespace std;

int main(int argv, char **argc)
{
	ifstream in("input.in");
	ofstream out("output.out");
	int totalCase;
	in >> totalCase;
	
	for(int caseNumber = 1; caseNumber <= totalCase; caseNumber++)
	{
		int height, width;
		int w[MAX][MAX] = {0,};
		int visit[MAX][MAX] = {0,};
		in >> height >> width;

		char ch;
		for(int i = 0; i < height; i++)
		{
			for(int j = 0; j < width; j++)
			{
				in >> ch;
				if( ch == '#')
				{
					w[i][j]=1;
				}
				else
				{
					w[i][j]=0;
				}
			}
		}

		for(int i = 0; i < height; i++)
		{
			for(int j = 0; j < width; j++)
			{
				if(w[i][j] == 1 && visit[i][j] == 0)
				{
					if(w[i][j + 1] == 1 && w[i + 1][j] == 1 && w[i + 1][j + 1] && visit[i+1][j] == 0  && visit[i][j+1] == 0  && visit[i+1][j+1] == 0 )
					{
						visit[i+1][j] = visit[i][j+1] = 1;
						visit[i][j] = visit[i+1][j+1] = 2;
					}
				}
			}
		}

		bool flag = true;
		for(int i = 0; i < height; i++)
		{
			for(int j = 0; j < width; j++)
			{
				if(w[i][j] == 1 && visit[i][j] == 0)
				{
					flag = false;
					break;
				}
			}
			if(flag == false)
			{
				break;
			}
		}

		out << "Case #" << caseNumber << ":" << endl;
		if(flag == false)
		{
			out << "Impossible" << endl;
		}
		else
		{
			for(int i = 0; i < height; i++)
			{
				for(int j = 0; j < width; j++)
				{
					if(visit[i][j] == 0)
					{
						out << ".";
					}
					else if(visit[i][j] == 1)
					{
						out << "\\";
					}
					else if(visit[i][j] == 2)
					{
						out << "/";
					}
				}
				out << endl;
			}
		}

	}

	in.close();
	out.close();
	return 0;
}