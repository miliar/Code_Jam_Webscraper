#include<cstdio>

#define IN "A-large.in"
#define OUT "A-large.out"

bool isOn(const int &N,const int &K)
{
	int step=(1<<N);
	int initial=step-1;
	return (K-initial)%step==0;
}

int main()
{
	freopen(IN,"r",stdin);
	freopen(OUT,"w",stdout);

	int T;
	scanf("%d",&T);
	for(int caseID=1;caseID<=T;caseID++)
	{
		int N,K;
		scanf("%d %d",&N,&K);
		printf("Case #%d: %s\n",caseID,isOn(N,K)?"ON":"OFF");
	}
	return 0;
}
