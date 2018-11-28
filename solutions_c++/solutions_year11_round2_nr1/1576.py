#include<iostream>
#include<sstream>
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;

#define pb								push_back
#define s(n)								scanf("%d",&n)
#define sl(n) 								scanf("%lld",&n)
#define sf(n) 								scanf("%lf",&n)
#define fill(a,v) 							memset(a, v, sizeof a)
#define INF								(int)1e9
#define EPS								1e-9

typedef long long LL;
typedef pair<int, int > PII;

int testCases, testNum;
// here follow the sovle, input & main

int N;
int adjMatrix[105][105];
int total[105], wins[105];
double wp[105], owp[105], oowp[105];
char line[105];

void solve()
{
	 fill( owp, 0);
	 fill( oowp, 0);
	 printf("Case #%d:\n", testNum);
	 
	 for(int i = 0; i < N; i++)
	 {
		  double sum = 0;
		  int all = 0;
		  for(int j = 0;j < N;j++)
		  {
			   if( adjMatrix[i][j] == 1)
			   {
					sum += total[j] > 1 ? ( 1.0 * wins[j]) / (total[j] - 1) : 0.0;
					all ++;
			   }
			   else if(adjMatrix[i][j] == -1)
			   {
					sum += (total[j] > 1 ? ( 1.0 * (wins[j] - 1) / (total[j] - 1)) : 0.0);
					all ++;
			   }
		  }
		  owp[i] = sum / all;
		  for(int j = 0; j < N; j++)
			   if( adjMatrix[i][j])
					oowp[j] += owp[i];
	 }
	 for(int i =0; i < N; i++)
	 {
		  int all = 0;
		  double sum = 0;
		  for(int j = 0; j < N; j++)
			   if( adjMatrix[i][j])
			   {
					sum += owp[j];
					all ++;
			   }
		  oowp[i] = sum / all;
	 }
	 
	 for(int i = 0; i < N; i++)
	 {
		  double its = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		  printf("%lf\n", its);
	 }
	 
}

bool input()
{
	 s(N);
	 for(int i = 0; i < N; i++)
	 {
		  total[i] = wins[i] = 0;
		  scanf("%s", line);
		  
		  for(int j = 0; j < N; j++)
		  {
			   if(line[j] == '.')
					adjMatrix[i][j] = 0;
			   else
			   {
					total[i] ++;
					adjMatrix[i][j] = (line[j] == '1' ? 1 : -1);
					if(line[j] == '1')
						 wins[i] ++;
			   }
		  }
		  wp[i] = total[i] ? (1.0 * wins[i]) / total[i] : 0.0;
	 }
	return true;
}

int main()
{
	s(testCases);
	for(testNum = 1; testNum <= testCases; testNum ++)
	{
		if(!input()) break;
		solve();
	}
}
