#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class pts
{
	public:
		
	int a;
	int b;
	
	pts(int c, int d)
	{
		a = c;
		b = d;
	}
	
	bool equals(pts& c)
	{
		return (a == c.a && b == c.b);
	}
};

bool check_a(pts c, pts d)
{
	return c.a > d.a;
}

bool check_b(pts c, pts d)
{
	return c.b > d.b;
}

int main()
{
	vector<pts> c;
	
	int t;
	cin>>t;
	
	for(int i = 1; i <= t; i++)
	{
		int n;
		cin>>n;
		
		for(int j=0; j < n ;j++)
		{
			int a, b;
			cin>>a;
			cin>>b;
			
			pts obj(a, b);
			
			c.push_back(obj);
		}
		
		if(n == 1)
			cout<<"Case #"<<i<<": 0\n";
		else
		{//Count them
			vector<pts> copy = c;
			
			int intersections = 0;
		
			sort(c.begin(), c.end(), check_a);
			
			sort(copy.begin(), copy.end(), check_b);
			
			for(int k = 0; k < c.size(); k++)
			{
				int diff = 0;
				
				for(int l = k; l < copy.size(); l++)
				{
					if(c[k].equals(copy[l]))
					{
						diff = l - k;
						break;
					}
				}
				
				intersections += diff;
			}
			
			cout<<"Case #"<<i<<": "<<intersections<<"\n";
		}
		
		c.clear();
	}
	
	return 0;
}