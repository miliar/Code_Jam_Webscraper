#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <cstring>
#include <string>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define pb push_back
#define mp make_pair
#define S second
#define F first
#define INF 2000000000
#define MEMSET_INF 127

char m[4][4];

int main(int argc, char const *argv[])
{
	int n;
	cin>>n;
	//getchar();
	char win;
	int point;
	char current;


	for (int i = 0; i < n; ++i)
	{
		point=0;

		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>m[j][k];
				if(m[j][k]=='.')
					point=1;
			}
			//getchar();
		}


		for (int j = 0; j < 4; ++j)
		{
			win=1;
			current='.';
			for (int k = 0; k < 4; ++k)
			{
				if(m[j][k]=='.')
				{
					win=0;
					break;
				}
				else if (current=='.')
				{
					if(m[j][k]!='T')
						current=m[j][k];
				}
				else
				{
					if(m[j][k]!='T')
						if(current!=m[j][k])
						{
							win=0;
							break;
						}
				}

			}
			if(win)
			{
				win=current;
				break;
			}
		}

		if(!win)
		for (int j = 0; j < 4; ++j)
		{
			win=1;
			current='.';
			for (int k = 0; k < 4; ++k)
			{
				if(m[k][j]=='.')
				{
					win=0;
					break;
				}
				else if (current=='.')
				{
					if(m[k][j]!='T')
						current=m[k][j];
				}
				else
				{
					if(m[k][j]!='T')
						if(current!=m[k][j])
						{
							win=0;
							break;
						}
				}

			}
			if(win)
			{
				win=current;
				break;
			}
		}
		if(!win)
		{
			win=1;
			current='.';
			for (int k = 0; k < 4; ++k)
			{
				if(m[k][k]=='.')
				{
					win=0;
					break;
				}
				else if (current=='.')
				{
					if(m[k][k]!='T')
						current=m[k][k];
				}
				else
				{
					if(m[k][k]!='T')
						if(current!=m[k][k])
						{
							win=0;
							break;
						}
				}
			}
			if(win)
			{
				win=current;
			}
		}

		if(!win)
		{
			win=1;
			current='.';
			for (int k = 0; k < 4; ++k)
			{
				if(m[k][3-k]=='.')
				{
					win=0;
					break;
				}
				else if (current=='.')
				{
					if(m[k][3-k]!='T')
						current=m[k][3-k];
				}
				else
				{
					if(m[k][3-k]!='T')
						if(current!=m[k][3-k])
						{
							win=0;
							break;
						}
				}

			}
			if(win)
			{
				win=current;
			}
		}

		if(win)
			printf("Case #%d: %c won\n", i+1,win);
		else if(point)
			printf("Case #%d: Game has not completed\n", i+1);
		else
			printf("Case #%d: Draw\n", i+1);



	}
	return 0;
}
