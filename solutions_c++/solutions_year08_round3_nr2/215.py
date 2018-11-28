#include<iostream>
using namespace std;
//int hash[]={2,3,5,7};
string s;
char t[20];
int len,ans;

typedef long long I;

I solve()
{
	I sum=0,tmp=0,l=1;
	for(int i=s.length()-1;i>=0;i--)
	{
		if(s[i]=='+')
		{
			sum+=tmp;tmp=0;l=1;
		}
		else if(s[i]=='-')
		{
			sum-=tmp;tmp=0;l=1;
		}
		else
		{
			tmp=(s[i]-'0')*l+tmp;
			l*=10;
		}
	}
	return sum;
}

void search(int d)
{
	s+=t[d];
	if(d==len-1)
	{
		I sum=solve();
		if(sum%2==0||sum%3==0||sum%5==0||sum%7==0)
			ans++;
	}
	else
	{
		search(d+1);
		s+='+';search(d+1);s=s.assign(s,0,s.length()-1);
		s+='-';search(d+1);s=s.assign(s,0,s.length()-1);
	}
	s=s.assign(s,0,s.length()-1);
}

int main()
{
//	freopen("D:\\in.txt", "r", stdin );
//	freopen("D:\\out1.txt", "w", stdout);
	int cas;
	scanf("%d",&cas);
	for(int ca=1;ca<=cas;ca++)
	{
		scanf("%s",t);
		len=strlen(t);
		s='+';
		ans=0;
		search(0);
		printf("Case #%d: %d\n",ca,ans);
	}
}
