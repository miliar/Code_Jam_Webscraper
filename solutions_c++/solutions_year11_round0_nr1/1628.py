#include <iostream>
#include <cmath>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <vector>
using namespace std;

#define MAX 101

typedef struct Command
{
	char rob;
	int pos;
};

int solve(Command cmd[], int N)
{
	int result = 0;
	
	int posOrange = 1;
	int posBlue = 1;
	
	for(int i=0;i<N;i++)
	{
		// 4 O 2 B 1 B 2 O 4
		//cout << "Blue : " << posBlue << " " << "Orange : " << posOrange << " Result : " << result << endl;
		
		if(cmd[i].rob == 'B')
		{
			result += abs(cmd[i].pos - posBlue) + 1;
			int diff = abs(cmd[i].pos - posBlue) + 1;
			posBlue = cmd[i].pos;
			
			int index = -1;
			for(int j=i+1;j<N;j++)
			{
				if(cmd[j].rob == 'O')
				{
					index = j;
					break;
				}
			}
			
			if(index != -1)
			{
				for(int j=0;j<diff;j++)
				{
					if(posOrange != cmd[index].pos)
					{
						posOrange += (cmd[index].pos > posOrange ? 1 : -1);
					}
					else
					{
						break;
					}
				}
			}
		}			
		else
		{
			result += abs(cmd[i].pos - posOrange) + 1;
			int diff = abs(cmd[i].pos - posOrange) + 1;
			posOrange = cmd[i].pos;
			
			int index = -1;
			for(int j=i+1;j<N;j++)
			{
				if(cmd[j].rob == 'B')
				{
					index = j;
					break;
				}
			}
			
			if(index != -1)
			{
				for(int j=0;j<diff;j++)
				{
					if(posBlue != cmd[index].pos)
					{
						posBlue += (cmd[index].pos > posBlue ? 1 : -1);
					}
					else
					{
						break;
					}
				}
			}
		}
	}
	
	//cout << "Blue : " << posBlue << " " << "Orange : " << posOrange << " Result : " << result << endl;
	
	return result;
	
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int Test;
	cin >> Test;
	for(int t=1;t<=Test;t++)
	{
		Command cmd[MAX];
		int N;
		cin >> N;
		for(int i=0;i<N;i++)
		{
			string str;
			int tmp;
			cin >> str >> tmp;
			cmd[i].rob = str[0];
			cmd[i].pos = tmp;
		}
		
		printf("Case #%d: %d\n", t, solve(cmd, N));
		
	}
	return 0;
}
