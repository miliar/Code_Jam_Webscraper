#include <iostream>
#include <stdio.h>
#include <fstream>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;

string com[50], opp[50];
char org[150];
char res[150];

int c, d, n;

int Dispose();

int main()
{
	freopen("B-large.in","r", stdin);
	freopen("outbL.txt", "w", stdout);
	int cas;
	cin >> cas;
	for(int i = 1; i <= cas; i++)
	{
		cin >> c;
		for(int j = 0; j < c; j++)
			cin >> com[j];
		cin >> d;
		for(int j = 0; j < d; j++)
			cin >> opp[j];
		cin >> n;
		cin >> org;

		int len = Dispose();

		cout << "Case #" << i << ": [";
		if(len)
		{
			for(int j = 0; j < len - 1; j++)
				printf("%c, ", res[j]);
			printf("%c", res[len-1]);
		}
		cout << "]" << endl;
	}
	return 0;
}


int Dispose()
{
	strcpy(res, "");
	int k= 0, i, j;
	for(i = 0; i < n; i++)
	{
		res[k++] = org[i];
		if(k>=2)
		{
			for(j = 0; j < c; j++)
				if(res[k-1] == com[j][0] && res[k-2] == com[j][1] ||
					res[k-1] == com[j][1] && res[k-2] == com[j][0])
				{
					res[k-2] = com[j][2];
					k--;
					break;
				}

			for(j = 0; j < d; j++)
				if(res[k-1] == opp[j][0])
				{
					if(find(res,res+k,opp[j][1])!=res+k)
					{	
						strcpy(res, "");
						k = 0;
						break;
					}
				}
				else if(res[k-1] == opp[j][1])
				{
					if(find(res, res +k, opp[j][0])!=res+k)
					{	
						strcpy(res, "");
						k=0;
						break;
					}
				}
		}
	}
	return k;
}