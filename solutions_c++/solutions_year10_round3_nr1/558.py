#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int pt[1005][2];

void work()
{
	int n;
	scanf("%d", &n);
	int i, j;
	int cnt = 0;
	for(i = 0; i < n; i ++)
	{
		scanf("%d%d", &pt[i][0], &pt[i][1]);
		for(j = 0; j < i; j ++)
		{
			if((pt[i][0] > pt[j][0]) && (pt[i][1] < pt[j][1]))
				cnt ++;
			
			else if((pt[i][0] < pt[j][0]) && (pt[i][1] > pt[j][1]))
				cnt ++;	
		}
			
	}
	printf("%d\n", cnt)	;
}


int main()
{
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	int kase;
	int t;
	scanf("%d", &t);
	for(kase = 1; kase <= t; kase ++)
	{
		printf("Case #%d: ", kase);
		work();
	}	

	return 0;
	
}
