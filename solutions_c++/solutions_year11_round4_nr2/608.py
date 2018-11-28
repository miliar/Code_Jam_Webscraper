#include <cstdlib>
#include <cctype>
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <assert.h>

using namespace std;

bool isCentered(const vector<vector<int> > mass,int startRow,int startCol,int s)
{
	s--;

	long long test1=0;
	long long test2=0;
	for(int r=0;r<=s;r++)
	{
		for(int c=0;c<=s;c++)
		{
			if(r==0 && c==0)
			{
				continue;
			}
			if(r==0 && c==s)
			{
				continue;
			}
			if(r==s && c==0)
			{
				continue;
			}
			if(r==s && c==s)
			{
				continue;
			}

			test1+=((2*r-s)*mass[r+startRow][c+startCol]);
			test2+=((2*c-s)*mass[r+startRow][c+startCol]);
		}
	}

	return test1==0 && test2==0;
}

int main()
{
	ifstream cin("C:\\Users\\Bryan\\Desktop\\TestFile.in");
	ofstream cout("C:\\Users\\Bryan\\Desktop\\Output.txt");

	int T;
	cin >> T;

	for(int counter=1;counter<=T;counter++)
	{
		int R,C,D;
		cin >> R >> C >> D;

		vector<vector<int> > mass;
		for(int r=0;r<R;r++)
		{
			vector<int> line;
			mass.push_back(line);

			for(int c=0;c<C;c++)
			{
				char i;
				cin >> i;
				mass[r].push_back((int)(i-'0'));
			}
		}

		int ans=0;
		for(int r=0;r<R;r++)
		{
			for(int c=0;c<C;c++)
			{
				for(int s=max(3,ans+1);s<=min(R-r,C-c);s++)
				{
					if(isCentered(mass,r,c,s))
					{
						ans=s;
					}
				}
			}
		}

		cout << "Case #" << counter << ": ";
		if(ans==0)
		{
			cout << "IMPOSSIBLE";
		}
		else
		{
			cout << ans;
		}
		cout << '\n';
	}

	return 0;
}