#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

using namespace std;

#define MAX 8

void sort(int *a, int n, bool asc)
{
	int t;
	if(asc)
	{
		for(int i=0;i<n;i++)	for(int j=0;j<i;j++)
			if(a[i]<a[j])
				{ t=a[i]; a[i]=a[j]; a[j]=t;}
		return;
	}

	for(int i=0;i<n;i++)	for(int j=0;j<i;j++)
		if(a[i]>a[j])
			{ t=a[i]; a[i]=a[j]; a[j]=t;}
}

int main()
{
	int num_test_cases;
	scanf("%d ", &num_test_cases);

	for(int test=1;test<=num_test_cases;test++)
	{
		int n, v1[MAX], v2[MAX], x=0;
		scanf("%d",&n);

		for(int r=0;r<n;r++)	scanf("%d",&v1[r]);
		for(int r=0;r<n;r++)	scanf("%d",&v2[r]);
		
		sort(v1,n,true);
		sort(v2,n,false);
		
		for(int i=0;i<n;i++)
			x+=v1[i]*v2[i];

		printf("Case #%d: %d\n",test,x);
	}

	return 0;
}
