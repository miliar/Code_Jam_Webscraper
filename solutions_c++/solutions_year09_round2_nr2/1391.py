#include<iostream>
#include<algorithm>
#include<cmath>
#include<stdio.h>
#define fo(i,u,d) for (long i=(u); i<=(d); ++i)
#define fod(i,u,d) for (long i=(u); i>=(d); --i)
using namespace std;

const long maxn=50;

long t,num[maxn],len;
long long n;

bool cmp(const long &p1, const long &p2)
{
	return p1>p2;
}
void solve()
{
	long pd=1;
	for (len=0; n; n/=10) num[++len]=n%10;
	fo(i,2,len)
		if (num[i]<num[i-1]) {
		   pd=0;
		   long min=10,pos,tmp;
		   fo(j,1,i-1) 
			   if (num[j]>num[i] && min>num[j]) min=num[j], pos=j;
		   tmp=num[i], num[i]=num[pos], num[pos]=tmp;
		   sort(num+1,num+i,cmp);
		   break;
	    }
	if (pd) {
		sort(num+1,num+len+1);
		fo(i,1,len) 
			if (num[i]>0) {
			   printf("%d0",num[i]), num[i]=-1;
			   break;
		    }
		fo(i,1,len) if (num[i]>=0) printf("%d",num[i]);
	} else fod(i,len,1) printf("%d",num[i]);
	printf("\n");
}
int main()
{
	freopen("BS.in","r",stdin);
	freopen("BS.out","w",stdout);
	scanf("%d",&t);
	fo(l,1,t) {
		scanf("%I64d",&n);
		printf("Case #%d: ",l);
		solve();
	}
	return 0;
}
