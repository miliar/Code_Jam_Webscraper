#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#define MAX1 600 
#define MAX2 60
using namespace std;

	int *ans[MAX1][MAX1];
ifstream in("C-large.in");
ofstream out("data.out");
class a
{
	string str;
	string org;
	int len;
	int org_len;
	//int *ans[MAX1][MAX1];
	//char str[MAX];	
public:
	a();
	void process();
};
a::a()
{
	getline(in, str);
	len = str.length();
//	org = "ab";
	org = "welcome to code jam";
	org_len = org.length();
//	cout<<str<<endl;	
//	cout<<org<<endl;
}
void a::process()
{
	for(int i = 0;i < len ;i++)
	{
		if(str[i] == org[0])
		{
			ans[i][i][0] = 1;
		}
		else
		{
			ans[i][i][0] = 0;
		}
	}
	for(int p = 1;p <= len - 1;p++)
	{
		for(int i = 0;i < len - p;i++)
		{
			for(int k = 0;k < org_len;k++)
			{
				int j = i + p;
				if(str[j] != org[k])
				{
					ans[i][j][k] = ans[i][j - 1][k];
				}
				else
				{
					if(k != 0)
					{

	
						ans[i][j][k] = (ans[i][j - 1][k - 1] + ans[i][j - 1][k]) % 10000;
					}
					else
					{
						ans[i][j][k] = (1 + ans[i][j - 1][k]) % 10000;
					}
				}
//				cout<<ans[i][j][k]<<endl;
			}
		}
	}
	int final =ans[0][len - 1][org_len - 1] ; 
	/*if(final < 10)
	{
		cout<<"000"<<final<<endl;
	}
	else if(final < 100)
	{
		cout<<"00"<<final<<endl;
	}
	else if(final < 1000)
	{
		cout<<"0"<<final<<endl;
	}
	else	
	{
		cout<<final<<endl;
	}
	*/
	if(final < 10)
	{
		out<<"000"<<final<<endl;
	}
	else if(final < 100)
	{
		out<<"00"<<final<<endl;
	}
	else if(final < 1000)
	{
		out<<"0"<<final<<endl;
	}
	else	
	{
		out<<final<<endl;
	}
}
	
void solve()
{
	class a myobj;
	myobj.process();
}
int main()
{
	for(int i = 0;i < MAX1;i++)
	{
		for(int j= 0;j < MAX1;j++)
		{
			ans[i][j] = new int[40];
		}
	}
	string s;
	int t;
	int i = 1;
	getline(in, s);
	istringstream sin(s);
	sin>>t;
	char c;
//	in>>c;
	while(i <= t)
	{
		out<<"Case #"<<i<<": ";

		solve();
		i++;
	}
	return 0;
}
