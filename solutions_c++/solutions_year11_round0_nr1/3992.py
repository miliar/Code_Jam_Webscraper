#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int t;
	cin >> t;
	for (int d=1;d<=t;++d)
	{
		int n;
		cin >> n;
		int ans=0;
		int x=1,y=1;
		string s="O";
		int t1=0,t2=0;
		vector < int > o,b;
		for (int f=0;f<n;++f)
		{
			string stemp; int temp;
			cin >> stemp >> temp;
			if (stemp=="O")
			{
				int time=abs(temp-x)+1;
				ans+=time;
				if (s=="O")
					t1+=time;
				else
				{
					s="O";
					ans-=min(time-1,t2);
					t1=max(time-t2-1,0)+1;
					t2=0;
				}
				x=temp;
			}
			else
			{
				int time=abs(temp-y)+1;
				ans+=time;
				if (s=="B")
					t2+=time;
				else
				{
					s="B";
					ans-=min(time-1,t1);
					t2=max(time-t1-1,0)+1;
					t1=0;
				}
				y=temp;
			}
		}
		cout << "Case #" << d << ": " << ans << '\n';
	}
	return 0;
}