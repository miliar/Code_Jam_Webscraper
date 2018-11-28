#include<iostream>
using namespace std;
#include<algorithm>
#include<string.h>
#define N 1005
struct node{
	char str[105];
}a[N];
char b[N][105];
int mark[N];
int cmp(node a,node b)
{
	if(strcmp(a.str,b.str)<0) 
		return 1;
	else 
		return 0;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k,n1,n2,s,ns(0);
	char ch;
	int sum;
	scanf("%d",&s);
	while(ns<s)
	{
		sum=0;
		scanf("%d",&n1);
		cin.get(ch);
		for(i=0;i<n1;i++)
		{
			cin.getline(a[i].str,105);
		}		
		sort(a,a+n1,cmp);
		memset(mark,0,sizeof(mark));
		scanf("%d",&n2);
		cin.get(ch);
		for(i=0;i<n2;i++)
		{
			cin.getline(b[i],105);
		}
		for(i=0;i<n2;i++)
		{	
			if(i>0&&!strcmp(b[i],b[i-1])) continue;
			j=0;
			while(strcmp(a[j].str,b[i])!=0&&j<n1)
			{
				j++;
			}
			mark[j]++;
			for(k=0;k<n1&&mark[k]>=1;k++);
			if(k==n1)
			{
				 sum+=1;
				 for(k=0;k<n1;k++)
					mark[k]=0;
				 mark[j]=1;		 
			}
			
		}
		
		cout<<"Case #"<<++ns<<": "<<sum<<endl;
	}
	return 0;
}
				
