#include <stdio.h>
#include <string.h>
#include <queue>
using namespace std;

int plist[80000],pcount=0;

bool prime(int n){
	int i;
	if((n!=2&&!(n%2))||(n!=3&&!(n%3))||(n!=5&&!(n%5))||(n!=7&&!(n%7)))
		return 0;
	for(i =0;plist[i]*plist[i]<=n;i++)
		if(!(n%plist[i]))
			return 0;
	return n>1;
}

void initprime(){
	int i;
	for(plist[pcount++]=2,i=3;i<2000;i++)
		if(prime(i))
			plist[pcount++]=i;
}
int fac[2000];

void split(int n){
	memset(fac,0,sizeof(fac));
	int i;
	for (i = 0;i < pcount && plist[i]*plist[i] <= n;i++)
	{
		if(n % plist[i])continue;
		while(n%plist[i] == 0)n/=plist[i],++fac[plist[i]];
	}
	if (n != 1)
	{
		fac[n] = 1;
	}
}
int z[2000];
bool combine(int n){
	bool flag = false;
	for (int i = 2;i <= n;i++)
	{
		if (z[i] < fac[i])
		{
			flag = true;
			z[i] = fac[i];
		}
	}
	return flag;
}
int maxT(int n){
	memset(z,0,sizeof(z));
	int ret = 1;
	int i;
	for (i = 2;i <= n;i++)
	{
		split(i);
		combine(i);
	}
	for (i = 2;i <= n;i++)
		ret += z[i];
	return ret;
}
int minT(int n){
	priority_queue<int> pq;
	for (int i = 2;i <=n;i++)
	{
		if (z[i] > 0)
		{
			int k = 1;
			while(z[i]--)k*=i;
			pq.push(k);
		}
	}
	while (pq.size() > 1)
	{
		int x = pq.top();
		pq.pop();
		int y = pq.top();
		pq.pop();
		if(x * y <= n)
			pq.push(x*y);
		else{
			pq.push(x);
			pq.push(y);
			break;
		}
	}
	return pq.size();
}
int work(int n){
	if(n == 1)
		return 0;
	return maxT(n) - minT(n);
}
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	initprime();
	int T,t=1,n;
	scanf("%d",&T);
	while (T--)
	{
		scanf("%d",&n);
		printf("Case #%d: %d\n",t++,work(n));
	}
	return 0;
}