#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main()
{
	unsigned int T = 0;
	unsigned long int R = 0;		//	Runs
	unsigned long int k = 0;		//	Coaster size
	unsigned int N = 0;				//	Number of groups
	queue<unsigned long int> g;		//	Size of each group
	
	unsigned long int earn = 0;
	unsigned long int cSize = 0;		//	Seats left
	unsigned long int temp = 0;
	int count = 0;
	
	
	ifstream fin ("C-small-attempt0.in");
	ofstream fout ("C-small-attempt0.out");
	
	fin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		fin >> R >> k >> N;
		
		earn = 0;
		
		for(int j = 0; j < N; j++)
		{
			fin >> temp;
			g.push(temp);
		}
		
		for(int j = 1; j <= R; j++)
		{
			cSize = k;
			count = 0;
			while(cSize >= g.front())
			{
				earn += g.front();
				cSize -= g.front();
				g.push(g.front());
				g.pop();
				count++;
				if(count == N)
				{
					break;
				}
			}
		}
		while(!g.empty())
		{
			g.pop();
		}
		
		fout << "Case #" << i << ": " << earn << endl;
	}
}
