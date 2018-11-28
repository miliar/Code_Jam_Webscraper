#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int idx, rst;
	int tidx[1001] = {0};
	int trst[1001] = {0};

	int t, rep, hold, gnum, tsum;
	int grp[1001];

//	FILE *fin = freopen("a.in", "r", stdin);
//	FILE *fout = fopen("a.out", "w");

	cin >> t;

	for(int i =1; i <= t; ++i )
	{
		cin >> rep >> hold >> gnum;
		int total = 0;
		for( int a=0;a< gnum; ++a )
		{
			cin >> grp[a];
			total += grp[a];
		}

		grp[gnum] = grp[0];
		tsum = rst = idx = 0;


		for( int j=0; j < rep; ++j)
		{		
			if( total < hold )
			{
				rst = total * rep;
				break;
			}
			idx = idx%gnum;
			
			tsum += grp[idx];
			
			while( 1 )
			{
				idx = idx%gnum;
				
				if( tsum + grp[idx+1] > hold )
				{
					rst += tsum;	tsum = 0;	++idx;
					break;
				}else
					tsum += grp[idx+1];
				++idx;
			}
		}
//		fprintf(fout, "Case #%d: %d\n", i, rst);
		printf("Case #%d: %d\n", i, rst);
	}
//	fclose(fout);
	return 0;
}