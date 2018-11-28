#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <istream>
#include <string.h>
#include <vector>
#include <sstream>

using namespace std;

#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))  
#define sz(a) int((a).size())

typedef vector<int> vi;
typedef vector<string> vs;

void main()
{
	int casenum;
	cin >> casenum;
	int i, j, k;

	for(i=0; i<casenum; i++)
	{
		int result = 0;
		int s, q;
		int search[101] = {0};
		char str[100][100];
		cin >> s;
		cin.ignore(1000, '\n');

		for(j=0; j<s; j++)
			cin.getline(str[j], sizeof(str[j]),'\n');

		cin >> q;
		cin.ignore(1000,'\n');
		char str2[100] = {0};

		for(k=0; k<q; k++)
		{
			cin.getline(str2, 100);
			
			for(j=0; j<s; j++)
			{
				if(strcmp(str[j], str2) == 0)
				{
					search[j]++;
					break;
				}
			}

			int num=0;
			int id;
			for(j=0; j<s; j++)
			{
				if(search[j] == 0)
				{
					num++;
					id = j;
				}
			}
			if(num == 0)
			{
				result++;
				for(j=0 ; j<s; j++)
					if(strcmp(str[j], str2) == 0) search [j] = 1;
					else search[j] = 0;

			}
		}

		cout << "Case #" << i+1 << ": " << result << "\n";
	}
}

