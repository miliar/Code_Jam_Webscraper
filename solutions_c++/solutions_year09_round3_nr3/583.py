#include<iostream>
#include<cstring>
#include<fstream>
#define MAX
using namespace std;
ifstream in("data.in");
ofstream out("data.out");
class contest
{
	int p,q;
	int cell[10001];
	int re[200];
	int max;
public:
	contest();
	void search(int );
	int cal();
	void process();
};
contest::contest()
{
	in>>p>>q;
	for(int i = 1;i <= q;i++)
	{
		in>>re[i];
	}
	max = 1000000;
}
int contest::cal()
{
	int mark[100001];
	int mon = 0;
	for(int i = 1;i <= p;i++)
	{
		mark[i] = 1;
	} 
	for(int i = 1;i <= q;i++)
	{
		mark[re[i]] = 0;
		for(int j = re[i] - 1;j >= 1 && mark[j] == 1;j--)
		{
			mon++;
		}
		for(int j = re[i] + 1;j <= p && mark[j] == 1;j++)
		{
			mon++;
		}	
	}
	return mon;
}
void contest::search(int i)
{
	if(i > q)
	{
		int ans = cal();
		if(ans < max)
		{
			max = ans;
		}
	}
	else
	{
		for(int j = i; j <= q;j++)
		{
			swap(re[i], re[j]);
			search(i + 1);
			swap(re[i], re[j]);
		}

		
	}
}
void contest::process()
{
	search(1);
	cout<<max<<endl;
	out<<max<<endl;
}
void solve()
{
	class contest myobj;
	myobj.process();
}
int main()
{
	int t;
	int i = 1;
	in>>t;
	while(i <= t)
	{
		cout<<"Case #"<<i<<": ";
		out<<"Case #"<<i<<": ";
		solve();
		i++;
	}
		
	return 0;
}
