#include<stdio.h>
#include<math.h>
#include<vector>
#include<string.h>
#include<iostream>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	int n;
	char s[2];
	int x;

	int o,b;
	int ans;

	int cas = 1;
	int now;

	int preo,preb;

	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		ans =0;
		now = 0;
		o = 1;
		b = 1;
		preo = 0;
		preb = 0;
		while(n--){
			scanf("%s %d",&s,&x);
			if(s[0] == 'O'){
				int tmp = abs(x-o);
				o = x;
				preb = max(preb+tmp,preo) + 1;
			}
			else{
				int tmp = abs(x-b);
				b = x;
				preo = max(preo+tmp,preb) + 1;
			}
		}
		printf("Case #%d: %d\n",cas++,max(preb,preo));
	}
	return 0;
}