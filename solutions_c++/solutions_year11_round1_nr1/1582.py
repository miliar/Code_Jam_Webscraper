#include <iostream>
#include<cmath>
#include<set>
#include<vector>
#include<map>
#include<algorithm>
#include<string>

using namespace std;

int mygcd(int a, int b)
{
	if(b == 0)
		return a;
	return mygcd(b,a%b);
}

int main()
{
	if(freopen("C:\\SANDBOX\\chocolates\\Debug\\input.txt", "r", stdin)&&freopen("C:\\SANDBOX\\chocolates\\Debug\\output.txt", "w", stdout))
	{
		//cout<<"Sucess!!";
	}
	else
	{
		cout<<"Fail!!";
		return 0;
	}

int num,sn;

int n,pd,pg,g;

cin>>num;
sn = 0;
while(num--)
{
	cin>>n>>pd>>pg;
	sn++;
	if(pg == 100 && pd != 100)
	{
		cout<<"Case #"<<sn<<": Broken"<<endl;
		continue;
	}
	else if(pd != 0 && pg == 0)
	{
		cout<<"Case #"<<sn<<": Broken"<<endl;
		continue;
	}
	else if(pd == 0)
	{
		cout<<"Case #"<<sn<<": Possible"<<endl;
		continue;
	}

	g = mygcd(pd,100);
	if((100/g) <= n)
		cout<<"Case #"<<sn<<": Possible"<<endl;
	else
		cout<<"Case #"<<sn<<": Broken"<<endl;
}
}
