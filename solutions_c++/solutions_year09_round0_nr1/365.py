#include<fstream>
#include<iostream>
#include<map>
#include<string>
#include<set>
using namespace std;

struct CS
{
	set<char> s;
} cs[16];
string strs[5100];

int main()
{
	ifstream ifs("A-small-attempt1.in");
	ofstream ofs("A-small-attempt1.out");
	int L, D, N;
	int i, k, index, r;
	string buf;
	int caseNo, res;
	while(ifs >> L >> D >> N)
	{
		caseNo = 1;
		for(i = 0; i < D; ++i)
		{
			ifs >> buf;
			strs[i] = buf;
		}
		for(i = 0; i < N; ++i)
		{
			ifs >> buf;
			index = 0;
			for(k = 0; k < L; ++k)
				cs[k].s.clear();
			for(k = 0; k < buf.size(); ++k)
			{
				if(buf[k] == '(')
				{
					while(buf[++k] != ')')
						cs[index].s.insert(buf[k]);
					++index;
				}
				else
				{
					cs[index++].s.insert(buf[k]);
				}
			}
			res = 0;
			for(k = 0; k < D; ++k)
			{
				buf = strs[k];
				bool flag = true;
				for(r = 0; r < L; ++r)
				{
					if(cs[r].s.count(buf[r]) <= 0)
					{
						flag = false;
						break;
					}
				}
				if(flag)
					++res;
			}
			ofs << "Case #" << caseNo << ": " << res << endl;
			++caseNo;
		}
	}

	return 0;
}