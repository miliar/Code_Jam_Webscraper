#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
#include<set>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<vector>
#include<iostream>
#define PINF 2000000000
#define NINF -2000000000
using namespace std;
struct node
{
	long long type;
	long long v;
}box[101],toy[101];
long long n,m,t,c;
long long search(long long id,long long idx,long long val)
{
	//prlong longf("%d %d %I64d %I64d %I64d\n",id,idx,box[id].v,toy[idx].v,val);
	if(id==n || idx==m)
		return val;
	if(box[id].type==toy[idx].type)
	{
		long long temp,ans;
		if(box[id].v>toy[idx].v)
		{
			temp=box[id].v;
			box[id].v-=toy[idx].v;
			ans=search(id,idx+1,val+toy[idx].v);
			box[id].v=temp;
			return ans;
		}
		else
		{
			temp=toy[idx].v;
			toy[idx].v-=box[id].v;
			ans=search(id+1,idx,val+box[id].v);
			toy[idx].v=temp;
			return ans;
		}
	}
	else
		return max(search(id+1,idx,val),search(id,idx+1,val));
}
int  main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%I64d",&t);
	for(long long c=1;c<=t;c++)
	{
		scanf("%I64d %I64d",&n,&m);
		for(long long i=0;i<n;i++)
			scanf("%I64d %I64d",&box[i].v,&box[i].type);
		for(long long i=0;i<m;i++)
			scanf("%I64d %I64d",&toy[i].v,&toy[i].type);
		printf("Case #%I64d: %I64d\n",c,search(0,0,0));
	}
    scanf(" ");
}

