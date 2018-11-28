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

const int INF=99999;
vector<vector<int> > connection;
vector<bool> wasVisited;

bool canConquer(int location, int MAX, int depth)
{
	if(depth>MAX)
	{
		return false;
	}

	for(int c=0;c<(int)connection[location].size();c++)
	{
		if(connection[location][c]==1)
		{
			return true;
		}
	}

	for(int c=0;c<(int)connection[location].size();c++)
	{
		if(!wasVisited[connection[location][c]])
		{
			wasVisited[connection[location][c]]=true;
			if(canConquer(connection[location][c],MAX,depth+1))
			{
				wasVisited[connection[location][c]]=false;
				return true;
			}
			wasVisited[connection[location][c]]=false;
		}
	}

	return false;
}

int evaluation(int location)
{
	bool valid=false;
	for(int c=0;c<(int)connection[location].size();c++)
	{
		if(connection[location][c]==1)
		{
			valid=true;
			break;
		}
	}
	if(!valid)
	{
		return 0;
	}

	vector<bool> canReach;
	for(int c=0;c<(int)wasVisited.size();c++)
	{
		canReach.push_back(false);
	}

	for(int c=0;c<(int)wasVisited.size();c++)
	{
		if(wasVisited[c])
		{
			for(int n=0;n<(int)connection[c].size();n++)
			{
				canReach[connection[c][n]]=true;
			}
		}
	}

	int ans=0;
	for(int c=0;c<(int)wasVisited.size();c++)
	{
		if(!wasVisited[c] && canReach[c])
		{
			ans++;
		}
	}

	return ans;
}

int maxThreaten(int location, int MAX, int depth)
{
	if(depth==MAX)
	{
		return evaluation(location);
	}

	int ans=0;
	for(int c=0;c<(int)connection[location].size();c++)
	{
		if(!wasVisited[connection[location][c]])
		{
			wasVisited[connection[location][c]]=true;
			ans=max(ans,maxThreaten(connection[location][c],MAX,depth+1));
			wasVisited[connection[location][c]]=false;
		}
	}

	return ans;
}
int main()
{
	ifstream cin("C:\\Users\\Bryan\\Desktop\\TestFile.in");
	ofstream cout("C:\\Users\\Bryan\\Desktop\\Output.txt");

	int T;
	cin >> T;

	for(int counter=1;counter<=T;counter++)
	{
		int P,W;
		cin >> P >> W;

		connection.clear();
		vector<int> blank;
		for(int c=0;c<P;c++)
		{
			connection.push_back(blank);
		}

		for(int c=0;c<W;c++)
		{
			int x,y;
			char comma;
			cin >> x >> comma >> y;
			connection[x].push_back(y);
			connection[y].push_back(x);
		}

		wasVisited.clear();
		for(int c=0;c<P;c++)
		{
			wasVisited.push_back(false);
		}
		wasVisited[0]=true;

		int minConquers=0;
		while(!canConquer(0,minConquers,0))
		{
			minConquers++;
		}

		int threats=maxThreaten(0,minConquers,0);

		cout << "Case #" << counter << ": " << minConquers << ' ' << threats << '\n';
	}

	return 0;
}