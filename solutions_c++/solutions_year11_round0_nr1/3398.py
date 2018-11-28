#include<stdio.h>
#include<string>
#include<sstream>
#include<vector>
#include<iostream>

using namespace std;

int main()
{
	int ncase,ccase;
	char c;
	int x,y,z;
	int cs,ts,t,act;
	int posO,posB,csO,csB;
	vector<int> O,B,Os,Bs;
	stringstream ss;
	string s;
	
	cin >> ncase;
	getline(cin,s);
	for(ccase = 1;ccase <= ncase;ccase++)
	{
		cin >> y;
		ts = 0;
		O.clear();
		B.clear();
		Os.clear();
		Bs.clear();
		while(y > 0)
		{
			cin >> c >> x;
			if(c == 'O')
			{
				O.push_back(x);
				Os.push_back(ts);
			}
			else if(c == 'B')
			{
				B.push_back(x);
				Bs.push_back(ts);
			}
			y--;
			ts++;
		}
		
		t = 0;
		cs = 0;
		posO = 1;
		posB = 1;
		csO = 0;
		csB = 0;
		while(cs < ts)
		{
			act = 0;
			if(csO < O.size())
			{
				if(cs == Os[csO])
				{
					if(posO == O[csO])
					{
						cs++;
						csO++;
						act = 1;
					}
					else
					{
						if(posO > O[csO]) posO--;
						else if(posO < O[csO]) posO++;
					}
				}
				else
				{
					if(posO > O[csO]) posO--;
					else if(posO < O[csO]) posO++;
				}
			}
			if(csB < B.size())
			{
				if(cs == Bs[csB])
				{
					if(posB == B[csB] && act == 0)
					{
						cs++;
						csB++;
					}
					else
					{
						if(posB > B[csB]) posB--;
						else if(posB < B[csB]) posB++;
					}
				}
				else
				{
					if(posB > B[csB]) posB--;
					else if(posB < B[csB]) posB++;
				}
			}
			t++;
		}
		
		cout << "Case #" << ccase << ": ";
		cout << t << endl;
	}

    while(getchar()!=EOF);
    return 0;
}
