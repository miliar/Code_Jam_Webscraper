#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <string>
using namespace std;
int t;
int dp[110][1010];
int samesq[110][1010];
char str[110];
string server[110];
string query[1100];
int main()
{
	int ka=1;
	int i,j,cnt=0;
	gets(str);
	t = atoi(str);
	while(t--){
		int n;
		gets(str);
		n = atoi(str);
		for(i=0;i<n;i++){
			gets(str);
			server[i] = string(str);
		}
		int nn;
		gets(str);
		nn = atoi(str);

		for(i=0;i<nn;i++){
			gets(str);
			query[i] = string(str);
		}
		memset(samesq,0,sizeof samesq);
		for(i=0;i<n;i++)
			for(j=0;j<nn;j++){
				if(server[i] ==query[j])
					samesq[i][j] = 1;
			}


		memset(dp,1,sizeof dp);
		int k=0;

		for(i=0;i<n;i++)
			dp[i][0] = samesq[i][0];

		for(j=1;j<nn;j++)
			for(i=0;i<n;i++){
				if(samesq[i][j]==0)
					dp[i][j] = dp[i][j-1];
				else {
					for(k=0;k<n;k++)
						if(i!=k)
							dp[i][j] <?= dp[k][j-1] +1;
				}
			}

		cnt = nn;
		if(nn-1>=0)
			for(i=0;i<n;i++)
				cnt <?= dp[i][nn-1];
		else cnt = 0;

		cout <<"Case #"<<ka++<<": "<< cnt<<endl;

	}
	return 0;
}
