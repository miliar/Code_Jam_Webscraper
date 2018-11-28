#include <iostream>
#include <fstream>
#include <vector>
#include <functional>
#include <algorithm>
using namespace std;

//#define fin cin
//#define fout cout

ifstream fin("B-large.in");
ofstream fout("B-large.out");

vector<int> t;

int main()
{
	int T, N, S, p;
	fin >> T;
	for(int count = 1; count <= T; count++)
	{
		fin >> N >> S >> p;
		int res = 0, score;
		t.clear();
		for(int i = 0; i < N; i++)
		{
			fin >> score;
			if(score % 3 == 0)
			{
				if(score/3 >= p)
					res++;
				else
					t.push_back(score);
			}
			else if (score % 3 == 1)
			{
				if(score/3+1 >= p)
					res++;
			}
			else
			{
				if((score+1)/3 < p)
					t.push_back(score);
				else
					res++;
			}
		}
		if(t.size() > 0)
		{
			sort(t.begin(), t.end(), greater<int>());
			for(int i = 0; i < t.size() && S > 0; i++)
			{
				if(t[i] == 0)
					continue;
				if((t[i]-2)/3+2 >= p)
					res++, S--;
			}
		}
		fout << "Case #" << count << ": " << res << endl;
	}
	return 0;
}
