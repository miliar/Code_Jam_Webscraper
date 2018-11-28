//Author : Nitin Gangahar
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <iostream>
#include <cstring>
#include <set>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define isok(x,y) (x>=0 && x<R && y>=0 && y<C)
#define MAX 102
#define INF INF

using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< VI > VII;
char A[MAX][MAX];
inline double RPI(double WP,double OWP, double OOWP)
{
	return 0.25*WP + 0.50 * OWP + 0.25 * OOWP;
}
int SUM[MAX]; //WP sum matrix
int PLAYED[MAX];
double WP[MAX];
double OWP[MAX];
int OWPSUM[MAX]; 
double OOWP[MAX];
int main()
{
	int T,cases = 1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d:\n",cases++);
		int N;
		scanf("%d",&N);
		for(int i=0;i<N;i++)
				scanf("%s",A[i]);
		for(int i=0;i<N;i++)
		{
			int sum = 0;
			int played = 0;
			for(int j=0;j<N;j++)
			{
				sum += (A[i][j]=='1'?1:0);
				played += ((A[i][j]=='1' || A[i][j]=='0')?1:0);
			}
			SUM[i] = sum; //sum of the games played
			PLAYED[i] = played; //total games played
			WP[i] = (double)sum/(double)played;
		}	

		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			OWPSUM[j] = SUM[j];
			
			double TOTSUM = 0; //summations of all WP of all opponents
			for(int j=0;j<N;j++)
			{
				if(A[i][j]=='0' || A[i][j]=='1') //did they play
				{
					OWPSUM[j] -= (A[j][i]=='1'?1:0);
					TOTSUM += ((double)OWPSUM[j]/((double)PLAYED[j]-1));
				}
			}
			TOTSUM = TOTSUM/PLAYED[i];
			OWP[i] = TOTSUM;
		}
		for(int i=0;i<N;i++)
		{
			double TOOWP = 0;
			for(int j=0;j<N;j++)
			{
				if(A[i][j]=='1' || A[i][j]=='0')
					TOOWP += OWP[j];
			}
			OOWP[i] = TOOWP/PLAYED[i];
			printf("%0.12lf\n",RPI(WP[i],OWP[i],OOWP[i]));
		}			
	}
	return 0;
}
