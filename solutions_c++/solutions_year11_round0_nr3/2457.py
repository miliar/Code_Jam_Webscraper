#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
using namespace std;
class candysplitting
{
	private:
		int n;
		vector<int> candy;
		int sol;
	public:
		candysplitting() {}
		void input()
		{
			scanf("%d",&n);
			candy.reserve(n);
			int x;
			for(int f=0;f<n;++f)
			{
				scanf("%d",&x);
				candy.push_back(x);
			}
		}
		void solve()
		{
			int ixor=0;
			for(vector<int>::iterator fi=candy.begin();fi<candy.end();++fi)
			{
				ixor^=(*fi);
			}
			if(ixor==0)
			{
				sol=accumulate(candy.begin(),candy.end(),0)-*min_element(candy.begin(),candy.end());
			}
			else
			{
				sol=-1;
			}
		}
		void output(int caseno)
		{
			if(sol>=0)
			{
				printf("Case #%d: %d\n",caseno,sol);
			}
			else
			{
				printf("Case #%d: NO\n",caseno);
			}
		}
};
int main(void)
{
	int nt;
	scanf("%d",&nt);
	for(int znj=1;znj<=nt;++znj)
	{
		candysplitting task;
		task.input();
		task.solve();
		task.output(znj);
	}
	return 0;
}
