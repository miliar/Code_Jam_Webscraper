#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class welcometocodejam
{
	private:
		const uint MOD;
		const string wcj;
		string cs;
	public:
		welcometocodejam():MOD(10000u),wcj("welcome to code jam") {}
		void input()
		{
			getline(cin,cs);
		}
		string solve()
		{
			vector<uint> omm(wcj.size(),0),nmm(wcj.size(),0);
			for(uint f=0;f<cs.size();++f)
			{
				for(uint g=0;g<wcj.size();++g)
				{
					if(cs.at(f)==wcj.at(g))
					{
						if(g==0) nmm.at(0)=1;
						else nmm.at(g)=omm.at(g-1);
					}
				}
				for(uint g=0;g<wcj.size();++g)
				{
					nmm.at(g)+=omm.at(g);
					nmm.at(g)%=MOD;
				}
				omm.clear();
				swap(omm,nmm);
				nmm.resize(wcj.size(),0);
			}
			uint ns=omm.at(wcj.size()-1);
			string sol(4,'0');
			for(int f=3;f>=0;--f,ns/=10)
			{
				sol.at(f)='0'+ns%10;
			}
			return sol;
		}
};
int main(void)
{
	uint znj;
	cin>>znj;
	string dummy;
	getline(cin,dummy);
	for(uint f=0;f<znj;++f)
	{
		welcometocodejam task;
		task.input();
		cout<<"Case #"<<f+1<<": "<<task.solve()<<endl;
	}
	return 0;
}
