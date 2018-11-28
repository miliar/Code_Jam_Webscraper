//#include <iostream>
#include <stdio.h>
//#include <math.h>
//#include <iomanip>
#include <utility>
#include <vector>

using namespace std;

vector<pair<int, int> > pp;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	__int64 a, b, c, d, x0, y0, m, x, y;
	int n, size, times=0, total, i, j, k;
	pair<int, int> p;
	//cin>>size;
	scanf("%d",&size);
	while(times++ < size)
	{
		//cin>>n>>a>>b>>c>>d>>x0>>y0>>m;
		scanf("%d%I64u%I64u%I64u%I64u%I64u%I64u%I64u",&n,&a,&b,&c,&d,&x0,&y0,&m);
		pp.clear();
		total=0;
		p.first=x0;
		p.second=y0;
		pp.push_back(p);
		x = x0;
		y = y0;
		//cout<<x<<' '<<y<<endl;
		for(i=1;i<=n-1;i++)
		{
			x = (a * x + b) % m;
			y = (c * y + d) % m;
			//cout<<x<<' '<<y<<endl;
			p.first = x;
			p.second = y;
			pp.push_back(p);
		}
		for(i=0;i<n-2;i++)
		{
			for(j=i+1;j<n-1;j++)
			{
				for(k=j+1;k<n;k++)
				{
					if((pp[i].first+pp[j].first+pp[k].first)%3==0)
						if((pp[i].second+pp[j].second+pp[k].second)%3==0)
							total++;
				}
			}
		}

		//cout<<"Case #"<<times<<""<<total<<endl;
		printf("Case #%d: %d\n",times,total);
	}

	
	return 0;
}
