#include<iostream>
using namespace std;

int gcd(int x,int y)
{
	if (y==0) 
		return x;
	else
		return gcd(y, x%y);
}

int work(int test_now)
{
	cout<<"Case #"<<test_now+1<<": ";
	long long n, pd, pg;
	cin>>n>>pd>>pg;
	if (pg==0&&pd>0)
	{
		cout<<"Broken"<<endl;
		return 0;
	}
	if (pg==100&&pd<100)
	{
		cout<<"Broken"<<endl;
		return 0;
	}
	if (n>=100/gcd(pd,100))
	{
		cout<<"Possible"<<endl;
	}
	else
		cout<<"Broken"<<endl;
	return 0;
}


int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);

	int test_num;
	cin>>test_num;
	for (int i=0; i<test_num; i++)
		work(i);

	return 0;
}
