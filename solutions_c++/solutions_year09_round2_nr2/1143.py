#include<iostream>
#include<cstring>
#include<fstream>
#define MAX
using namespace std;
ifstream in("data.in");
ofstream out("data.out");
class contest
{
	char str[1000];
	int a[1000];
	int dt;
	int n;
	double p;
	int top;
public:
	contest();
	void sort(int a[], int s, int e);
	void process();
};
contest::contest()
{
	in>>str;
	int len = strlen(str);
	for(int i = 0;i < len;i++)
	{
		a[i + 1] = str[len - i - 1] - '0';
	}
	for(int i = 1;i <= len;i++)
	{
//		cout<<a[i]<<endl;
	}
	top = len;
	n = len;
}
void contest::sort(int a[], int s, int e)
{
	for(int i = s; i <= e;i++)
	{
		for(int j = i;j <= e;j++)
		{
			if(a[i] < a[j])
			{
				swap(a[i], a[j]);
			}
		}
	}

}
void contest::process()
{
	int find = 0;
	int ni = 1000;
	int nj = 1000;
	if(n == 1)
	{
		cout<<a[1]<<'0'<<endl;
		out<<a[1]<<'0'<<endl;
		return ;
	}
	for(int i = 1;i <= n;i++)
	{
		for(int j = i;j <= n;j++)
		{
			if(a[i] > a[j] && !(a[j] == 0 && i == n))
			{
				if(j < nj)
				{
					nj = j,ni = i;
					find = 1;
					break;
				}
			}
		}
	}
	if(find == 1)
	{
		swap(a[ni], a[nj]);
		sort(a, 1, nj - 1); 
	}
	if(find == 0)
	{
		int t = 1;
		while(a[t] == 0)t++;
		sort(a, t, top);
		top ++;
		for(int i = top;i > 1;i--)
		{
			a[i] = a[i - 1];
		}
		a[1] = 0;
		sort(a, 1, top - 1);
	}
	find = 0;
	for(int i = top;i >= 1;i--)
	{
		if(a[i] > 0)find = 1;
		if(find)
		{out<<a[i];
		cout<<a[i];
		}
	}
	out<<endl;
	cout<<endl;
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
