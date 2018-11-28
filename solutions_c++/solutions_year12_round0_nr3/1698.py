#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int A,B;
bool mark[2000001];

int cycle(int n)
{
	if(mark[n]) return 0;

	int stk[20],top=0,i,j,lim=1,s=0;

	while(n){ stk[top++]=n%10; n/=10; }
	reverse(stk,stk+top);

	for(i=0;i<top-1;++i) lim *= 10;

	for(i=0;i<top;++i){
		n = 0;
		for(j=i;j<top;++j) n = 10*n + stk[j];
		for(j=0;j<i;++j) n = 10*n + stk[j];
		
		if(n>=lim&&A<=n&&n<=B){
			if(mark[n]==false){
				++s;
				mark[n] = true;
			}
		}
	}

	return s*(s-1)/2;
}

int main()
{
	//freopen("C-large.in","r",stdin);
	//freopen("C-large.out","w",stdout);

	int t,cs=0,i,s;
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&A,&B);
		s=0; memset(mark,0,sizeof(mark));
		for(i=A;i<=B;++i) s += cycle(i);
		//s += cycle(123);
		printf("Case #%d: %d\n",++cs,s);
	}

	return 0;
}

