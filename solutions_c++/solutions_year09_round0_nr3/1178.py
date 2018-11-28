#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
using namespace std;

int calc(string text)
{
	int sz = text.size();
	vector< vector<int> > cnt(sz, vector<int> (19, 0));
	string p = "welcome to code jam";
	for (int i = sz - 1; i >= 0; --i)
	{
		for (int j = 18; j >= 0; --j)
		{
			if(i < sz-1)
			{
				cnt[i][j] = cnt[i+1][j];
			}
			if (p[j] == text[i])
			{				
				if(j < 18)
				{
					cnt[i][j] += cnt[i][j+1];
					cnt[i][j] %= 10000;
				}
				else
				{
					cnt[i][j] += 1;
					cnt[i][j] %= 10000;
				}
			}
		}
	}

	return cnt[0][0];
}

int main()
{
	fstream fin("1.txt", fstream::in);
	fstream fout("1.out.txt", fstream::out);

	int N;
	fin>>N;
	string str;
	getline(fin, str);
	for (int i = 0; i < N; ++i)
	{
		string text;
		getline(fin, text);
		fout<<setfill('0')<<"Case #"<<i+1<<": "<<setw(4)<<calc(text)<<endl;
	}

	return 0;
}