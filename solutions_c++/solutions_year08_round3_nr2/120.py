#include<iostream>
#include<cstring>
using namespace std;
char dig[41];
int check[41];
int len,rrr;
void force(int loc)
{
	check[loc]=1;
	if(loc==len-1)
	{
		__int64 res=dig[0]-'0';
		int i=1;
		while(i<=loc&&check[i]==1)
		{
			res*=10;
			res+=dig[i]-'0';
			i++;
		}
		while(i<=loc)
		{
			__int64 tt=dig[i]-'0';
			int j=i+1;
			while(j<=loc&&check[j]==1)
			{
				tt*=10;
				tt+=dig[j]-'0';
				j++;
			}
			if(check[i]==2)res+=tt;
			else res-=tt;
			i=j;
		}
		if(res%2==0||res%3==0||res%5==0||res%7==0)rrr++;
	}
	else force(loc+1);
	check[loc]=2;
	if(loc==len-1)
	{
		__int64 res=dig[0]-'0';
		int i=1;
		while(i<=loc&&check[i]==1)
		{
			res*=10;
			res+=dig[i]-'0';
			i++;
		}
		while(i<=loc)
		{
			__int64 tt=dig[i]-'0';
			int j=i+1;
			while(j<=loc&&check[j]==1)
			{
				tt*=10;
				tt+=dig[j]-'0';
				j++;
			}
			if(check[i]==2)res+=tt;
			else res-=tt;
			i=j;
		}
		if(res%2==0||res%3==0||res%5==0||res%7==0)rrr++;
	}
	else force(loc+1);
	check[loc]=3;
	if(loc==len-1)
	{
		__int64 res=dig[0]-'0';
		int i=1;
		while(i<=loc&&check[i]==1)
		{
			res*=10;
			res+=dig[i]-'0';
			i++;
		}
		while(i<=loc)
		{
			__int64 tt=dig[i]-'0';
			int j=i+1;
			while(j<=loc&&check[j]==1)
			{
				tt*=10;
				tt+=dig[j]-'0';
				j++;
			}
			if(check[i]==2)res+=tt;
			else res-=tt;
			i=j;
		}
		if(res%2==0||res%3==0||res%5==0||res%7==0)rrr++;
	}
	else force(loc+1);
}
int main()
{
	int n,flag=1;
	freopen("B-small-attempt0.in.txt","r",stdin);
	freopen("bbb.out","w",stdout);
	cin>>n;
	while(n--)
	{
		cin>>dig;
		len=strlen(dig);
	
		printf("Case #%d: ",flag++);
		if(len==1)
		{
			__int64 ts=dig[0]-'0';
			if(ts%2==0||ts%3==0||ts%5==0||ts%7==0)
				cout<<1<<endl;
			else cout<<0<<endl;
			continue;
		}
		rrr=0;
		force(1);
		cout<<rrr<<endl;
		
	}
	return 0;
}