#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stdlib.h>
#include <cmath>
using namespace std;

int len[1005];
int lenx[1005];
bool comp(int a,int b)
{
	return a>b;
}

int main()
{
	freopen("e:\\B-small.in", "r", stdin);	freopen("e:\\B-small.out", "w", stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int l,t,n,c;
		long long res=0;
		scanf("%d%d%d%d",&l,&t,&n,&c);
		for(int j=0;j<c;j++)
		{
			scanf("%d",&len[j]);
			len[j]=2*len[j];
		}
		int cnt=0;
		long long res1=0;
		int test;
		for(int j=0;j<n;j++)
		{
			int num=j%c;
			res1=res;
			test=num;
			res=res+len[num];
			if((res) >= t)
			{
				for(int k=j+1;k<n;k++)
				{
					lenx[cnt++]=len[(k%c)];
				}
				break;
			}
		}
		sort(lenx,lenx+cnt,comp);
		for(int j=0;j<cnt;j++)
		{
			if(j < l)
			{
				res=res+lenx[j]/2;
			}
			else
			{
				res=res+lenx[j];
			}
		}		
		int onelen=len[test]-(t-res1);
		lenx[cnt++]=onelen;
		sort(lenx,lenx+cnt,comp);
		res1=t;
		for(int j=0;j<cnt;j++)
		{
			if(j < l)
			{
				res1=res1+lenx[j]/2;
			}
			else
			{
				res1=res1+lenx[j];
			}
		}
		if(res1 < res)
			res=res1;
		printf("Case #%d: %lld\n",i+1,res);
		
	}
	return 0;
}