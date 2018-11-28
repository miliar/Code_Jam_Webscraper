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
	for (int z=0;z<q;z++)
	{
		long long a,b,c;
		cin>>a>>b>>c;
		long long x[10000];
		for (int i=0;i<c;i++)
			cin>>x[i];
		sort(x,x+c,co);
		long long tt=0;
		for (int i=0;i<c;i++)
			tt+=(i/b+1)*x[i];
		cout<<"Case #"<<z+1<<": "<<tt<<endl;
	}
	return 0;
}