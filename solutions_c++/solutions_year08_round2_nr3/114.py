#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");


int cards[5000];

int main(void)
{
	int ttt;
	cin >> ttt;
	int ct = 0;
	while(ttt>0)
	{
		ct++;
		ttt--;
		int i,j,k,a,b,n,m,curr,todo;
		cin >> n;
		memset(cards,0,sizeof(cards));
		curr=0;
		for(i=1; i<=n; i++)
		{
			todo=i;
			while(todo>0)
			{
				if(cards[curr]==0)
				{
					todo--;
					if(todo==0)
					{
						cards[curr]=i;
						break;
					}
					curr++;
					curr%=n;
				}
				else
				{
					curr++;
					curr%=n;
				}
			}
		}
		cin >> m;
		cout << "Case #" << ct << ":";
		fout << "Case #" << ct << ":";
		for(i=0; i<m; i++)
		{
			cin >> j;
			cout << " " << cards[j-1];
			fout << " " << cards[j-1];
		}
		cout << endl;
		fout << endl;
		
	}

	
	return 0;
}

