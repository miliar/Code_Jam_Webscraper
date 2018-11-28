#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main()
{
	int r,k,n,t,i,j,c,cas,gc;
	__int64 s;
	vector<int> g;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("c-small.out");

	fin >> t;
	for (cas = 0;cas < t;cas ++)
	{
		fin >> r >> k >> n;
		g.clear();
		while (n --)
		{
			fin >> i;
			g.push_back(i);
		}
		s = 0;
		j = 0;
		for (i = 0;i < r;i ++)
		{
			c = 0;
			c += g[j];
			gc = 1;
			while (c <= k && gc <= g.size())
			{
				j = (j + 1) % g.size();
				c += g[j];
				gc ++;
			} 
			c -= g[j];
			s += c;
		}
		fout << "Case #" << cas + 1 << ": " << s << endl;


	}
}
