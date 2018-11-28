#include <iostream>

using namespace std;


string a;
int tt;
bool co(int a,int b)
{
	return a>b;
}
void go(int lv,string c)
{
	if (lv==a.size())
	{
		long long ss=0;
		long long cc=0;
		cout<<c<<endl;
		if (ss%3==0||ss%2==0||ss%5==0||ss%7==0)
			tt++;
		return;
	}
	go(lv+1,c+"+");
	go(lv+1,c+"-");
	go(lv+1,c+" ");
}

int main()
{
	int q;
	cin>>q;
	for (int zz=0;zz<q;zz++)
	{
		long long tt=0;
		long long n,m,x,y,z;
		cin>>n>>m>>x>>y>>z;
		long long a[1001],b[10001];
		for (int i=0;i<m;i++)
			cin>>a[i];
		for (int i=0;i<n;i++)
		{
			b[i]=a[i%m];
		//	cout<<i<<b[i]<<endl;
			a[i%m]=(x*a[i%m]+y*(i+1))%z;
		}
		long long c[1001]={0};
		for (int i=0;i<n;i++)
			c[i]=1;
		for (int i=1;i<n;i++)
		{
			for (int j=0;j<i;j++)
				if (b[i]>b[j])
					c[i]+=c[j];
			c[i]%=1000000007;
		}
		for (int i=0;i<n;i++)
			tt+=c[i];//,cout<<i<<' '<<c[i]<<endl;
		cout<<"Case #"<<zz+1<<": "<<tt%1000000007<<endl;
	}
	return 0;
}