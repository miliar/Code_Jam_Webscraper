#include <iostream>
#pragma comment(linker,"/STACK:256000000")

using namespace std;

long long g[2000];
long long used[2000];
long long pr[2000];
long long sums[2000];
long long n,r,k;
long long s[3000];

void gen(long long x){
	if (pr[x]!=-1) return;
	
	long long st=x;
	long long sum=0;
	while (st<x+n&&sum+s[st]<=k){
		sum+=s[st];
		st++;
	}

	if (st==x){
		pr[x]=x;
		sums[x]=sum;
	} else {
		pr[x]=st%n;
		sums[x]=sum;
		gen(st%n);
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	long long t;
	scanf("%I64d",&t);
	for (int tt=1; tt<=t; tt++){
		printf("Case #%d: ",tt);
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		for (int i=0; i<n; i++)
			scanf("%I64d",&g[i]);
		memset(used,0,sizeof(used));
		memset(pr,-1,sizeof(pr));
		memset(sums,0,sizeof(sums));
		for (int i=0; i<n; i++)
			s[i]=g[i];
		for (int i=n; i<3*n; i++)
			s[i]=s[i-n];

		gen(0);

		long long res=0;

		long long ts=0;
		for (int i=0; i<r; i++){
			res+=sums[ts];
			ts=pr[ts];
		}
		printf("%I64d\n",res);
	}	

	return 0;
}