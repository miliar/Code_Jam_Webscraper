#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#define eps 1e-11
#define INF (2<<31)-1

using namespace std;

int max(int a, int b) {
	if(a>b) return a;
	return b;
}
int min(int a, int b){
	if(a<b) return a;
	return b;
}


int T, n, a[1000005];





int main()
{
	freopen("L.in","r",stdin);
		freopen("out2.txt","w",stdout);
	int i, ct=1, res, y;
	scanf("%d", &T);
	while(T--)
	{
		y=0;
		res=0;
		scanf("%d", &n);
		for(i=0;i<n;i++)
		{
			scanf("%d", &a[i]);
			y=y^a[i];
			res+=a[i];
		}
		sort(a, a+n);
		if(y==0)
			printf("Case #%d: %d\n", ct++, res-a[0]);
		else
			printf("Case #%d: NO\n", ct++);
	}
	return 0;
	
}
