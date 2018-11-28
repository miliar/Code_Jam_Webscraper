// Google CodeJAM 2011
// Author: Syed Ghulam Akbar

#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <iostream>

using namespace std;
char Team[101][101];
double TeamInfo[101][3];

int main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int C;
	int N;
	scanf("%d",&C);

	for (int test=1;test<=C;test++) {
		cin >> N;

		// Read the teams data
		for (int i=0; i<N; i++)
			for (int j=0; j<N; j++)
				cin >> Team[i][j];

		// Calculate Wining Percentiles
		for (int i=0; i<N; i++)
		{
			double win=0, tot=0;
			for (int j=0; j<N; j++)
			{
				if (Team[i][j] == '.') continue;
				if (Team[i][j] == '1') 
					win++;
				tot++;
			}
			TeamInfo[i][0]=win/tot;
		}

		// Calculate OWP 
		for (int i=0; i<N; i++)
		{
			double ow=0, tt=0;
			for (int j=0; j<N; j++)
			{
				if (Team[i][j] == '.') continue;
				
				// Calculate other matches WP
				double win=0, tot=0;
				for (int k=0; k<N; k++)
				{
					if (k==i) continue;
					if (Team[j][k] == '.') continue;
					if (Team[j][k] == '1') 
						win++;
					tot++;
				}
				ow += (win/tot);
				tt++;
			}
			TeamInfo[i][1]= ow / tt;
		}

		// Calculate OOWP 
		for (int i=0; i<N; i++)
		{
			double oow=0, tot=0;
			for (int j=0; j<N; j++)
			{
				if (Team[i][j] == '.') continue;
				oow += TeamInfo[j][1];
				tot++;
			}
			TeamInfo[i][2]= oow / tot;
		}

		printf("Case #%d: \n", test);
		for (int i=0; i<N; i++)
		{
			float rpi = 0.25 * TeamInfo[i][0] + 0.50 * TeamInfo[i][1] + 0.25 * TeamInfo[i][2];
			printf("%f\n", rpi);
		}
	}
}