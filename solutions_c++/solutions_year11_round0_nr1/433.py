#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

void runCase()
{
	int N;
	scanf("%d",&N);
	
	int o,b;
	o = 1;
	b = 1;
	int res = 0;
	
	int lto = 0;
	int ltb = 0;
	for(int i = 0; i < N; i++) {
		char nm[2];
		int botton;
		scanf("%s %d",nm,&botton);
		
		if(nm[0] == 'O') {
			int nt = abs(botton-o)+1;
			nt -= lto;
			if(nt < 1) nt = 1;
			res += nt;
			
			o = botton;
			ltb += nt;
			lto = 0;
		}
		else {
			int nt = abs(botton-b)+1;
			nt -= ltb;
			if(nt < 1) nt = 1;
			res += nt;
			
			b = botton;
			lto += nt;
			ltb = 0;
		}
	}
	
	printf("%d\n",res);
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();
	
	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
	}
}

int main()
{
	solve();
	return 0;
}
