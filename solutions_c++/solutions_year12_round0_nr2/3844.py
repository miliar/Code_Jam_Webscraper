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

int ar[100];

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int N,S,P,good=0;
		scanf("%d%d%d",&N,&S,&P);
		
		for(int i=0;i<N;i++)
			scanf("%d",ar+i);
		
		for(int i=0;i<N;i++)
			if(P+2*max(0,P-1)<=ar[i])good++;
			else if((S>0)&&(P+2*max(0,P-2)<=ar[i]))good++,S--;
		printf("Case #%d: %d\n",t,good);
	}
	return 0;
}
