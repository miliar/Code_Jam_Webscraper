#include<iostream>
#include<algorithm>
using namespace std;
#define BIG 99999999999999
int x[801],y[801];
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int i,j,t,cases,num;
	__int64 best,sum;
	cin>>t;
	for(cases=1;cases<=t;cases++)
	{
		cin>>num;
		for(i=1;i<=num;i++)
			cin>>x[i];
		for(j=1;j<=num;j++)
			cin>>y[j];

		best=BIG;
		sum=0;

		sort(x+1,x+1+num);
		sort(y+1,y+1+num);

		for(i=1,j=num;i<=num;i++,j--)
		{
			sum+=x[i]*y[j];
		}

		best=sum;
		cout<<"Case #"<<cases<<": ";
		printf("%I64d\n",best);
	}
	system("pause");
	return 0;
}