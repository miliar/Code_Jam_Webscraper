#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int T,R,k,N,result;

void solve(queue<int> g)
{
	//ofstream fout("C-small.out");
	int i,j,l,c;
	for (i=0;i<R;i++)
	{
		j=0;
		c=0;
		while (1)
		{
			l=g.front();
			if (l+j>k)
				break;
			c++;
			if (c>N)
				break;
			j+=l;
			g.pop();
			if (g.empty())
			{
				g.push(l);
				break;
			}
			g.push(l);
		}
		result+=j;
	}
}

int main()
{
	int i,j,l;
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	fin >> T;
	for (i=0;i<T;i++)
	{
		queue<int> g;
		fin >> R >> k >> N;
		result=0;
		for (j=0;j<N;j++)
		{	
			fin >> l;
			g.push(l);
		}
		fout << "Case #" << i+1 << ": ";
		solve(g);
		fout << result << endl;
	}
	return 0;
}