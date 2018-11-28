#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int num,posO,posB,timeO,timeB,n,Test;
char ch;
int use[1000];
void work()
{
	posO = 1;timeO = 0;
	posB = 1;timeB = 0;
	for (int i = 0;i<n;++i) use[i] = 0;

	for (int i = 0;i<n;++i)
	{
		cin >> ch >> num;
		if (ch == 'O')
		{
			timeO += abs(posO-num)+1;
			posO = num;
			if (i>0)
			if (timeO<=use[i-1]) timeO = use[i-1]+1;
			use[i] = timeO;
		}
		else
		{
			timeB += abs(posB-num)+1;
			posB = num;
			if (i>0)
			if (timeB<=use[i-1]) timeB = use[i-1]+1;
			use[i] = timeB;
		}
	//	cout << use[i] << endl;
	}
	cout << use[n-1] << endl;
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> Test;
	//while (Test --)
	for (int i = 1;i<=Test;++i)
	{
		printf("Case #%d: ",i);
		cin >> n;
		work();
	}
	return 0;
}
