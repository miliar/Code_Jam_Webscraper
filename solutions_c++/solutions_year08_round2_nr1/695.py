#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

template<typename T1, typename T2> T1 cast(const T2 &v) 
{ 
	T1 ret; 
	stringstream s; 
	s << v; 
	s.seekg(O); 
	s >> ret; 
	return ret; 
} 

int main()
{
	int ca, n, a, b, c, d, x0, y0, m;
	long long int x, y;
	int rst =0;

	vector < pair<long long int,long long int> > data;

	cin >> ca;

	for(int i=1; i<=ca ; ++i)
	{
		rst = 0;
		data.clear();
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;

		data.push_back(make_pair(x0, y0));

		x = x0; y = y0;

		for(int j=1; j< n; ++j)
		{
			data.push_back(make_pair((x*a+b)%m, (y*c+d)%m));

			x = (x*a+b)%m;
			y = (y*c+d)%m;
		}
		

		for(int i1=0; i1 < data.size(); i1++)
		{
			for(int i2=i1+1; i2 < data.size(); ++i2)
			{
				for(int i3=i2+1; i3< data.size(); ++i3)
				{
					if((data[i1].first + data[i2].first + data[i3].first)%3 == 0 &&
						(data[i1].second + data[i2].second + data[i3].second) %3 == 0)
						rst++;
				}
			}
		}

		cout << "Case #" << i << ": " << rst << endl;

	}
	return 0;
}
