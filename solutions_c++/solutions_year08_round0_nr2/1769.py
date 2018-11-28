#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef struct _data
{
	int start, end;
} Dat;

int delay, N[2];
vector <vector <Dat> > data;
int readyTrain[2][1500];

bool sortf(Dat a, Dat b)
{
	return a.start<b.start;
}

int main(void)
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	data.resize(2);
	int T;
	scanf("%d", &T);

	for(int q=1;q<=T;q++)
	{
		scanf("%d", &delay);
		scanf("%d %d\n", N, N+1);		
		data[0].clear(), data[1].clear();
		memset(readyTrain, 0, sizeof(readyTrain));
		
		for(int i=0;i<2;i++) 
		{
			for(int j=0;j<N[i];j++)
			{
				int temp[4];
				scanf("%d:%d %d:%d\n", temp, temp+1, temp+2, temp+3);
				Dat tempDat;
				tempDat.start=temp[0]*60+temp[1];
				tempDat.end=temp[2]*60+temp[3]+delay;
				data[i].push_back(tempDat);
			}
			sort(data[i].begin(), data[i].end(), sortf);
		}		

		int ans[2]={0, }, ind[2]={0, }, cur[2]={0, };
		for(int i=0;i<1440;i++)
		{
			for(int j=0;j<2;j++)
			{
				cur[j]+=readyTrain[j][i];
				int req=0;
				while(ind[j]<data[j].size() && i==data[j][ind[j]].start) { req++; readyTrain[1-j][data[j][ind[j]].end]++; ind[j]++; }
				if(cur[j]>=req) cur[j]-=req;
				else { cur[j]=0; ans[j]+=req-cur[j]; }
			}
		}
		
		printf("Case #%d: %d %d\n", q, ans[0], ans[1]);
	}

	return 0;
}