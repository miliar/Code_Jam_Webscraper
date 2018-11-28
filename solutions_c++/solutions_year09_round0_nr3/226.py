#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> piii; 

string T = "welcome to code jam";
string P;

int R[512][19];

int main()
{
	int cases;
	scanf("%d", &cases);
	getline(cin, P);
	REP(caseIndex, cases)
	{
		//memset(S, 0, sizeof S);
		memset(R, 0, sizeof R);
		getline(cin, P);
		int M = P.size();
		int N = T.size();
		REP(i, M)
		{
			REP(j, N)
			{
				R[i][j] = (i)? R[i-1][j] : 0;
				if (j == 0)
				{
					R[i][j] += (P[i] == T[j]);
				}
				else
				{
					if (P[i] == T[j])
					{
						R[i][j] += (i && j) ? R[i-1][j-1] : 0;
					}
				}
				R[i][j] %= 10000;
			}
		}
		printf("Case #%d: ", caseIndex + 1);
		int rst = R[M - 1][N - 1];
		if (rst < 1000)
			putchar('0');
		if (rst < 100)
			putchar('0');
		if (rst < 10)
			putchar('0');
		if (rst < 1)
			putchar('0');
		if (rst)
			printf("%d\n", rst);
		else
			puts("");
	}
	return 0;
}
