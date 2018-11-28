#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

queue<int> s[2], r;

int main()
{
	ofstream fout ("A-large.out");
	ifstream fin ("A-large.in");
	int t;
	fin >> t;
	for(int j = 0; j < t; j++)
	{
		int n, c = 0, p[2] = {0};
		fin >> n;
		for(int i = 0; i < n; i++)
		{
			char a; int b;
			fin >> a >> b;
			r.push(a == 'B' ? 1 : 0);
			s[a == 'B' ? 1 : 0].push(b - 1);
		}
		while(!r.empty())
		{
			int u = r.front();
			c++;
			if(!s[(u + 1) % 2].empty())
				if(p[(u + 1) % 2] != s[(u + 1) % 2].front())
					p[(u + 1) % 2] += (p[(u + 1) % 2] > s[(u + 1) % 2].front()?-1:1);
			if(p[u] == s[u].front())
			{	r.pop(), s[u].pop();	continue;	}
			if(!s[u].empty())
				if(p[u] != s[u].front())
					p[u] += (p[u] > s[u].front()?-1:1);
		}
		fout << "Case #" << j + 1 << ": " << c << endl;
	}
	return 0;
}
