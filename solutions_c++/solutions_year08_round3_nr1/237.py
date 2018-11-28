#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;

int num[1002];
int p,k,l;

int main()
{

	freopen("A-large.in","r",stdin);
	freopen("A-large.sol","w",stdout);
	int ncase ,x ,i ,j;
	scanf("%d",&ncase);
	
	for(x=1;x<=ncase;x++) {

		int error=0;
		long long sum = 0;

		scanf("%d%d%d",&p,&k,&l);
		if(l > p*k)
			error = 1;
		
		for(i=0;i<l;i++)
			scanf("%d",&num[i]);
		sort(num , num + l , greater<int>());

		int cnt = 0;
		long long keyPress = 1;
		for(i=0;i<l;i++ ,cnt++) {
			if(cnt == k) {
				cnt = 0;
				keyPress++;
			}
			sum += (long long)num[i] * keyPress;
		}

		printf("Case #%d: ",x);
		if(error) printf("IMPOSSIBLE\n");
		else cout << sum << endl;
	}
	
	return 0;
}
