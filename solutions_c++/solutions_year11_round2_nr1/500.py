#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

char matches[105][105];
double wp[105];
double owp[105];
double oowp[105];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	//freopen("XXX-large.out", "w", stdout);
	int test, cas = 1;
	cin>>test;
	while(test--)
	{
		int N;
		int i, j, k;

		cin>>N;

		for(i=0; i<N; i++) wp[i] = owp[i] = oowp[i] = 0;
		
		for(i=0; i<N; i++) scanf("%s", matches[i]);

		for(i=0; i<N; i++)
		{
			int tot = 0;
			int win = 0;
			for(j=0; j<N; j++) if(matches[i][j]!='.')
			{
				tot ++;
				if(matches[i][j] == '1') win++;
			}
			wp[i] = win*1.0/(1.0*tot);
		}

		for(i=0; i<N; i++)
		{
			int t = 0;
			double sum = 0;
			for(j=0; j<N; j++) if(matches[i][j]!='.')
			{
				int tot = 0;
				int win = 0;
				for(k=0; k<N; k++) if(k!=i && matches[j][k]!='.')
				{
					tot ++;
					if(matches[j][k]=='1') win++;
				}
				t++;
				sum += win*1.0/(1.0*tot);
			}
			owp[i] = sum/(1.0*t);
		}

		for(i=0; i<N; i++)
		{
			int t = 0;
			double sum = 0;
			for(j=0; j<N; j++) if(matches[i][j]!='.')
			{
				t++;
				sum += owp[j];
			}
			oowp[i] = sum/(1.0*t);
		}
		cout << "Case #" << cas++ << ":\n";
		for(i=0; i<N; i++)
		{
			double rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			printf("%.12lf\n", rpi);
		}
	}
	return 0;
}