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

vector<bool> wasVisited;
int flood(vector<int> number, int index)
{
	wasVisited[index]=true;

	if(wasVisited[number[index]])
	{
		if(number[index]!=index)
		{
			return 1;
		}
		return 0;
	}
	return 1+flood(number,number[index]);
}

int main()
{
	ifstream cin("C:\\Users\\Bryan\\Desktop\\TestFile.in");
	ofstream cout("C:\\Users\\Bryan\\Desktop\\Output.txt");

	int T;
	cin >> T;
	for(int counter=1;counter<=T;counter++)
	{
		int N;
		cin >> N;
		vector<int> number;
		wasVisited.clear();
		for(int c=0;c<N;c++)
		{
			int i;
			cin >> i;
			number.push_back(i-1);

			wasVisited.push_back(false);
		}

		int ans=0;
		for(int c=0;c<N;c++)
		{
			if(!wasVisited[c])
			{
				ans+=flood(number, c);
			}
		}
		cout << "Case #" << counter << ": " << ans << '\n';
	}

	return 0;
}