#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
const __int64 maxn=500001;
const __int64 modo=1000000007;
__int64 n,m,x,y,z;
__int64 A[maxn],a[maxn];
struct fst{
	__int64 v,p;
} tmp[maxn];

bool operator < (const fst &a,const fst &b){
	if (a.v==b.v){
		return a.p>b.p;
	}
	return a.v<b.v;
}

__int64 tree[maxn];

void init(){
	scanf("%I64d%I64d%I64d%I64d%I64d",&n,&m,&x,&y,&z);
	for (__int64 i=0;i<m;i++){
		scanf("%I64d",&A[i]);
	}
	for (__int64 i=0;i<n;i++){
		a[i]=A[i%m];
		A[i%m]=(x*A[i%m]+y*(i+1))%z;
	}
	for (__int64 i=n;i>=1;i--){
		a[i]=a[i-1];
	}
	for (__int64 i=1;i<=n;i++){
		tmp[i].v=a[i];
		tmp[i].p=i;
	}
	sort(tmp+1,tmp+1+n);
	for (__int64 i=1;i<=n;i++){
		a[tmp[i].p]=i;
	}
	memset(tree,0,sizeof(tree));
	return;
}

void insert(__int64 x, __int64 a)
{
	while(x <= n)
	{
		tree[x] += a;
		x+=x&~(x-(__int64)1);
	}
}

__int64 query(__int64 x)
{
	if (x==0){
		return 0;
	}
	__int64 t = 0;
	while(x > 0)
	{
		t += tree[x];
			x&=x-1;
	}
	return t;
}

__int64 f[maxn];

__int64 dp(){
	memset(f,0,sizeof(f));
	f[0]=1;
	__int64 ans=0;
	for (__int64 i=1;i<=n;i++){
		f[i]=1+query(a[i]-1);
		f[i]%=modo;
		ans+=f[i];
		ans%=modo;
		insert(a[i],f[i]);
	}
	return ans;
}

int main(){
	__int64 t;
	scanf("%I64d",&t);
	for (__int64 cse=1;cse<=t;cse++){
		init();
		printf("Case #%I64d: %I64d\n",cse,dp());
	}
	return 0;
}
