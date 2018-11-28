#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <cmath>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cstdio>
#include <cctype>
#include <string>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <sstream>
#include <iostream>
#include <algorithm>	

using namespace std;

int main()
{
	int nCase;
	int N, T;
	int i, j, k;
	char str[55][55];
	int cnt[55][55][4];

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d", &nCase);

	for(int cc=1; cc<=nCase; cc++)
	{
		scanf("%d%d", &N, &T);
		for(i=0; i<N; i++)
		{
			scanf("%s", str[i]);
			for(j=N-1, k=N-1; j>=0 && k>=0; j--)
			{
				if(str[i][j]!='.')
				{
					char tmp = str[i][j];
					str[i][j] = '.';
					str[i][k] = tmp;
					k--;
				}
			}
			//cout<<str[i]<<endl;
		}

		memset(cnt, 0,sizeof(cnt));
		for(i=0; i<N; i++)
		{
			if(str[i][0]!='.') cnt[i][0][1] = cnt[i][0][2] = 1;
			if(str[0][i]!='.') cnt[0][i][0] = cnt[0][i][3] = 1;
		}


		for(i=0; i<N; i++)
		{
			for(j=0; j<N; j++)
			{
				if(i>0 && str[i][j]!='.'){
					if( str[i][j] == str[i-1][j] )
						cnt[i][j][0] = cnt[i-1][j][0]+1;
					else 
						cnt[i][j][0] = 1;
				}
				if(j>0 && str[i][j]!='.'){
					if(str[i][j] == str[i][j-1])
						cnt[i][j][1] = cnt[i][j-1][1]+1;
					else
						cnt[i][j][1] = 1 ;
				}
				if(i>0 && j>0 && str[i][j]!='.'){
					if(str[i][j] == str[i-1][j-1])
						cnt[i][j][2] = max(cnt[i][j][2], cnt[i-1][j-1][2]+1);
					else
						cnt[i][j][2] = max(cnt[i][j][2], 1) ;
				}
				if(i>0 && j<N && str[i][j]!='.'){
					if(str[i][j] == str[i-1][j+1])
						cnt[i][j][3] = max(cnt[i][j][3], cnt[i-1][j+1][3]+1);
					else
						cnt[i][j][3] = max(cnt[i][j][3], 1) ;
				}
			}
		}

		bool rsucc, bsucc;
		rsucc = bsucc = false;
		for(i=0; i<N; i++)
		{
			for(j=0; j<N; j++)
			{
				//printf("%d%d%d ", cnt[i][j][0], cnt[i][j][1], cnt[i][j][2]);
				for(k=0; k<4; k++)
				{
					if(cnt[i][j][k]>=T) break;
				}
				if(k<4) 
					if(str[i][j]=='B') bsucc=true;
					else rsucc = true;
			}
			//printf("\n");
		}
		printf("Case #%d: ", cc);
		if(!bsucc && !rsucc )
			printf("Neither\n");
		else if( bsucc && rsucc )
			printf("Both\n");
		else if(!bsucc && rsucc )
			printf("Red\n");
		else if( bsucc && !rsucc )
			printf("Blue\n");

	}
	return 0;

}