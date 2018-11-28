#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1; i<=t; i++) {
		int n,s,p,res=0;
		scanf("%d %d %d",&n,&s,&p);
		int l1=max(((p-1)*2+p),p);
		int l2=max(((p-2)*2+p),p);
		while (n--) {
			int score;
			scanf("%d",&score);
			if (score >= l1) {
				res++;
			} else if (s>0 && score>=l2) {
				res++;
				s--;
			}
		}
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}
