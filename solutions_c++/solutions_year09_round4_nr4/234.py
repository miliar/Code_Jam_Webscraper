#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class wateringplants
{
	private:
		struct plant
		{
			public:
				int x,y,r;
				inline plant(int xi=0,int yi=0,int ri=0):x(xi),y(yi),r(ri) {}
				inline double wds(const plant &b)
				{
					return r+b.r+sqrt((x-b.x)*(x-b.x)+(y-b.y)*(y-b.y));
				}
		};
		int n;
		vector<plant> pls;
	public:
		inline wateringplants() {}
		inline void input()
		{
			cin>>n;
			pls.reserve(n);
			int x,y,r;
			for(int f=0;f<n;++f)
			{
				cin>>x>>y>>r;
				pls.push_back(plant(x,y,r));
			}
		}
		inline double solve()
		{
			if(n==1) return pls.at(0).r;
			else if(n==2) return max(pls.at(0).r,pls.at(1).r);
			else return min(min(max(0.+pls.at(0).r,pls.at(1).wds(pls.at(2))/2.),max(0.+pls.at(1).r,pls.at(0).wds(pls.at(2))/2.)),max(0.+pls.at(2).r,pls.at(0).wds(pls.at(1))/2.));
		}
};
int main(void)
{
	int znj;
	cin>>znj;
	cout.setf(ios_base::fixed);
	cout.precision(6);
	for(int f=0;f<znj;++f)
	{
		wateringplants task;
		task.input();
		cout<<"Case #"<<f+1<<": "<<task.solve()<<endl;
	}
	return 0;
}
