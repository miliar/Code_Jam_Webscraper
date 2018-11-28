# include <cstdio>
# include <iostream>
# include <algorithm>
# include <vector>
# include <cstring>
# include <cctype>
# include <set>
# include <map>
# include <cmath>
# include <queue>
# include <string>

using namespace std;

int pos[10000],len[10000];
int deepest[10000];

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		int N;
		scanf("%d",&N);
		
		for(int i=0;i<N;i++)
		{
			scanf("%d%d",pos+i,len+i);
			deepest[i]=0;
		}
		
		int lim;
		scanf("%d",&lim);
		
		int maxreach=0;
		deepest[0]=pos[0];
		
		for(int i=0;i<N;i++)
		{
			maxreach=max(maxreach,pos[i]+deepest[i]);
			if(maxreach>=lim)
			{
				printf("YES\n");
				goto BPP;
			}
			
			for(int j=i+1;(j<N)&&(pos[i]+deepest[i]>=pos[j]);j++)
				deepest[j]=max(deepest[j],min(len[j],pos[j]-pos[i]));
		}
		
		printf("NO\n");
		BPP:;
	}
	return 0;
}
