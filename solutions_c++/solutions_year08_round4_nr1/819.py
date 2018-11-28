#include <iostream>

using namespace std;

int main()
{
        int t, test, DP[2][10001], m, V, i, g, c, v[10001], j;
	bool change[10001], gate[10001];
        scanf("%d", &t);
        for(test=1; test<=t; test++)
        {
		scanf("%d%d", &m, &V);
		for(i=0; i<(m-1)/2; i++)
		{
			scanf("%d%d", &g, &c);
			gate[i+1]=(g==1);
			change[i+1]=(c==1);
		}

		for(i=0; i<(m+1)/2; i++)
			scanf("%d", &v[(m-1)/2+i+1]);

		for(i=(m-1)/2; i>0; i--)
			if(gate[i])
				v[i]=(v[2*i]*v[2*i+1]);
			else
				if(v[2*i] || v[2*i+1])
					v[i]=1;
				else
					v[i]=0;
		if(v[1]==V)
		{
			printf("Case #%d: 0\n", test);
			continue;
		}

		for(i=1; i<=m; i++)
			for(j=0; j<2; j++)
				DP[j][i]=(1<<28);

		for(i=m; i>(m-1)/2; i--)
			DP[v[i]][i]=0;
		for(i=(m-1)/2; i>0; i--)
			for(j=0; j<2; j++)
			{
				if(v[i]==j)
				{
					DP[j][i]=0;
					continue;
				}
				if(gate[i])
				{
					if(j==0)
						DP[j][i]=min(DP[0][2*i], DP[0][2*i+1]);
					else if(j==1)
						DP[j][i]=DP[1][2*i]+DP[1][2*i+1];
				}
				else
				{
					if(j==0)
						DP[j][i]=DP[0][2*i]+DP[0][2*i+1];
					else
						DP[j][i]=min(DP[1][2*i], DP[1][2*i+1]);
				}
				if(change[i])
				{
					if(gate[i])
					{
						if(j==0)
                                        	        DP[j][i]=min(DP[j][i], DP[0][2*i]+DP[0][2*i+1]+1);
                                 	       else
                                               		 DP[j][i]=min(min(DP[1][2*i], DP[1][2*i+1])+1, DP[j][i]);
					}
					else
					{
						if(j==0)
                               		                 DP[j][i]=min(DP[j][i], min(DP[0][2*i], DP[0][2*i+1])+1);
                               		         else if(j==1)
                                	                DP[j][i]=min(DP[1][2*i]+DP[1][2*i+1]+1, DP[j][i]);
					}
				}
			}
		if(DP[V][1]>=(1<<28))
			printf("Case #%d: IMPOSSIBLE\n", test);
		else
			printf("Case #%d: %d\n", test, DP[V][1]);
        }
        return 0;
}
