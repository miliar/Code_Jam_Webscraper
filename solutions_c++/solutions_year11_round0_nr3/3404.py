#include<stdio.h>
#include<algorithm>
using namespace std;
int sum(int a[], int n)
{
    int i;
    int sum = 0;
    for(i=0; i<n; ++i)
	sum += a[i];
    return sum;
}


int main()
{
    int t;
    int n;
    int i, j;
    int a[10000];
    scanf("%d", &t);
    int max = 0;
    int tp = 1;
    int sum1;
    int sean, pat;
    int temp;
    while(t--)
    {
	max = 0;
	scanf("%d", &n);
	for(i=0; i<n; ++i)
	{
	    scanf("%d", &a[i]);
	}
	std::sort(a,a+ n);

	sum1 = sum(a,n);		//sm of elts

	temp = 0;
	for(i=0; i<n; ++i)
	{
	    temp = temp^a[i];
	}
	if(temp == 0)
	{
	    for(i=1; i<n; ++i)
	    {
		max += a[i];
	    }
	}


	if(max == 0)
	    printf("Case #%d: NO\n", tp);
	else
	{
	    printf("Case #%d: %d\n", tp, max);
	}
	tp ++;
    }

    return 0;
}

