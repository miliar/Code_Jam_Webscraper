//CODEJAM - D

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;

int main()
{
	//vars
	ifstream f ("D.in");
	ofstream g ("D.out");
	int t,tt;
	int sy,sx,a,b,c;
	bool rock[105][105];
	long cnt[105][105];
	//testcase loop
	f >> tt;
		for (t=1; t<=tt; t++)
		{
			memset(rock,false,sizeof(rock));
			//input
			f >> sy >> sx >> a;
			sy--;
			sx--;
				while (a--)
				{
					f >> b >> c;
					rock[b-1][c-1]=true;
				}
			//count
			memset(cnt,0,sizeof(cnt));
			cnt[0][0]=1;
				for (a=0; a<sy; a++)
					for (b=0; b<sx; b++)
						if (cnt[a][b]!=0)
						{
							if (!rock[a+1][b+2])
								cnt[a+1][b+2]=(cnt[a+1][b+2]+cnt[a][b])%10007;
							if (!rock[a+2][b+1])
								cnt[a+2][b+1]=(cnt[a+2][b+1]+cnt[a][b])%10007;
						}
			//output
			cout << "Case #" << t << ": ";
			cout << cnt[sy][sx] << endl;
			g << "Case #" << t << ": ";
			g << cnt[sy][sx] << endl;
		}
	return(0);
}