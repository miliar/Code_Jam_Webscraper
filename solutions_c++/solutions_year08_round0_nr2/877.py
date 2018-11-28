#include<iostream>
using namespace std;
#include<algorithm>
#define N 105
bool mark1[N],mark2[N];
struct node1{
	int st;
	int ed;
}a[N];
struct node2{
	int st;
	int ed;
}b[N];
int cmp1(node1 a,node1 b)
{
	if(a.st!=b.st)
		return a.st<b.st;
	else 
		return a.ed<b.ed;
}
int cmp2(node2 a,node2 b)
{
	if(a.st!=b.st)
		return a.st<b.st;
	else
		return a.ed<b.ed;
}
int main()
{
	int i,j,k,t,s,n1,n2,ns(0);
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>s;
	while(ns<s)
	{
		cin>>t;
		cin>>n1>>n2;
		for(i=0;i<n1;i++)
		{
			scanf("%d:%d",&j,&k);
			a[i].st=j*60+k;
			scanf("%d:%d",&j,&k);
			a[i].ed=j*60+k;
		}
		for(i=0;i<n2;i++)
		{
			scanf("%d:%d",&j,&k);
			b[i].st=j*60+k;
			scanf("%d:%d",&j,&k);
			b[i].ed=j*60+k;
		}
		sort(a,a+n1,cmp1);
		sort(b,b+n2,cmp2);
	
		memset(mark1,0,sizeof(mark1));
		memset(mark2,0,sizeof(mark2));
		for(i=0;i<n1;i++)
		{
			for(j=0;j<n2;j++)
			{
				if(!mark2[j]&&a[i].st>=b[j].ed+t)
				{
					mark1[i]=1;//不用从A开过来 
					mark2[j]=1; 
					break;
				}
			}
		}
		int sum1(0),sum2(0);
		for(i=0;i<n1;i++)
			if(!mark1[i]) sum1+=1;
		memset(mark1,0,sizeof(mark1));
		memset(mark2,0,sizeof(mark2));
		for(i=0;i<n2;i++)
			for(j=0;j<n1;j++)
				if(!mark1[j]&&b[i].st>=a[j].ed+t)
				{
					mark1[j]=1;
					mark2[i]=1;
					break;
				}
		for(i=0;i<n2;i++)
			if(!mark2[i])
				sum2++;
		cout<<"Case #"<<++ns<<": "<<sum1<<" "<<sum2<<endl;
	}
	return 0;
}
