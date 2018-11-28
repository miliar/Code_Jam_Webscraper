#include <iostream>
#include<iomanip>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <deque>
//#define SET(p) memset(p,-1,sizeof(p))
//#define CLR(p) memset(p,0,sizeof(p))
#define LL long long int
#define ULL unsigned long long int
#define S(n) scanf("%d",&n)
#define Sl(n) scanf("%lld",&n)
#define Sf(n) scanf("%lf",&n)
#define Ss(n) scanf("%s",n)
using namespace std;
int kmod=1000000007;
void fun(int k)
{
	string dataset[4];
	for(int i=0;i<4;i++)
	{
		cin>>dataset[i];
		//cout<<dataset[i];
	}
	/*int score[6][6];
	for(int i=0;i<6;i++)
	{
		for(int j=0;j<6;j++)
		{
			score[i][j]=0;
		}
	}*/

	int rows=0;
	for(int i=1;i<5;i++)
	{
		for(int j=1;j<5;j++)
		{

			if(dataset[i-1][j-1]=='X' || dataset[i-1][j-1]=='T')
				rows++;

		}
		if(rows==4)
		{
			printf("Case #%d: X won\n",k);
			return;
		}
		rows=0;

	}

	int cols=0;

	for(int j=1;j<5;j++)
	{
		for(int i=1;i<5;i++)
		{

			if(dataset[i-1][j-1]=='X' || dataset[i-1][j-1]=='T')
				cols++;

		}
		if(cols==4)
		{
			printf("Case #%d: X won\n",k);
			return;
		}
		cols=0;

	}

	int diag=0;
	for(int i=0;i<4;i++)
	{
		if(dataset[i][i]=='X' || dataset[i][i]=='T')
			diag++;
		else
			break;
	}
	if(diag==4)
	{
		printf("Case #%d: X won\n",k);
		return;
	}

	diag=0;
	for(int i=0;i<4;i++)
	{
		if(dataset[3-i][i]=='X' || dataset[3-i][i]=='T')
			diag++;
		else
			break;
	}
	if(diag==4)
	{
		printf("Case #%d: X won\n",k);
		return;
	}

	rows=0;
	for(int i=1;i<5;i++)
	{
		for(int j=1;j<5;j++)
		{

			if(dataset[i-1][j-1]=='O' || dataset[i-1][j-1]=='T')
				rows++;

		}
		if(rows==4)
		{
			printf("Case #%d: O won\n",k);
			return;
		}
		rows=0;

	}

	cols=0;

	for(int j=1;j<5;j++)
	{
		for(int i=1;i<5;i++)
		{

			if(dataset[i-1][j-1]=='O' || dataset[i-1][j-1]=='T')
				cols++;

		}
		if(cols==4)
		{
			printf("Case #%d: O won\n",k);
			return;
		}
		cols=0;

	}


	diag=0;
	for(int i=0;i<4;i++)
	{
		if(dataset[i][i]=='O' || dataset[i][i]=='T')
			diag++;
		else
			break;
	}
	if(diag==4)
	{
		printf("Case #%d: O won\n",k);
		return;
	}

	diag=0;
	for(int i=0;i<4;i++)
	{
		if(dataset[3-i][i]=='O' || dataset[3-i][i]=='T')
			diag++;
		else
			break;
	}
	if(diag==4)
	{
		printf("Case #%d: O won\n",k);
		return;
	}

	for(int i=1;i<5;i++)
	{
		for(int j=1;j<5;j++)
		{
			if(dataset[i-1][j-1]=='.')
			{
				printf("Case #%d: Game has not completed\n",k);
				return;
			}

		}
	}


	printf("Case #%d: Draw\n",k);

}

int main()
{
	int t;
	S(t);
	string s;
	for(int k=1;k<=t;k++)
	{
		fun(k);
		//cin>>s;
	}
	return 0;
}

