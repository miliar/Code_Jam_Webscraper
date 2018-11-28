#include <cstdio>
#include <algorithm>

using namespace std;

long double combi[1001][1001];
long double derangement[1001];
long double fact[1001];

long double dynamic[1001];
bool isVisit[1001];

long double getDynamic(int left);

int caseN;

int main(void)
{
	combi[1][0]=combi[1][1]=1;
	for(int i=2;i<=1000;i++)
	{
		for(int j=0;j<=i;j++)
		{
			if(j==0 || j==i) combi[i][j]=1;
			else combi[i][j]=combi[i-1][j-1]+combi[i-1][j];
		}
	}

	derangement[0]=1, derangement[2]=1, derangement[3]=2;
	fact[0]=fact[1]=1;
	fact[2]=2, fact[3]=6;
	for(int i=4;i<=1000;i++)
	{
		derangement[i]=(i-1)*(derangement[i-1]+derangement[i-2]);
		fact[i]=i*fact[i-1];
	}

	int t;
	scanf("%d", &t);
	for(caseN=1;caseN<=t;caseN++)
	{
		int n, data[1000], sorted[1000];
		scanf("%d", &n);
		for(int i=0;i<n;i++)
		{
			scanf("%d", data+i);
			sorted[i]=data[i];
		}
		
		sort(sorted, sorted+n);

		int sameCnt=0;
		for(int i=0;i<n;i++) if(data[i]==sorted[i]) sameCnt++;

		printf("Case #%d: %.10lf\n", caseN, (double)getDynamic(n-sameCnt));
	}

	return 0;
}

long double getDynamic(int left)
{
	long double &ret=dynamic[left];
	if(isVisit[left]) return ret;
	isVisit[left]=true;

	ret=0;
	if(left>0)
	{
		for(int i=1;i<=left;i++)
		{
			long double rightPos=combi[left][i];
			long double falsePos=derangement[left-i];
			long double totPos=fact[left];

			long double portion=rightPos*falsePos/totPos;
			long double curAns;

			curAns=portion*(getDynamic(left-i)+1);
			ret+=curAns;
		}

		ret+=derangement[left]/fact[left];

		ret/=(1-derangement[left]/fact[left]);
	}

	return ret;
}
