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

struct Combination
{
	char b1;
	char b2;
	char c;

	Combination(){}
	Combination(char B1, char B2, char C)
	{
		b1=B1;
		b2=B2;
		c=C;
	}
};

int value(char let)
{
	if(let=='Q') return 0;
	if(let=='W') return 1;
	if(let=='E') return 2;
	if(let=='R') return 3;
	if(let=='A') return 4;
	if(let=='S') return 5;
	if(let=='D') return 6;
	if(let=='F') return 7;

	assert(false);
}

bool isBase(char let)
{
	return let=='Q' || let=='Q' || let=='W' || let=='E' || let=='R' || let=='A' || let=='S' || let=='D' || let=='F';
}

int main()
{
	ifstream cin("C:\\Users\\Bryan\\Desktop\\TestFile.in");
	ofstream cout("C:\\Users\\Bryan\\Desktop\\Output.txt");

	int T;
	cin >> T;
	for(int counter=1;counter<=T;counter++)
	{
		int C;
		cin >> C;
		vector<Combination> combination;
		for(int c=0;c<C;c++)
		{
			char x,y,z;
			cin >> x >> y >> z;
			combination.push_back(Combination(x,y,z));
		}

		int D;
		cin >> D;
		vector<int> oppose[8];
		for(int c=0;c<D;c++)
		{
			char a,b;
			cin >> a >> b;
			oppose[value(a)].push_back(value(b));
			oppose[value(b)].push_back(value(a));
		}

		vector<char> element;
		int num[8];
		for(int c=0;c<8;c++)
		{
			num[c]=0;
		}

		int N;
		cin >> N;
		for(int c=0;c<N;c++)
		{
			char next;
			cin >> next;
			element.push_back(next);
			num[value(next)]++;
			if(element.size()!=1)
			{
				for(int n=0;n<C;n++)
				{
					if((element[element.size()-1]==combination[n].b1 && element[element.size()-2]==combination[n].b2) || (element[element.size()-1]==combination[n].b2 && element[element.size()-2]==combination[n].b1))
					{
						num[value(element[element.size()-1])]--;
						num[value(element[element.size()-2])]--;
						element.pop_back();
						element.pop_back();
						element.push_back(combination[n].c);
						break;
					}
				}
				if(isBase(element[element.size()-1]))
				{
					for(int n=0;n<(int)oppose[value(element[element.size()-1])].size();n++)
					{
						if(num[oppose[value(element[element.size()-1])][n]]!=0)
						{
							element.clear();
							for(int x=0;x<8;x++)
							{
								num[x]=0;
							}
							break;
						}
					}
				}
			}
		}
		cout << "Case #" << counter << ": [";
		for(int c=0;c<(int)element.size();c++)
		{
			if(c!=0)
			{
				cout << ", ";
			}
			cout << element[c];
		}
		cout << "]\n";
	}

	return 0;
}