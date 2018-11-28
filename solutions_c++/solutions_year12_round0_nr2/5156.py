#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int T,ans,tempans;
int N,S,P,score[110];

int main()
{
	scanf("%d\n",&T);
	for (int temp(1);temp<=T;++temp)
	{
		ans=0;
		memset(score,0,sizeof(score));
		scanf("%d %d %d",&N,&S,&P);
		for (int i(1);i<=N;++i)
			scanf("%d",&score[i]);
		sort(score+1,score+N+1);
		for (int i(N);i;--i)
		{
			if (score[i]==0 && P!=0) continue;
			tempans=ans;
			if (score[i]%3==0)
			{
				if ((score[i]/3)>=P) ++ans;
			}
			else if (((score[i]/3+1)>=P)) ++ans;
			if (tempans==ans)
			{
				tempans=i;
				break;
			}
			if (i==1) tempans=0;
		}
		for (int i(tempans);i>tempans-S && i>0;--i)
		{
			if (score[i]==0 && P!=0) continue;
			switch (score[i]%3)
			{
				case 0:
				case 1:
					if (((score[i]/3+1)>=P)) ++ans;
					break;
				case 2:
					if (((score[i]/3+2)>=P)) ++ans;
					break;
			}
		}
		cout << "Case #" << temp << ": " << ans << endl;
	}
	return 0;
}
