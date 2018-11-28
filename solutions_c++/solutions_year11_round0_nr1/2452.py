#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
typedef pair<bool,int> pbi;
class bottrust
{
	private:
		int n;
		vector<pbi> moves;
		int sol;
		void moverobot(int &sol,int npos,int &lpos,int &ltime)
		{
			int mtime=ltime+abs(npos-lpos);
			if(mtime<sol)
			{
				mtime=sol;
			}
			++mtime;
			ltime=mtime;
			sol=mtime;
			lpos=npos;
		}
	public:
		bottrust() {}
		void input()
		{
			scanf("%d",&n);
			moves.reserve(n);
			char rid;
			int rmp;
			for(int f=0;f<n;++f)
			{
				scanf(" %c%d",&rid,&rmp);
				--rmp;
				moves.push_back(pbi((rid=='B'),rmp));
			}
		}
		void solve()
		{
			sol=0;
			int bpos=0,opos=0;
			int btime=0,otime=0;
			for(vector<pbi>::iterator fi=moves.begin();fi<moves.end();++fi)
			{
				if(fi->first)
				{
					moverobot(sol,fi->second,bpos,btime);
				}
				else
				{
					moverobot(sol,fi->second,opos,otime);
				}
			}
		}
		void output(int caseno)
		{
			printf("Case #%d: %d\n",caseno,sol);
		}
};
int main(void)
{
	int nt;
	scanf("%d",&nt);
	for(int znj=1;znj<=nt;++znj)
	{
		bottrust task;
		task.input();
		task.solve();
		task.output(znj);
	}
	return 0;
}
