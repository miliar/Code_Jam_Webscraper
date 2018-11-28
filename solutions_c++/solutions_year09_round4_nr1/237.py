#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class crazyrows
{
	private:
		int n;
		vector<string> mtx;
	public:
		inline crazyrows() {}
		inline void input()
		{
			cin>>n;
			mtx.resize(n);
			for(int f=0;f<n;++f)
			{
				cin>>mtx.at(f);
			}
		}
		inline int solve()
		{
			vector<int> hp1(n);
			for(int f=0;f<n;++f)
			{
				for(int g=0;g<n;++g)
				{
					if(mtx.at(f).at(g)=='1')
					{
						hp1.at(f)=g;
					}
				}
			}
			int sol=0;
			for(int f=0;f<n;++f)
			{
				for(int g=f;g<n;++g)
				{
					if(hp1.at(g)<=f)
					{
						for(;g>f;--g)
						{
							swap(hp1.at(g-1),hp1.at(g));
							++sol;
						}
						break;
					}
				}
			}
			return sol;
		}
};
int main(void)
{
	int znj;
	cin>>znj;
	for(int f=0;f<znj;++f)
	{
		crazyrows task;
		task.input();
		cout<<"Case #"<<f+1<<": "<<task.solve()<<endl;
	}
	return 0;
}
