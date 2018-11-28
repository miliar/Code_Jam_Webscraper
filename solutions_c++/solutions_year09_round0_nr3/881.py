#include <iostream>
#include <vector>
#include <string>
using namespace std;

string need = "welcome to code jam";
int was[505][40];
char tmp[1005];

int solve()
{
	for (int i=0; i<need.size(); i++)
	{
		if (i == 0)
		{
			for (int j=0; tmp[j]; j++)
				if (tmp[j] == need[i])
					was[j][0]++;
		}
		else
		{
			for (int j=0; tmp[j]; j++)
				if (tmp[j] == need[i])
				{
					for (int k=0; k<j; k++)
						was[j][i]+= was[k][i-1];
					was[j][i] %= 10000;
				}
		}
	}
	int ret = 0;
	for (int i=0; tmp[i]; i++)
		ret += was[i][need.size()-1];
	ret %= 10000;
	return ret;
}

string norm(int x)
{
	string ret = "";
	while (x)
	{
		ret = (char)( x%10+'0') + ret;
		x /= 10;
	}
	while (ret.size() < 4)
		ret = '0' + ret;
	return ret;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int N;
	cin >> N;
	cin.getline(tmp,10);
	for (int I=0; I<N; I++)
	{
		memset(was,0,sizeof(was));
		cin.getline(tmp,1000);
		int ret = solve();
		cout << "Case #" << I+1 << ": " << norm(ret) << endl;
	}
}