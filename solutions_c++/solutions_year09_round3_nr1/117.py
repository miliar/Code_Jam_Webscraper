#include <iostream>

using namespace std;

long long ans;
int f[100];
int a[100];
int n;

void init()
{
	char s[100];
	cin>>s;
	n = 0;
	memset(f,-1,sizeof(f));
	for (int i=0;s[i];i++,n++)
		if (s[i]>='0'&& s[i]<='9') 
			a[i] = s[i]-'0';
		else a[i] = s[i]-'a'+10;
}
void calc()
{
	int base = 2;
	if (n==1)
	{
		ans = 1;
		return;
	}
	f[a[0]] = 1;
	int c = 0;
	for (int i=0;i<n;i++)
	{
		if (f[a[i]]==-1)
		{
			f[a[i]]=c++;
			if (c==1) c++;
		}
		if (base<f[a[i]]+1) base = f[a[i]]+1;
	}
	ans = 0;
	for (int i=0;i<n;i++)
		ans=ans*base+f[a[i]];
		
}
int main()
{
	int t;
	cin>>t;
	for (int i=0;i<t;i++)
	{
		init();
		calc();
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
		
	}

}
