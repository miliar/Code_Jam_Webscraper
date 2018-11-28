#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
class magicka
{
	private:
		int c,d,n;
		map<int,char> produce;
		set<int> oppose;
		string incant;
		vector<char> sol;
		int charmask(char a,char b)
		{
			if(a>b)
			{
				swap(a,b);
			}
			return (a<<8)|b;
		}
		bool stackconflict(char ac)
		{
			for(vector<char>::iterator fi=sol.begin();fi<sol.end();++fi)
			{
				if(oppose.find(charmask(ac,*fi))!=oppose.end())
				{
					return true;
				}
			}
			return false;
		}
		void addtostack(char ac)
		{
			if(sol.empty())
			{
				sol.push_back(ac);
				return;
			}
			else
			{
				char tr=produce[charmask(ac,sol.back())];
				if(tr!='\0')
				{
					sol.pop_back();
					sol.push_back(tr);
				}
				else
				{
					if(stackconflict(ac))
					{
						sol.clear();
					}
					else
					{
						sol.push_back(ac);
					}
				}
			}
		}
	public:
		magicka() {}
		void input()
		{
			char *buf=new char[5];
			scanf("%d",&c);
			for(int f=0;f<c;++f)
			{
				scanf("%4s",buf);
				produce[charmask(buf[0],buf[1])]=buf[2];
			}
			scanf("%d",&d);
			for(int f=0;f<d;++f)
			{
				scanf("%4s",buf);
				oppose.insert(charmask(buf[0],buf[1]));
			}
			scanf("%d",&n);
			delete[] buf;
			buf=new char[n+3];
			scanf("%s",buf);
			incant=buf;
			delete[] buf;
		}
		void solve()
		{
			sol.clear();
			for(int f=0;f<n;++f)
			{
				addtostack(incant.at(f));
			}
		}
		void output(int caseno)
		{
			printf("Case #%d: [",caseno);
			for(unsigned int f=0;f<sol.size();++f)
			{
				if(f>0)
				{
					printf(", ");
				}
				printf("%c",sol.at(f));
			}
			printf("]\n");
		}
};
int main(void)
{
	int nt;
	scanf("%d",&nt);
	for(int znj=1;znj<=nt;++znj)
	{
		magicka task;
		task.input();
		task.solve();
		task.output(znj);
	}
	return 0;
}
