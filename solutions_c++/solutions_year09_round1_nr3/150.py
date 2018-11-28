#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

double dynamic[41];
bool isVisit[41];
int c, n;

double getDynamic(int);

double total;

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int caseN=1;caseN<=t;caseN++)
	{
		scanf("%d %d", &c, &n);
		memset(isVisit, 0, sizeof(isVisit));

		total=1;
		for(int i=0;i<n;i++) { total*=(c-i); total/=(i+1); }

		printf("Case #%d: %.10lf\n", caseN, getDynamic(c));
	}

	return 0;
}

double getDynamic(int left)
{
	if(isVisit[left]) return dynamic[left];
	double &ret=dynamic[left];
	isVisit[left]=true;

	ret=0;
	if(left==0) return ret;

	for(int i=1;i<=n;i++)
	{
		int bef=(n-i), news=i;
		if(bef>c-left) continue;
		if(news>left) continue;

		double cnt=1;
		for(int j=0;j<bef;j++) { cnt*=(c-left-j); cnt/=(1+j); }
		for(int j=0;j<news;j++) { cnt*=(left-j); cnt/=(1+j); }

		ret+=(getDynamic(left-i)+1)*cnt/total;
	}

	if(c-left>=n)
	{
		double cnt=1;
		for(int i=0;i<n;i++) { cnt*=(c-left-i); cnt/=(i+1); }
		double p=cnt/total;

		ret=(ret+p)/(1-p);
	}

	return ret;
}
