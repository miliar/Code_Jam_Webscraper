#include <cstdio>
#include <cstring>

int dynamic[100][100][100];
int n;
int data[100][2];

int getDynamic(int nth, int blue, int orange);

int main(void)
{
	int T;
	scanf("%d", &T);
	for(int caseN=1;caseN<=T;caseN++)
	{
		scanf("%d", &n);
		for(int i=0;i<n;i++)
		{
			char temp[2];
			int ind;
			scanf("%s %d", temp, &ind);
			ind--;

			if(temp[0]=='B') data[i][0]=0;
			else data[i][0]=1;
			data[i][1]=ind;
		}

		memset(dynamic, -1, sizeof(dynamic));
		printf("Case #%d: %d\n", caseN, getDynamic(0, 0, 0));
	}

	return 0;
}

int getDynamic(int nth, int blue, int orange)
{
	if(nth==n) return 0;
	int &ret=dynamic[nth][blue][orange];
	if(ret!=-1) return ret;

	ret=999999999;
	if(data[nth][0]==0)
	{
		int bDist=data[nth][1]-blue;
		if(bDist<0) bDist*=-1;
		bDist++;

		for(int i=0;i<100;i++)
		{
			int oDist=orange-i;
			if(oDist<0) oDist*=-1;

			int dist=(oDist>bDist?oDist:bDist);
			int temp=getDynamic(nth+1, data[nth][1], i)+dist;
			if(ret>temp) ret=temp;
		}
	}
	else
	{
		int oDist=data[nth][1]-orange;
		if(oDist<0) oDist*=-1;
		oDist++;

		for(int i=0;i<100;i++)
		{
			int bDist=blue-i;
			if(bDist<0) bDist*=-1;

			int dist=(oDist>bDist?oDist:bDist);
			int temp=getDynamic(nth+1, i, data[nth][1])+dist;
			if(ret>temp) ret=temp;
		}
	}

	return ret;
}
