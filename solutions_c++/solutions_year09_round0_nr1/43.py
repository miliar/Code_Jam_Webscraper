#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;
class alienlanguage
{
	private:
		int l,d,n;
		vector<string> dict,pat;
		vector<int> sol;
	public:
		alienlanguage() {}
		void input()
		{
			cin>>l>>d>>n;
			dict.resize(d);
			for(int f=0;f<d;++f)
			{
				cin>>dict.at(f);
			}
			pat.resize(n);
			for(int f=0;f<n;++f)
			{
				cin>>pat.at(f);
			}
		}
		void solve()
		{
			sol.resize(n,d);
			for(int f=0;f<n;++f)
			{
				vector<bool> app(d,true);
				string::iterator gi=pat.at(f).begin();
				for(int h=0;h<l;++h)
				{
					if((*gi)=='(')
					{
						vector<bool> plet(26,false);
						for(++gi;(*gi)!=')';++gi)
						{
							plet.at((*gi)-'a')=true;
						}
						for(int i=0;i<d;++i)
						{
							if(!(plet.at(dict.at(i).at(h)-'a')))
							{
								if(app.at(i))
								{
									--sol.at(f);
									app.at(i)=false;
								}
							}
						}
					}
					else
					{
						for(int i=0;i<d;++i)
						{
							if(dict.at(i).at(h)!=(*gi))
							{
								if(app.at(i))
								{
									--sol.at(f);
									app.at(i)=false;
								}
							}
						}
					}
					++gi;
				}
			}
		}
		void output()
		{
			for(int f=0;f<n;++f)
			{
				cout<<"Case #"<<f+1<<": "<<sol.at(f)<<endl;
			}
		}
};
int main(void)
{
	alienlanguage task;
	task.input();
	task.solve();
	task.output();
	return 0;
}
