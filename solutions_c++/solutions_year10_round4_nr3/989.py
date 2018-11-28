#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <cstdio>
#include <sstream>
#include <cmath>
using namespace std;

int d[101][101];
int d2[101][101];

int main()
{
	int N ; 
	cin>>N;

	for(int t = 1 ; t <= N ; t++)
	{
		memset (d,0,sizeof(d)) ; 
		memset(d2,0,sizeof(d2)) ; 

		int r ; cin>> r ; 

		for(int i = 0 ; i < r ; i++)
		{
			int x1,x2,y1,y2;
			cin>>x1>>y1>>x2>>y2 ;

			for(int k = x1; k<=x2 ; k++)
				for(int a = y1;a<=y2 ; a++)
					d[k][a] = 1 ; 
		}

		int index = 0 ; 
		bool bAlldie = true; 
		while(1)
		{
			bAlldie = true; 
			for(int i = 1 ; i < 101 ; i++)
			{
				for(int j = 1 ; j < 101 ; j++)
				{
					if(d[i][j]) 
						bAlldie = false; 
					if(d[i-1][j] == 1 && d[i][j-1] == 1)
						d2[i][j] = 1 ;
					else if(d[i][j] == 1 && d[i-1][j]==0 && d[i][j-1] == 0)
						d2[i][j] = 0 ; 
					else
						d2[i][j] = d[i][j];
				}
			}
			memcpy(d, d2, sizeof(d2)) ; 
			memset(d2,0,sizeof(d2)) ; 

			if(bAlldie) break ;		
			index++ ; 
		}
		cout<<"Case #"<<t<<": "<<index<<endl;
	}
	return 0 ; 
}