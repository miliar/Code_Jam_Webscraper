#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

ofstream fout;

void solve(int c, vector<string> &s, vector<string> &q)
{
	int p = 0;
	int ret = 0;
	while(true)
	{
		int t = p;
		while(t < q.size() && s[0] != q[t])
			t++;
		int mx = t;
		int b = 0;
		for(int i = 1; i < s.size(); i++)
		{
			t = p;
			while(t < q.size() && s[i] != q[t])
				t++;
			if(t > mx)
			{
				mx = t;
				b = i;
			}
		}
		if(mx >= q.size())
			break;
		else
		{
			ret++;
			p = mx;
		}
	}
	fout << "Case #" << c+1 << ": " << ret << endl;
}

int main(int argc, char *argv[])
{
	string t;
	ifstream f(argv[1]);
	fout.open(argv[2]);
	int n;
	f >> n;
	getline(f,t);
	for(int i = 0; i < n; i++)
	{
		int s;
		f >> s;
		getline(f,t);
		vector<string> engines(s);
		for(int j = 0; j < s; j++)
			getline(f,engines[j]);
		int q;
		f >> q;
		getline(f,t);
		vector<string> queries(q);
		for(int j = 0; j < q; j++)
			getline(f,queries[j]);
		solve(i,engines,queries);
	}
	f.close();
	fout.close();
}
