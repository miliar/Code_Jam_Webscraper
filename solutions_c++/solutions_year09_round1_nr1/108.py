#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

const int maxn=20000000;

int t, ans;
int f[10][maxn];
vector<int> a;

void analyze(string str)
{
	int cur = 0;
	for (int i=0; i<str.length(); i++)
	{
		if (str[i]>='0'&&str[i]<='9')
			cur = cur*10 + str[i] - 48;
		else
		{
			a.push_back(cur);
			cur = 0;
		}
	}
	if (cur!=0)
		a.push_back(cur);
}

void prepare(int i)
{
	f[i-1][1] = 1;
	for (int a=2; a<maxn; a++)
	{
		vector<int> back;
		int ba = a, cur = 0;
		while (true)
		{
			if (f[i-1][a] != 0)
				break;
			while (ba!=0)
			{
				cur += (ba%i)*(ba%i);
				ba=ba/i;
			}
			if (cur>=maxn)
				f[i-1][a] = -1;
			if (f[i-1][cur] == -1)
				f[i-1][a] = -1;
			else if (f[i-1][cur] == 1)
				f[i-1][a] = 1;
			else if (f[i-1][cur] == -2)
				f[i-1][a] = -1;
			else
				f[i-1][cur] = -2;
			ba = cur;
			back.push_back(cur);
			cur = 0;
		}
		for (int k=0; k<back.size(); k++)
			if (back[k]<maxn)
				f[i-1][back[k]] = f[i-1][a];
	}
}

void calc()
{
	for (ans = 2; ans<maxn; ans++)
	{
		bool flag = true;
		for (int i=0; i<a.size(); i++)
			if (f[a[i]-1][ans]!=1)
			{
				flag = false;
				break;
			}
		if (flag)
			break;
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	string str;
	int k = 0;
	getline(cin, str);
	memset(f,0,sizeof(f));
	for (int i=2; i<=10; i++)
		prepare(i);
	while (t>0)
	{
		t--;
		k++;
		getline(cin, str);
		a.clear();
		analyze(str);
		calc();
		cout << "Case #" << k << ": " << ans << endl;
	}
	return 0;
}