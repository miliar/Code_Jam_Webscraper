//B
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
struct level
{
	int a,b,f;
}L[1100];
bool comp(level l1,level l2)
{
	return l1.b>l2.b;
}
int main(){
	int T,n,sum,flag,ff,ans;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for(int cnt=1;cnt<=T;cnt++)
	{
		cin>>n;
		ans=sum=ff=0;
		for(int i=0;i<n;i++) 
		{
			scanf("%d %d",&L[i].a,&L[i].b);
			L[i].f=0;
		}
		sort(L,L+n,comp);
		while(sum<2*n)
		{
			flag=0;
			for(int i=0;i<n;i++)
			{
				if(L[i].f<2 && sum>=L[i].b)
				{
					sum+=2-L[i].f;
					L[i].f=2;
					flag=1;
					ans++;
					break;
				}
			}
			if(flag)continue;
			for(int i=0;i<n;i++)
			{
				if(L[i].f<1 && sum>=L[i].a)
				{
					sum++;
					L[i].f=1;
					flag=1;
					ans++;
					break;
				}
			}
			if(flag==0) {ff=1;break;}
		}
		cout<<"Case #"<<cnt<<": ";
		if(ff)
			cout<<"Too Bad"<<endl;
		else
			cout<<ans<<endl;
	}
	return 0;
}
