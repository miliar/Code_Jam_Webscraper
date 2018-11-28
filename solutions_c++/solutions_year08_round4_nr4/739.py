#include<iostream>
using namespace std;
int n,used[5],mn,m,b[5];
char str[1001];
char getchr(int p)
{
	return str[p-p%m+b[p%m]];
}
void search(int d)
{
	int a,t,c;
	if( d==m )
	{
		t=-1;
		c=0;
		for(a=0;a<n;a++)
		{
			if( getchr(a)!=t ) c++;
			t=getchr(a);
		}
		if( c<mn ) mn=c;
		return;
	}
	for(a=0;a<m;a++)
	{
		if( used[a]==1 ) continue;
		b[d]=a;
		used[a]=1;
		search(d+1);
		used[a]=0;
	}
}
int main()
{
	int a,data,cnt;
	scanf("%d",&data);
	cnt=0;
begin: data--; cnt++; printf("Case #%d: ",cnt);
	scanf("%d",&m);
	scanf("%s",&str);
	n=strlen(str);
	for(a=0;a<m;a++) used[a]=0;
	mn=n;
	search(0);
	printf("%d\n",mn);
	if( data>0 ) goto begin;
	return 0;
}
