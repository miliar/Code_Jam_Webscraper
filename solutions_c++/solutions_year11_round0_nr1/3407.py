#include<iostream>
using namespace std;

int t,n;
char p[200],r[200];

int BotTrust()
{
	int ret=0,i,j,tmp,ot=0,bt=0;
	int o=1,b=1;
	for(i=0;i<n;++i)
	{
		tmp=0;
		if('O'==p[i]){
			tmp=r[i]-o;
			if(tmp<0) tmp=-tmp;
			ot+=tmp;
			if(ot<bt) ot=bt+1;
			else ++ot;
			o=r[i];
		}else{
			tmp=r[i]-b;
			if(tmp<0) tmp=-tmp;
			bt+=tmp;
			if(bt<ot) bt=ot+1;
			else ++bt;
			b=r[i];
		}
		//cout<<i<<":"<<ret<<endl;
	}
	if(ot>bt) ret=ot;
	else ret=bt;
	return ret;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int ti,i;
	scanf("%d",&t);
	for(ti=1;ti<=t;++ti)
	{
		scanf("%d",&n);
		for(i=0;i<n;++i)
			scanf(" %c %d",&p[i],&r[i]);
		printf("Case #%d: %d\n",ti,BotTrust());
	}
	return 0;
}