#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

struct Point
{
	int x;
	int y;
};

bool operator < (const Point &a,const Point &b)
{
	if(a.x==b.x)
		return a.y<b.y;
	return a.x<b.x;
}
int main()
{
	int t;
	int n;
	int j;
	vector<Point> coll;
	scanf("%d",&t);
	int result;
	int i;
	int z=0;
	while(t--)
	{
		coll.clear();
		result=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			Point p;
			scanf("%d%d",&p.x,&p.y);
			coll.push_back(p);
		}
		sort(coll.begin(),coll.end());
		for(i=0;i<coll.size();i++)
		{
			for(j=i+1;j<coll.size();j++)
			{
				if(coll[j].y<coll[i].y)
				{
					result++;
				}
			}
		}
		printf("Case #%d: %d\n",++z,result);
	}
	return 0;
}
