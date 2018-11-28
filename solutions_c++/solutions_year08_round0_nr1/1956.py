#include <iostream>
#include <string>

using namespace std;

#define MAXS 320
#define MAXQ 3200
#define INFIN (100000000)


int s,q;
//string S[MAXQ],Q[MAXS];
int dp[MAXQ][MAXS];
char S[MAXQ][10000],Q[MAXS][10000];


int def(int a, int b)
{
	if(a==b)
		return 0;
	else
		return 1;
}


void run()
{
	for(int i=0; i<q; i++)
		for(int j=0; j<s; j++)
			for(int k=0; k<s; k++)
			{
				if(strcmp(S[k],Q[i+1]))
				{
					dp[i+1][k]=min(dp[i+1][k],dp[i][j]+def(k,j));
				}
			}
}


int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test_count;
	cin >> test_count;
	for(int test_num=1; test_num<=test_count; test_num++)
	{
		cin >> s;
		cin.getline(S[0],1000);
		for(int i=0; i<s; i++)
			cin.getline(S[i],1000);
		cin >> q;
		cin.getline(Q[0],1000);
		for(int i=1; i<=q; i++)
			cin.getline(Q[i],1000);
		memset(dp,0,sizeof(dp));
		for(int i=0; i<s; i++)
			for(int j=1; j<=q; j++)
			{
				dp[j][i]=INFIN;
			}
		run();
		int res = INFIN;
		for(int i=0; i<s; i++)
			res=min(dp[q][i],res);
		printf("Case #%d: %d\n",test_num,res);
	}
	return 0;
}