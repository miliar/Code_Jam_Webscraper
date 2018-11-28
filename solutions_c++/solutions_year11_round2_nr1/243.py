#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define S(X) ((X)*(X))
#define ABS(X) ((X)>0?(X):(-(X)))

typedef pair<int,int> PII;
typedef __int64 LL;

double owp[200], oowp[200], win[200], played[200], wp[200];
char word[200][200];

int main()
{
	double wins, play;

//	freopen("A-small-attempt0.in","r",stdin); freopen("A-small-output0.out","w",stdout);
//	freopen("A-small-input1.in","r",stdin); freopen("A-small-output1.out","w",stdout);
//	freopen("A-small-input2.in","r",stdin); freopen("A-small-output2.out","w",stdout);
	freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);

	int T, ks;
	int N, i,j,pl;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d:\n",ks);

		scanf("%d",&N);
		for(i=0;i<N;i++)
		{
			scanf("%s",word[i]);
		}

		for(i=0;i<N;i++)
		{
			played[i]=0;
			win[i]=0;
			for(j=0;j<N;j++)
				if(word[i][j]=='0') played[i]++;
				else if(word[i][j]=='1') played[i]++, win[i]++;

			wp[i]=  1.*win[i]/played[i];
		}

		for(i=0;i<N;i++)
		{
			pl = 0;
			owp[i]=0;
			for(j=0;j<N;j++)
				if( word[i][j]!='.' )
				{
					play = played[j]-1;
					wins = win[j] - (word[j][i]=='1');

					owp[i]+=1.*wins/play;
					pl++;
				}

			owp[i]/=pl;
		}

		for(i=0;i<N;i++)
		{
			oowp[i]=0;
			for(j=0;j<N;j++)
				if(word[i][j]!='.')
					oowp[i]+=owp[j];

			oowp[i]/=played[i];
//			printf("%.14lf\n",oowp[i]);
		}

		double rpi;
		for(i=0;i<N;i++)
		{
			rpi = .25*wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%.14lf\n",rpi);
		}

	}

	return 0;
}