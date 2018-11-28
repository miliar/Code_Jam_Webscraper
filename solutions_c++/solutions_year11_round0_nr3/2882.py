#include<iostream>
using namespace std;

int work(int test_now)
{
	int x=0;
	int tot,min=99999999,num;
	cin>>num;
	for (int i=0; i<num; i++)
		{
			int y;
			cin>>y;
			x^=y;
			tot+=y;
			if (y<min)
				min=y;
		}
	cout<<"Case #"<<test_now+1<<": ";
	if (x==0)
		cout<<tot-min<<endl;
	else
		cout<<"NO"<<endl;
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
