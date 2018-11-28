#include<iostream>
#include<vector>
using namespace std;


struct point
{
	double x, y;
	
	bool valid;
	bool operator < (const point & p1) const
	{
		if( x < p1.x)
			return true;
		if( x == p1.x)
			return y < p1.y;
		return false;
	}
	
	bool operator == (const point & p1) const
	{
		return x == p1.x && y == p1.y;
	}
};


point intersection(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4)
{
	double A1 = y2 - y1;
	double B1 = x1 - x2;
	double C1 = A1*x1 + B1*y1;
	
	double A2 = y4 - y3;
	double B2 = x3 - x4;
	double C2 = A2*x3 + B2*y3;
	
    double det = A1*B2 - A2*B1;
    point p;
    if(det == 0)
    {
        //Lines are parallel
        p.valid = false;
		
    }else
    {
        double x = (B2*C1 - B1*C2)/det;
        double y = (A1*C2 - A2*C1)/det;
        p.x = x;
        p.y = y;
        p.valid = false;
        
        if( min(x1,x2) <= x && x <= max(x1,x2) && min(y1,y2) <= y && y <= max(y1,y2) && min(x3,x4) <= x && x <= max(x3,x4) && min(y3,y4) <= y && y <= max(y3,y4) )
        {
        	p.valid = true;
        }
        	
        	
        	
    }
    
    return p;
    
 }
 



int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T;t++)
	{
		int n;
		cin >> n;
		vector<int> left, right;
		for(int i = 0; i < n;i++)
		{
			int a,b;
			cin >> a >> b;
			left.push_back(a);
			right.push_back(b);
		}
		int count = 0;
		for(int i = 0; i < left.size();i++)
		{
			for(int j = i+1; j < left.size();j++)
			{
				point p = intersection(0, left[i], 5, right[i], 0, left[j], 5, right[j]);
				if(p.valid != false)
					count++;
			}
		}
		
		cout << "Case #" << t+1 << ": " << count << endl;
	
	
	}











}
























