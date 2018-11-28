#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

char seq[100];
int loc[100];

int main()
{
	int n;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		int num;
		cin >> num;
		for(int j=0;j<num;j++)
		{
			cin >> seq[j] >> loc[j];
		}
		int np = 0, t=0;
		int oloc = 0, ol = 1;
		int bloc = 0, bl = 1;
		while(oloc<num&&seq[oloc]=='B') oloc++;
		while(bloc<num&&seq[bloc]=='O') bloc++;
		while(np!=num)
		{
			int usetime;
			if(oloc<bloc && oloc < num)
			{
				usetime = abs(loc[oloc]-ol)+1;
				ol = loc[oloc];
				if(abs(bl-loc[bloc])<=usetime)
				{
					bl = loc[bloc];
				}
				else if(loc[bloc]>bl)
				{
					bl+=usetime;
				}
				else
					bl-=usetime;
				oloc++;
				while(oloc<num&&seq[oloc]=='B') oloc++;
				t += usetime;
				np++;
			}
			else if(bloc < oloc && bloc < num)
			{
				usetime = abs(loc[bloc]-bl)+1;
				bl = loc[bloc];
				if(abs(ol-loc[oloc])<=usetime)
				{
					ol = loc[oloc];
				}
				else if(loc[oloc]>ol)
				{
					ol+=usetime;
				}
				else
					ol-=usetime;
				bloc++;
				while(bloc<num&&seq[bloc]=='O') bloc++;
				t += usetime;
				np++;
			}
		}
		cout << "Case #" << i+1 << ": ";
		cout << t << endl;
	}
}
