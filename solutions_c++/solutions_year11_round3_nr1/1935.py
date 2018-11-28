#include <iostream>
#include <fstream>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <memory>
#include <sstream>

using namespace std;

int T, t, r,c;

char data[50][50];

bool CheckValid(int i, int j)
{
	if(i + 1 >= r || j + 1 >= c) return false;

	if(data[i][j] != '#' || data[i + 1][j] != '#' || data[i][j + 1] != '#' || data[i + 1][j + 1] != '#')
		return false;
	data[i][j] =  data[i + 1][j + 1] = '/';
	data[i + 1][j] = data[i][j + 1] = '\\';
	return true;
}

int main()
{
	freopen("D://1.in", "rb", stdin);
	freopen("D://1.out", "wb", stdout);
	int i,j;
	bool result;
	cin >> T;
	for(t = 1; t <= T; t++)
	{
		result = true;
		cin >> r >> c;
		for(i = 0;i < r;i++) for(j = 0;j < c;j++) cin >> data[i][j];
		for(i = 0;i < r;i++) for(j = 0;j < c;j++)
		{
			if(data[i][j] == '#')
			{
				if(!CheckValid(i,j))
				{
					result = false;
					i = r + 1;
					break;
				}
			}
		}
		cout << "Case #" << t << ":" << endl;
		if(!result) cout << "Impossible" << endl;
		else{
			for(i = 0;i < r;i++)
			{
				for(j = 0;j < c;j++) cout << data[i][j];
				cout << endl;
			}
		}
	}
};


