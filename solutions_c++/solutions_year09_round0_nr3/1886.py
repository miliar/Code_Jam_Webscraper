#include <stdio.h>
#include <string>
#include <string.h>

using namespace std;

#define MAXN 1000

int N;
char buf[MAXN];
string jamString = "welcome to code jam";

int memo[MAXN][25];

int countString(int i,int j)
{
	int k;

	int& ret = memo[i][j];

	if( ret != -1 )
		return ret;

	if( j >= jamString.size() )
		return ret = 1;

	if( i >= N )
		return ret = 0;

	ret = 0;

	for( k = i; k < N; k++ )
	{
		if( buf[k] == jamString[j] )
		{
			int t = countString(k + 1,j + 1);
			ret = (ret % 10000 + t % 10000) % 10000;
		}
	}

	return ret;
}

int main()
{
	int T,i;
	char res[10];

	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	scanf("%d\n",&T);;
	int result;
	string zero;
	string resultString;
	 
	for( int kase = 1; kase <= T; kase++ )
	{
		gets(buf);
		N = strlen(buf);
		memset(memo,-1,sizeof(memo));
		result = countString(0,0);
		sprintf(res,"%d",result);
		zero = "";

		for( i = 0; i < 4 - strlen(res); i++ ) zero += "0";
		
		resultString = zero + res;
		printf("Case #%d: ",kase);
		puts(resultString.c_str());
	}

	return 0;
}

		