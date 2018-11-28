#include <iostream>
#include <vector>

using namespace std;

class LeaguePicks //只需要这个类就可以了

{
	
public:
	
	vector <int> returnPicks(int a,int b,int c) //需要这个method
		
	{
		
		vector <int> ret;
		
		int i;
		
		if (c>=a) ret.push_back (a); else return ret;
		
		if (c>=2*b-a+1) ret.push_back(2*b-a+1);
		
		for (i=0;;i++)
			
			if (2*b<=c)
			{
				ret.push_back(2*b);
				b=2*b;
			}
			
			else return ret;
			
			return ret;
			
	}
	
};

int main()
{
	LeaguePicks p;
	vector<int>a;
	a=p.returnPicks(3,6,20);
	for(int i=0;a[i]!='\0';++i)
		cout<<a[i]<<" ";
}