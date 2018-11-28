#include <stdio.h>
#include <vector>
#include <functional>
#include <algorithm>
using namespace std;
vector<int> a,b;
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	int T,nT;
	scanf("%d",&T);
	nT=T;
	while (T--)
	{
		a.clear();
		b.clear();
		int N,i,v;
		scanf("%d",&N);
		for (i=0;i<N;i++)
		{
			scanf("%d",&v);
			a.push_back(v);
		}
		for (i=0;i<N;i++)
		{
			scanf("%d",&v);
			b.push_back(v);
		}
		sort(a.begin(),a.end(),less<int>());
		sort(b.begin(),b.end(),greater<int>());
		long long p=0;
		for (i=0;i<N;i++)
			p+=((long long)a[i])*b[i];
		printf("Case #%d: %I64d\n",nT-T,p);
	}
	fclose(stdin);
	fclose(stdout);
}