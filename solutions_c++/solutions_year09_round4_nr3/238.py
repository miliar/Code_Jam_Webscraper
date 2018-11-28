#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
using namespace std;
class stockcharts
{
	private:
		int n,k;
		vector<vector<int> > stls;
		vector<vector<int> > ptmts;
		vector<int> mtch;
		vector<bool> done;
		inline bool dfsmatch(int p)
		{
			if(done.at(p)) return false;
			done.at(p)=true;
			for(vector<int>::iterator fi=ptmts.at(p).begin();fi<ptmts.at(p).end();++fi)
			{
				if(mtch.at(*fi)<0)
				{
					mtch.at(*fi)=p;
					return true;
				}
				else if(dfsmatch(mtch.at(*fi)))
				{
					mtch.at(*fi)=p;
					return true;
				}
			}
			return false;
		}
	public:
		inline stockcharts() {}
		inline void input()
		{
			cin>>n>>k;
			stls.resize(n,vector<int>(k));
			for(int f=0;f<n;++f)
			{
				for(int g=0;g<k;++g)
				{
					cin>>stls.at(f).at(g);
				}
			}
		}
		inline int solve()
		{
			ptmts.resize(n);
			for(int f=0;f<n;++f)
			{
				for(int g=0;g<n;++g)
				{
					if(f==g) continue;
					bool mok=true;
					for(int h=0;h<k;++h)
					{
						if(stls.at(f).at(h)>=stls.at(g).at(h))
						{
							mok=false;
							break;
						}
					}
					if(mok)
					{
						ptmts.at(f).push_back(g);
					}
				}
			}
			mtch.resize(n,-1);
			int nms=0;
			for(int f=0;f<n;++f)
			{
				done.clear();
				done.resize(n,false);
				if(dfsmatch(f)) ++nms;
			}
			return n-nms;
		}
};
int main(void)
{
	int znj;
	cin>>znj;
	for(int f=0;f<znj;++f)
	{
		stockcharts task;
		task.input();
		cout<<"Case #"<<f+1<<": "<<task.solve()<<endl;
	}
	return 0;
}
