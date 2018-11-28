#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int maxn=1024;

int n;
struct node{
	int a,b;
	bool operator < (const node& x)
	{
		return a<x.a;
	}
}x[maxn];
node tmp[maxn];

void input()
{
	int i;
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d%d",&x[i].a,&x[i].b);
	}
}

int merge(node* p, int size)
{
	if(size<=1) return 0;

	int s1=size/2,s2=size-s1,cot=0,i,j;
	int ret=0;
	node* q=&p[s1];
	ret+=merge(p,s1);
	ret+=merge(q,s2);
	for(i=0,j=0;i<s1&&j<s2;)
	{
		if(p[i].b<q[j].b){
			tmp[cot++]=p[i++];
			ret+=j;
		}else{
			tmp[cot++]=q[j++];
		}
	}
	while(i<s1){
		tmp[cot++]=p[i++];
		ret+=j;
	}
	while(j<s2){
		tmp[cot++]=q[j++];
	}
	for(i=0;i<size;i++)p[i]=tmp[i];
	return ret;
}

int solve()
{
	sort(x,x+n);
	return merge(x,n);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int i,T;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		input();
		printf("Case #%d: ",i);
		printf("%d\n",solve());
	}
	return 0;
}