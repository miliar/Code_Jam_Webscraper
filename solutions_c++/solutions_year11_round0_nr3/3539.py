#include<iostream>
#include<cstdio>

using namespace std;

int n,sum,now,x,small,Test;
void work()
{
	cin >> n;
	sum = 0; now = 0;
	small = 1000000000;
	for (int i = 0;i<n;++i)
	{
		cin >> x;
		now ^= x;
		sum += x;
		if (x<small) small = x;
	}
	if (now != 0) 
	{
		puts("NO");
		return;
	}
	cout << sum-small << endl;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> Test;
	for (int i = 1;i<=Test;++i)
	{
		printf("Case #%d: ",i);
		work();
	}
	return 0;
}
