#include<cstdio>
#include<queue>
#include<algorithm>
#define MP make_pair
#define PII pair<int,int> 
#define F first
#define S second
using namespace std;
int test,ntest,n,i,j,po,pb,to,tb,wyn;
char s[3];
int abs(int x){ return x<0?-x:x; }
queue<PII> qo,qb;

int main()
{
	scanf("%d",&ntest);
	for(test=1; test<=ntest; ++test)
	{
		scanf("%d",&n);
		for(i=0; i<n; ++i)
		{
			scanf("%s%d",s,&j);
			if(s[0]=='O') qo.push(MP(j,i));
			else qb.push(MP(j,i));
		}
		to=tb=0;
		po=pb=1;
		wyn=0;
		while((!qo.empty())&&(!qb.empty()))
		{
			if(qo.front().S<qb.front().S) {
				wyn=max(wyn,to+abs(po-qo.front().F))+1;
				po=qo.front().F;
				to=wyn;
				qo.pop();
			} else {
				wyn=max(wyn,tb+abs(pb-qb.front().F))+1;
				pb=qb.front().F;
				tb=wyn;
				qb.pop();
			}
		}
		while(!qo.empty()) {
			wyn=max(wyn,to+abs(po-qo.front().F))+1;
			po=qo.front().F;
			to=wyn;
			qo.pop();
		}
		while(!qb.empty()) {
			wyn=max(wyn,tb+abs(pb-qb.front().F))+1;
			pb=qb.front().F;
			tb=wyn;
			qb.pop();
		}
		printf("Case #%d: %d\n",test,wyn);
	}
}

