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
		vector<vector<int> > digit;
		vector<int> blank;
		for(int c=0;c<N;c++)
		{
			int i;
			cin >> i;
			number.push_back(i);

			digit.push_back(blank);
		}

		vector<int> temp=number;
		bool done=false;
		while(!done)
		{
			done=true;
			for(int c=0;c<N;c++)
			{
				digit[c].push_back(temp[c]%2);
				temp[c]/=2;
				if(temp[c]!=0)
				{
					done=false;
				}
			}
		}

		bool canDo=true;
		for(int c=0;c<(int)digit[0].size();c++)
		{
			int sum=0;
			for(int n=0;n<N;n++)
			{
				sum+=digit[n][c];
			}
			if(sum%2!=0)
			{
				canDo=false;
				break;
			}
		}
		if(!canDo)
		{
			cout << "Case #" << counter << ": NO\n";
			continue;
		}

		int total=0;
		int minimum=number[0];
		for(int c=0;c<N;c++)
		{
			total+=number[c];
			minimum=min(minimum,number[c]);
		}

		cout << "Case #" << counter << ": " << total-minimum << '\n';
	}

	return 0;
}