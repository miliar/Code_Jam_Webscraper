#include<iostream>
#include<cstring>
#include<fstream>
#define MAX 10000
using namespace std;
ifstream in("data.in");
ofstream out("data.out");
class contest
{
	char s[MAX];
	char a[MAX];
	int n;
	int b;

public:
	contest();
	void process();
};
contest::contest()
{
	in>>s;
	int len = strlen(s);
	n = len;
	
	for(int i = 1;i <= len;i++)
	{
		a[i] = s[len - i];
	}
	int markd[10];
	int marks[26];
	for(int i = 0;i <= 9;i++)
	{
		markd[i] = 0;
	}
	for(int j = 0;j <= 25;j++)
	{
		marks[j] = 0;
	}
	for(int i = 1;i <= len;i++)
	{
		if(a[i] <= '9' && a[i] >= '0')
		{
			markd[a[i] - '0'] = 1;
		}
		else
		{
			marks[a[i] - 'a'] = 1;
		}

	}
	int sum = 0;
	for(int i = 0 ;i <= 9;i++)
	{
		if(markd[i] != 0)
		{
			sum ++;
		}
	}
	for(int j = 0;j <= 25;j++)
	{
		if(marks[j] != 0)
		{
			sum ++;
		}
	}
	if(sum == 1) sum++;
	b = sum;
	char used[1000];
	for(int i = 0;i <= sum;i++)
	{
		used[i] = '$';
	}
	long ans = 0;
	
	for(int i = len;i >= 1;i--)
	{
		int find = 0;
		for(int j = 0;j < sum;j++)
		{
			if(a[i] == used[j])
			{
				find = 1;
				ans = ans * b + j;
				break;
			}
		}
		if(find)continue;
		if(i == len)
		{
			used[1] = a[i];
			ans = ans * b + 1;
		}
		else
		{
			for(int t = 0;t < sum;t++)
			{
				if(used[t] == '$')
				{
					used[t] = a[i];
					ans = ans * b + t;
					break;
				}
			}
		}
	}
	cout<<ans<<endl;
	out<<ans<<endl;
}
void contest::process()
{
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
