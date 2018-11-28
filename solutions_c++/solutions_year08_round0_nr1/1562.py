#include <cstdio>
#include <string>
#include <vector>
#include <map>
//#include <hash_map.h>
#include <cstdlib>

using namespace std;
using namespace __gnu_cxx;

map<string,int> s2i;
int q,s;

vector<string> a;

int dp[1024][128];

int calc_dp(int i,int j)
{
	if( i == q )
		return 0;
	if( dp[i][j] != -1 )
		return dp[i][j];

	map<string,int>::iterator it = s2i.find(a[i]);
	if( it == s2i.end() || it->second != j )
		dp[i][j] = calc_dp(i+1,j);
	else
	{
//		printf("match %d %d\n",i,j);
		int best=0x7fffffff;
		for(int k=0;k<s;k++)
			if(k != j)
			{
				int c = calc_dp(i+1,k);
				if( c < best )
					best = c;
			}
		dp[i][j] = best + 1;
	}

	return dp[i][j];
}

int main()
{
	int n;

//	freopen("test.in","r",stdin);
	scanf("%d",&n);

	for(int z=1;z<=n;z++)
	{

		a.clear();
		s2i.clear();
		memset(dp,-1,sizeof(dp));

		char buffer[128];

		scanf("%d\n",&s);
		for(int i=0;i<s;i++)
		{
			fgets(buffer,sizeof(buffer),stdin);
			s2i[string(buffer)] = i;
		}

		scanf("%d\n",&q);
		for(int i=0;i<q;i++)
		{
			fgets(buffer,sizeof(buffer),stdin);
			a.push_back(string(buffer));
		}

		int r=0x7fffffff;
		for(int i=0;i<s;i++)
		{
			int c = calc_dp(0,i);
			if( c<r )
				r = c;
		}

/*		for(int i=0;i<q;i++)
		{
			for(int j=0;j<s;j++)
				printf("%4d ", calc_dp(i,j) );
			printf("\n");
		}
*/
		printf("Case #%d: %d\n", z, r);
	}



}


