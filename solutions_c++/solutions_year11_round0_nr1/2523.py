#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<cstdio>
#include<string>
#include<list>
using namespace std;


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
	
	int t;
	cin >> t;
	for(int c = 1; c <= t; c++)
	{
		int n;
		cin >> n;
		char who;
		int to;
		int otime  = 0, btime  = 0, curtime = 0;
		int oplace = 1, bplace = 1;

		for(int i = 0; i < n; i++)
		{
			cin >> who >> to;
			if(who == 'O')
			{
				int time = abs(oplace - to);
				oplace = to;
				otime = max(otime+time+1, curtime+1);
				curtime = otime;
			}
			else if(who == 'B')
			{
				int time = abs(bplace - to);
				bplace = to;
				btime = max(btime+time+1, curtime+1);
				curtime = btime;
			}
		}






		cout << "Case #" << c << ": " << curtime << endl;
	}





	return 0;
}