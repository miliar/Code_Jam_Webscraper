#include<iostream>
#include<set>
#include<map>
#include<string>
using namespace std;
set<char> base;
int T,C,D,N;
string combine;
string oppose;
string seq;
char res[100];
int main()
{
	base.insert('Q');
	base.insert('W');
	base.insert('E');
	base.insert('R');
	base.insert('A');
	base.insert('S');
	base.insert('D');
	base.insert('F');
	cin >> T;
	int casenum = 1;
	for (casenum = 1;casenum <= T;++casenum)
	{
		map<string,char> combinemap;
		set<string> opposeset; 
		cin >> C;
		getchar();
		for (int i = 0;i < C;++i)
		{
			cin >> combine;
			string s = combine.substr(0,2);
			combinemap[s] = combine[2];
			char c = s[0];
			s[0] = s[1];
			s[1] = c;
			combinemap[s] = combine[2];
		}
		cin >> D;
		for (int i = 0;i < D;++i)
		{
			cin >> oppose;
			opposeset.insert(oppose);
			reverse(oppose.begin(),oppose.end());
			opposeset.insert(oppose);
		}
		cin >> N;
		cin >> seq;
		res[0] = seq[0];
		char tc[2];
		string ts;
		int idx = 0;
		for (int i = 1;i < N;++i)
		{
			if(idx < 0)
			{
				res[++idx] = seq[i];
				continue;
			}
			tc[1] = seq[i];
			tc[0] = res[idx];
			ts = string(tc,2);
			map<string,char>::iterator it = combinemap.find(ts);
			if (it != combinemap.end())
			{
				res[idx] = (*it).second;
			}
			else
			{
				bool flag = false;
				for (int j = 0;j <= idx;++j)
				{
					tc[0] = res[j];
					ts = string(tc,2);
					set<string>::iterator sit = opposeset.find(ts);
					if (sit != opposeset.end())
					{
						idx = -1;
						flag = true;
						break;
					}
				}
				if (!flag)
				{
					res[++idx] = seq[i];
				}
			}
		}
		printf("Case #%d: [",casenum);
		for (int i = 0;i <= idx;++i)
		{
			if (i == 0)
			{
				printf("%c",res[i]);
				continue;
			}
			printf(", %c",res[i]);
		}
		printf("]\n");
	}
	return 0;
}