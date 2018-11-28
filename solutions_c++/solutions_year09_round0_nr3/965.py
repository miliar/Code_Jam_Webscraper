#include<iostream>
#include<string>
#include<fstream>
using namespace std;

const int MAXN = 19;
const int MAXL = 500+1;
string match = "welcome to code jam";
//string match = "aaa";
int dp[MAXL][MAXN];


int main()
{
	ifstream fin("input");
	//ofstream fout("output");
	//FILE *fp = freopen( "input",stdin );	
	freopen( "output","w", stdout );	
	int n;
	fin >> n;	
	for(int i = 0 ; i <  n ; i++)
	{
		string sztext;
		getline(fin,sztext);
		if( sztext[0] < 'a' || sztext[0] > 'z' )
		{
			i--;
			continue;
		}
		//cout << sztext << endl;
		memset( dp,0,sizeof(dp) );
		int nlen = sztext.length();
		for( int j = nlen - 1 ; j >= 0 ; j-- )
		{
			for( int k = 0 ; k < MAXN ; k++ )
			{
				if( sztext[j] == match[k] )
				{
					if( k == MAXN-1 )
					{
						dp[j][k] = 1;
						continue;
					}
					for( int m = j + 1 ; m < nlen ; m++ )
					{
						if( sztext[m] == match[k+1] )
							dp[j][k] += dp[m][k+1];
						dp[j][k] %= 10000;
					}				
				}				
			}
		}
		int res = 0;
		for(int  j = 0 ; j <  nlen ; j++ )
		{
			res += dp[j][0];
			res %= 10000;
		}
		printf( "Case #%d: %04d\n", i+1,res );

	}
	
	return 0;
}