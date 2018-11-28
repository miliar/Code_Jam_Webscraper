#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

map< string ,int > Code;
int Dp[1005][105] , cnt ;
int code(string & a)
{
	if(Code.find(a) == Code.end())
	{
		Code[a] = cnt ++;
		return cnt - 1;
	}
	return Code[a];
}
int main(void)
{
	freopen("A-large(1).in","r",stdin);
	freopen("out","w",stdout);
	int cases ;
	scanf("%d",&cases);

	int f = 0 ; 
	while( cases -- )
	{
		Code.clear();
		cnt = 0 ; 
		int s ,i,j,k;
		scanf("%d",&s);
		string engine;
		cin.ignore();
		for(i = 0 ; i < s ; i ++)
		{
			getline(cin,engine,'\n');
			code(engine) ;
		}
		int q;
		scanf("%d",&q);
		cin.ignore();
		getline(cin,engine,'\n');
		int Id = code(engine);
		memset(Dp,-1,sizeof(Dp));
		for(j = 0 ; j < s ; j ++)
		{
			if(Id != j)
				Dp[0][j] = 0;
		}

		for(i = 1 ; i < q ; i ++)
		{
			getline(cin,engine,'\n');
			Id = code(engine);
			for(j = 0 ; j < s ; j ++)
			{
				if(Dp[i-1][j] == -1) continue;
				for(k = 0 ; k < s ; k ++)
				{
					if(k == Id) continue;
					if(j != k)
					{
						if(Dp[i][k] == -1 || Dp[i][k] > Dp[i-1][j] + 1)
						{
							Dp[i][k] = Dp[i-1][j] + 1;
						}
					}
					else
					{
						if(Dp[i][k] == -1 ||Dp[i][k] > Dp[i-1][j])
						{
							Dp[i][k] = Dp[i-1][j];
						}
					}
				}
			}
		}
		int Min = INT_MAX;
		for(i = 0 ; i < s ; i ++)
		{
			if(Dp[q-1][i] != -1 && Dp[q-1][i] < Min)
				Min = Dp[q-1][i];
		}
		printf("Case #%d: %d\n",++f,Min);
	}
	return 0;
}