
#include <vector>
#include <stdlib.h>
#include <list>
#include <algorithm>
#include <stack>
#include <string>
#include <iostream>
#include <stdio.h>
#include <math.h>


using namespace std;

int mAbs(int x)
{
	if ( x < 0 ) return -x;
	return x;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int t;
	cin>>t;
	for (int tt = 1; tt <= t ;tt++)
	{
		int n;
		cin>>n;
		char c;
		int num;
		int zapas_b = 0, zapas_o = 0, ox = 1, bx = 1;
		int time = 0;

		for (int x = 0 ; x < n ; x++) 
		{
			cin>>c>>num;
			if ( c == 'O' )
			{
				if ( zapas_o == 0)	
				{
					time += mAbs(num - ox) + 1;
					zapas_b += mAbs(num - ox) + 1;
					ox = num;
				} else
				{
					if ( zapas_o <= mAbs(num - ox))
					{
						time += mAbs(num - ox) - zapas_o + 1;
						zapas_b += mAbs(num - ox) - zapas_o + 1;
						zapas_o = 0;
						ox = num;
					} else
					{
						time += 1;
						zapas_b += 1;
						zapas_o = 0;
						ox = num;
					}
				}
			}
			if ( c == 'B' )
			{
				if ( zapas_b == 0)	
				{
					time += mAbs(num - bx) + 1;
					zapas_o += mAbs(num - bx) + 1;
					bx = num;
				} else
				{
					if ( zapas_b <= mAbs(num - bx))
					{
						time += mAbs(num - bx) - zapas_b + 1;
						zapas_o += mAbs(num - bx) - zapas_b + 1;
						zapas_b = 0;
						bx = num;
					} else
					{
						time += 1;
						zapas_b = 0;
						zapas_o += 1;
						bx = num;
					}
				}
			}
		}
		

		printf("Case #%d: %d\n",tt,time);
	}

}

