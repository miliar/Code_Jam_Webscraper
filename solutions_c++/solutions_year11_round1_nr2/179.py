#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
const int TS=26;
class thekillerword
{
	private:
		int d,m;
		vector<string> dict;
		vector<string> order;
		vector<string> sol;
		string singlesolve(const string ord)
		{
			static map<string,int> compgroup;
			compgroup.clear();
			static vector<string> ckey;
			ckey.clear();
			ckey.resize(d,"");
			static vector<int> cpl;
			cpl.clear();
			cpl.resize(d,0);
			for(int f=0;f<d;++f)
			{
				ckey.at(f)=string('_',dict.at(f).size());
				++compgroup[ckey.at(f)];
			}
			for(int cl=0;cl<TS;++cl)
			{
				char cc=ord.at(cl);
				static set<string> foundcurr;
				foundcurr.clear();
				for(int f=0;f<d;++f)
				{
					bool found=false;
					for(int g=0;g<dict.at(f).size();++g)
					{
						if(dict.at(f).at(g)==cc)
						{
							if(!found)
							{
								found=true;
								foundcurr.insert(ckey.at(f));
							}
						}
					}
				}
				for(int f=0;f<d;++f)
				{
					string nkey=ckey.at(f);
					bool found=false;
					for(int g=0;g<dict.at(f).size();++g)
					{
						if(dict.at(f).at(g)==cc)
						{
							found=true;
							nkey.at(g)=cc;
						}
					}
					if((!found)&&(foundcurr.find(ckey.at(f))!=foundcurr.end()))
					{
						++cpl.at(f);
					}
					--compgroup[ckey.at(f)];
					ckey.at(f)=nkey;
					++compgroup[nkey];
				}
			}
			int cnmp=-1;
			string csol="";
			for(int f=0;f<d;++f)
			{
				if(cpl.at(f)>cnmp)
				{
					cnmp=cpl.at(f);
					csol=dict.at(f);
				}
			}
			return csol;
		}
	public:
		thekillerword() {}
		void input()
		{
			char *buf=new char[TS+5];
			scanf("%d%d",&d,&m);
			dict.reserve(d);
			for(int f=0;f<d;++f)
			{
				scanf("%13s",buf);
				dict.push_back(string(buf));
			}
			order.reserve(m);
			for(int f=0;f<m;++f)
			{
				scanf("%29s",buf);
				order.push_back(string(buf));
			}
			delete[] buf;
		}
		void solve()
		{
			sol.reserve(m);
			for(int f=0;f<m;++f)
			{
				sol.push_back(singlesolve(order.at(f)));
			}
		}
		void output(int caseno)
		{
			printf("Case #%d:",caseno);
			for(vector<string>::iterator fi=sol.begin();fi<sol.end();++fi)
			{
				printf(" %s",fi->c_str());
			}
			printf("\n");
		}
};
int main(void)
{
	int nt;
	scanf("%d",&nt);
	for(int znj=1;znj<=nt;++znj)
	{
		thekillerword task;
		task.input();
		task.solve();
		task.output(znj);
	}
	return 0;
}
