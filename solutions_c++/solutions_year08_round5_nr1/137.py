#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
using namespace std;
int triarea(const pair<int, int>& p1, const pair<int, int>& p2)
{
	return (p1.first * p2.second - p1.second * p2.first ) / 4; //+ p2.first * 6002  + 6002 * p1.second  - p2.second * 6002 - 6002 * p1.first)/ 8;
}
int areat(const vector<pair<int, int> >& points)
{
	int res = 0;
	//pair<int, int> p(points[0]);
	for(int i = 1 ; i < points.size(); i++)
	{
		res += triarea(points[i - 1], points[i]);
	}
	res += triarea(points.back(), points[0]);
	return  res / 2;

}
int main()
{
	freopen("../../google.in", "r", stdin);
	freopen("../../google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);

		//map<pair<int, int> > m;
		//m.insert(make_pair(0, 0));
		string str;
		int temp;
		int l;
		cin >> l;
		int mat[4][2] = {{2, 0}, {0, 2}, {-2, 0}, {0, -2}};
		pair<int, int> cur(6002, 6002);
		int dir = 0;
		vector<int> horizontsMax(12005, -14000), verticalsMax(12005, -14000);
		vector<int> horizontsMin(12005, 14000), verticalsMin(12005, 14000);
		horizontsMax[6002] = 6002;
		verticalsMax[6002] = 6002;
		horizontsMin[6002] = 6002; 
		verticalsMin[6002] = 6002;
		pair<int, int> p;
		vector<pair<int, int> > v;
		v.push_back(make_pair(6002, 6002));
		for(int i = 0; i  < l; i++)
		{
			cin >> str >> temp;
			for(int j = 0; j < temp; j++)
			{
				for(int k = 0; k < str.size(); k++)
				{
					if(str[k] == 'L')
					{
						dir = (dir + 3) % 4;
						v.push_back(make_pair(cur.first, cur.second));
					}
					else
					{
						if(str[k] == 'R')
						{
							dir = (dir + 1) % 4;
							v.push_back(make_pair(cur.first, cur.second));
						}
						else
						{
							p = cur;
							cur.first += mat[dir][0];
							cur.second += mat[dir][1];
							if(dir % 2 == 1)
							{
								verticalsMax[(cur.second + p.second) / 2] = max(verticalsMax[(cur.second + p.second) / 2], cur.first);
								verticalsMin[(cur.second + p.second) / 2] = min(verticalsMin[(cur.second + p.second) / 2], cur.first);
							}
							else
							{
								horizontsMax[(cur.first + p.first) / 2] = max(horizontsMax[(cur.first + p.first) / 2], cur.second);
								horizontsMin[(cur.first + p.first) / 2] = min(horizontsMin[(cur.first + p.first) / 2], cur.second);
							}
						}
					}
				}
			}
		}
		v.push_back(make_pair(cur.first, cur.second));
		int area = -abs(areat(v));
		for(int i = 1; i < 12005; i+=2)
			for(int j = 1;  j < 12005; j+=2)
			{
				if(i > verticalsMin[j] && i < verticalsMax[j])
					area++;
				else
				{
					if(j > horizontsMin[i] && j < horizontsMax[i])
						area++;
				}
			}
		cout << area << endl;
	}
	return 0;
}
