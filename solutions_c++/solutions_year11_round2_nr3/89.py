#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

int n, m;
bool edge[8][8];
int data[2][5];

int ans, stat[8], ansStat[8];
bool isUsed[8];
int bitCnt[1<<8];

void backtr(int nth, int MAX);

int main(void)
{
	for(int i=0;i<(1<<8);i++)
	{
		for(int j=0;j<8;j++) if(i & (1<<j)) bitCnt[i]++;
	}

	int T;
	cin>>T;

	for(int caseN=1;caseN<=T;caseN++)
	{
		cin>>n>>m;

		memset(edge, 0, sizeof(edge));
		for(int i=0;i<n;i++)
		{
			edge[i][(i+1)%n]=edge[(i+1)%n][i]=true;
		}
		
		for(int i=0;i<m;i++) cin>>data[0][i];
		for(int i=0;i<m;i++) cin>>data[1][i];

		for(int i=0;i<m;i++)
		{
			data[0][i]--, data[1][i]--;
			edge[data[0][i]][data[1][i]]=edge[data[1][i]][data[0][i]]=true;
		}

		ans=-1;
//		printf("n, m: %d %d\n", n, m);
		
		for(int i=n;i>=1 && ans==-1;i--) backtr(0, i);

		printf("Case #%d: %d\n", caseN, ans);
//		printf("n, m: %d %d\n", n, m);
		for(int i=0;i<n;i++) 
		{
			if(i) printf(" ");
			printf("%d", ansStat[i]+1);
		}
		printf("\n");
	}

	return 0;
}

int check(int MAX)
{
//	printf("anmg\n");
	int ret=0;

	for(int i=0;i<n;i++)
	{
		int minV=i;

		for(int j=i+1;j<n;j++)
		{
			int next=j;

			if(edge[i][next])
			{
				int curColor = (1<<stat[i]) | (1<<stat[next]);

				int cur=next;

//				printf("i: %d\n", i);
				bool isFirst=true;

				while(cur!=i)
				{
					int bef=cur;

//					printf("cur: %d\n", cur);

					minV=min(minV, cur);
					if(minV<i) break;

					for(int k=0;k<n;k++)
					{
						int next=(i-k+n)%n;
						if(next<cur && (isFirst || next!=i)) continue;
						if(edge[cur][next])
						{
							cur=next;
							curColor |= (1<<stat[cur]);
							break;
						}
					}

					if(bef==cur) 
					{
						cur=bef;
						break;
					}
			
					isFirst=false;
				}

				if(cur==i)
				{
					if(ret==0) 
					{
						ret=bitCnt[curColor];
						if(ret!=MAX) return -1;
					}
					else
					{
						if(ret!=bitCnt[curColor]) return -1;
					}
				}
			}
		}
	}

	return ret;
}

void backtr(int nth, int MAX)
{
	if(nth==n)
	{
		int maxVal=check(MAX);
//		printf("afterCheck: ");
//		for(int i=0;i<n;i++) printf("%d ", stat[i]);
//		printf("\n");
		if(maxVal>ans)
		{
			ans=maxVal;
			for(int i=0;i<n;i++) ansStat[i]=stat[i];
		}

		return;
	}

	for(int i=0;i<MAX;i++)
	{
		stat[nth]=i;
		backtr(nth+1, MAX);
		if(ans!=-1) return;
	}

	return;
}
