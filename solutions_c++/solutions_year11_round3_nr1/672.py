#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <fstream>
#include <algorithm>
#include <memory.h>

using namespace std;

vector<string> vs;

bool Check()
{
	int sum=0;
	for(int i=0; i<vs.size(); i++)
	{
		sum += count(vs[i].begin(), vs[i].end() , '#');
	}
	if(sum % 4)
		return false;
	if(sum == 0)
		return true;
	int cnt;
	for(int i=0; i<vs.size(); i++)
	{
		cnt = 0;
		for(int j=0; j<vs[i].size(); j++)
			if(vs[i][j] == '#' && cnt%2 == 0)
			{
				if(vs[i+1][j] == '#')
					vs[i][j] = '/', vs[i+1][j] = '\\', cnt ++;
				else
					return false;
			}
			else if(vs[i][j] == '#' && cnt%2 != 0)
			{
				if(vs[i+1][j] == '#')
					vs[i][j] = '\\', vs[i+1][j] = '/', cnt ++;
				else
					return false;
			}
		
		if(cnt %2)
			return false;
	}
	return true;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("aLout.txt", "w", stdout);
	int cas;
	cin >> cas;
	for(int ca=1; ca<=cas; ca++)
	{
		vs.clear();
		cout << "Case #" << ca <<":" << endl;
		int R, C;
		cin >> R >> C;
		for(int i=0; i<R; i++)
		{
			string str;
			cin >>str;
			vs.push_back(str);
		}
		if(Check())
		{
			for(int i=0; i<vs.size(); i++)
				cout << vs[i] << endl;
		}
		else
			cout << "Impossible" << endl;
	}
	return 0;
}
