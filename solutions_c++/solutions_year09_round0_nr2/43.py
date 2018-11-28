#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;
const int inf=0x3f3f3f3f;
class watersheds
{
	private:
		int r,c;
		vector<vector<int> > hmap;
		vector<string> sol;
		inline int readht(int x,int y)
		{
			if((x<0)||(y<0)||(x>=r)||(y>=c)) return inf;
			else return hmap.at(x).at(y);
		}
		inline bool reccol(int x,int y,char nc)
		{
			if(sol.at(x).at(y)!=' ') return true;
			int lph=hmap.at(x).at(y);
			for(int f=-1;f<=1;++f)
			{
				for(int g=-1;g<=1;++g)
				{
					if((f==g)||(f==-g)) continue;
					lph=min(lph,readht(x+f,y+g));
				}
			}
			if(lph>=hmap.at(x).at(y))
			{
				sol.at(x).at(y)=nc;
				return false;
			}
			else
			{
				for(int f=-1;f<=1;++f)
				{
					for(int g=-1;g<=1;++g)
					{
						if((f==g)||(f==-g)) continue;
						if(readht(x+f,y+g)==lph)
						{
							if(reccol(x+f,y+g,nc))
							{
								sol.at(x).at(y)=sol.at(x+f).at(y+g);
								return true;
							}
							else
							{
								sol.at(x).at(y)=nc;
								return false;
							}
						}
					}
				}
			}
			throw 42;
		}
	public:
		watersheds() {}
		void input()
		{
			cin>>r>>c;
			hmap.resize(r,vector<int>(c,0));
			for(int f=0;f<r;++f)
			{
				for(int g=0;g<c;++g)
				{
					cin>>hmap.at(f).at(g);
				}
			}
		}
		void solve()
		{
			sol.resize(r,string(c,' '));
			char ccch='a';
			for(int f=0;f<r;++f)
			{
				for(int g=0;g<c;++g)
				{
					if(!(reccol(f,g,ccch))) ++ccch;
				}
			}
		}
		void output()
		{
			for(int f=0;f<r;++f)
			{
				cout<<sol.at(f).at(0);
				for(int g=1;g<c;++g)
				{
					cout<<" "<<sol.at(f).at(g);
				}
				cout<<endl;
			}
		}
};
int main(void)
{
	int znj;
	cin>>znj;
	for(int f=0;f<znj;++f)
	{
		watersheds task;
		task.input();
		task.solve();
		cout<<"Case #"<<f+1<<":"<<endl;
		task.output();
	}
	return 0;
}
