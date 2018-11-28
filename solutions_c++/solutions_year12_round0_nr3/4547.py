#include<stdio.h>
#include<string.h>
bool cmp(int s1[],int s2[],int n)
{
	int i,j;
	for(i=0;i<n;i++)
		if(s1[i]!=s2[i])return 0;
	return 1;
}
void dondur(int k[],int n)
{
	int i,j=k[n-1];
	for(i=n-1;i>0;i--)
		k[i]=k[i-1];
	k[0]=j;
}
bool recycled(int i,int j)
{
	int k1[25],a=0,b=0,s1[25],s2[25];
	while(i)
	{
		k1[a]=s1[a]=i%10;
		a++;
		i/=10;
	}
	while(j)
	{
		s2[b++]=j%10;
		j/=10;
	}
	if(a!=b)return 0;
	dondur(k1,a);
	while(1)
	{
		if(cmp(k1,s1,a))return 0;
		if(cmp(k1,s2,a))return 1;
		dondur(k1,a);
	}
}
int n,m,x;
int main()
{
	FILE *oku=fopen("C-small-attempt0.in","r");
	FILE *yaz=fopen("C-small-attempt0.out","w");
	int i,j,sayac=0,k;
	fscanf(oku,"%d",&x);
	for(k=0;k<x;k++)
	{
		sayac=0;
		fscanf(oku,"%d %d",&n,&m);
		fprintf(yaz,"Case #%d: ",k+1);
		for(i=n;i<=m;i++)
		{
			for(j=n;j<=m;j++)
			{
				if(i==j)continue;
				
				if(recycled(i,j))sayac++;
			}
		}
		fprintf(yaz,"%d\n",sayac/2);
	}
	return 0;
}
