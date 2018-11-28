#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <vector>
using namespace std;


ifstream in("B-large.in");
ofstream out("B-large.out");
// ifstream in(stdin);
// ofstream out(stdout);

struct two
{
	char first;
	char second;
	two(char f,char s):first(f),second(s){}

	friend bool operator < (const two & ls, const two &rs)

	{

		return ls.first < rs.first || (ls.first == rs.first && ls.second < rs.second);

	}



};

int main()
{
	int t;
	int c,d,n;
	in>>t;
	for(int ii=1;ii<=t;ii++)
	{
		char str[105];
		vector<char> ans;
		map<two,char> comb;
		set<two> oppo;
		in>>c;
		for (int i=0;i<c;i++)
		{
			char c1,c2,c3;
			in>>c1>>c2>>c3;
			if(c1 > c2)
			{
				char c4 = c1;
				c1 = c2;
				c2 = c4;
			}
			two tt(c1,c2);
			comb[tt] = c3;
		}
		in>>d;
		for (int i=0;i<d;i++)
		{
			char c1,c2;
			in>>c1>>c2;
			if(c1 > c2)
			{
				char c4 = c1;
				c1 = c2;
				c2 = c4;
			}
			two tt(c1,c2);
			oppo.insert(tt);
		}
		in>>n>>str;
		ans.push_back(str[0]);
		int start = 0;
		for (int i=1;i<n;i++)
		{
			char last = str[i-1];
			char now = str[i];
			if (last > now)
			{
				char tmp = now;
				now = last;
				last = tmp;
			}
			two tt(last,now);
			map<two,char>::iterator it = comb.find(tt);
			if (it != comb.end())
			{
				ans.pop_back();
				ans.push_back(it->second);
				str[i] = it->second;
				str[i-1] = '\0';
			}
			else
				ans.push_back(str[i]);

			for (int j=start;j<i;j++)
			{
				char before = str[j];
				now = str[i];
				if (before > now)
				{
					char tmp = now;
					now = before;
					before = tmp;
				}
				two ttt(before,now);
				set<two>::iterator it = oppo.find(ttt);
				if (it != oppo.end())
				{
					ans.clear();
					str[i] = '\0';
					start = i+1;
					break;
				}
			}
		}

		out<<"Case #"<<ii<<": "<<"[";
		if (ans.size() > 0)
		{
			out<<ans[0];
			if (ans.size() > 1)
			{
				out<<",";
			}
			for (int k=1;k<ans.size()-1;k++)
			{
				out<<" "<<ans[k]<<",";
			}
			if(ans.size()>1)
				out<<" "<<ans.back();
		}
		out<<"]"<<endl;

	}
	//system("pause");
	return 0;
}