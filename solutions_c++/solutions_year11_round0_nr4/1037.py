#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <string>
using namespace std;


typedef long long cybers ;


#define MAX_SIZE 1000
#define INFINITY 1000000000
#define PI 3.1415926

#define PRT_F(a,b) cout<<"Case #"<<a<<": "<<b<<".000000"<<endl;


int main()
{

	freopen("D-large.in","rt",stdin); freopen("D-large.out","wt",stdout);
	int ARRAY_OF[1009];
	bool ARRAY_OF_VISITED[1009];
	int amount = 0;
	cin>>amount;
	int p = 0;
	
	while (p<amount)
		{
		memset (ARRAY_OF,0,sizeof(ARRAY_OF));
		memset (ARRAY_OF_VISITED,0,sizeof(ARRAY_OF_VISITED));
		int arraysize  = 0;
		
		cin>>arraysize;
		for (int i=1;i<(1+arraysize);i++)
			{
				cin>>ARRAY_OF[i];
				

			}
		int hits = 0;
		int visitedcounter = 1;
		do
			{
			int curhit = 0;
			for (int i = visitedcounter ;ARRAY_OF_VISITED[i]!=true ; i = ARRAY_OF[i])
				{
				ARRAY_OF_VISITED[i] = true;
				curhit++;
				}
				if (curhit!=1)
				hits+=(curhit);
			int t = 0;
			for ( t = visitedcounter;t<(arraysize+1); ++t)
				{
				if (ARRAY_OF_VISITED[t] == false)
					{
					
					break;
					}

				}
			
			visitedcounter = t;

			}	
		while (visitedcounter < (arraysize+1));

		p++;
		
		PRT_F(p,hits);
		}
}

