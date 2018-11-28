#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

int main()
{
	
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	
	int N,C,s,time=0,posO = 1,posB = 1, timeO = 0, timeB = 0;
	char t;
	cin >> N;
	
	for(int testcase = 0; testcase<N;testcase++)
	{
		time=0;posO = 1;posB = 1; timeO = 0; timeB = 0;
		
		cin >> C;
		for(int com = 0;com<C;com++)
		{
				cin >> t >> s;
				if (t == 'O')
				{
					int needed = abs(s-posO) + 1 - timeO;
					if (needed < 1) needed = 1;
					time += needed;
					timeO = 0;
					timeB += needed;
					posO = s;
					//cout << "needed " << needed << endl;  
				}
				else
				{
					int needed = abs(s-posB) + 1 - timeB;
					if (needed < 1) needed = 1;
					time += needed;
					timeB = 0;
					timeO += needed;
					posB= s;
					//cout << "needed " << needed << endl;  
				}
		}
		
		cout << "Case #" << testcase+1 << ": ";
		
		
		cout << time <<endl;
		
	}
	
	
	fcloseall();
return 0;
}
