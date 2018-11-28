#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int T;
int N;

void main()
{

	int i,j;
	int  x;
	int count;
	vector<int>  a;
	vector<int>  b;


	scanf("%d",&T);
	

	for(i=1;i<=T;i++)
	{

		count=0;

		scanf("%d",&N);
		
		for(j=0;j<N;j++)
		{
			scanf("%d",&x);
			a.push_back(x);
		}

		for(j=0;j<N;j++)
		{
			scanf("%d",&x);
			b.push_back(x);
		}

		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		
		for(j=0;j<N;j++)
			count+=a[j]*b[N-1-j];
		

		printf("Case #%d: %d\n",i,count);
		a.clear();
		b.clear();


	}

}