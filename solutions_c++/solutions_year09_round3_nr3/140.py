#include<iostream>
#include<stdio.h>
#include<string.h>
#include<cmath>
#include<algorithm>
using namespace std;
int re[150][150];
int ls[500],ln,data[500],s2l[20010],dn;
int sjr(int a,int b)
{
	if(re[a][b]!=-1)
		return re[a][b];
	int i,j;
	if(a+1==b)
		return re[a][b]=0;
	for(i=a+1;i<b;i++)
	{
		j=-s2l[a]+s2l[b]+sjr(a,i)+sjr(i,b);
		if(a!=0)
			j--;
		if(b!=dn)
			j--;
		if(re[a][b]==-1 || re[a][b]>j)
			re[a][b]=j;
	}
	//cout<<a<<" "<<b<<" "<<re[a][b]<<endl;
	
	return re[a][b];
}
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int i,j,k,l,m,n,y,z,q,p;
	scanf("%d",&z);
	for(y=1;y<=z;y++)
	{
		scanf("%d%d",&p,&q);
		ln=0;
		for(i=0;i<q;i++)
		{
			scanf("%d",data+i);
			ls[ln++]=data[i];
		}
		sort(ls,ls+ln);
		memset(re,-1,sizeof(re));
		j=1;
		for(i=0;i<ln;i++)
		{
			s2l[j]=ls[i];
			j++;
		}
		s2l[0]=1;
		s2l[j]=p;
		dn=j;
		printf("Case #%d: %d\n",y,sjr(0,j));
	}
	return 0;
}
