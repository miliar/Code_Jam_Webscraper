#include <fstream>
#include <string>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

int k;
string t;
int vis[10];
int order[10];
int ans;

void calc(const int &dep)
{
	if (dep == k)
	{
		string tmp = t;
		for (int i = 0; i < t.length()/k; i++)
		{
			for (int j = 0; j < k; j++)
			{
				tmp[i*k+j] = t[i*k+order[j]];
			}
		}
		int cnt = 1;
		for (int i = 1; i < tmp.length(); i++)
		{
			if (tmp[i] != tmp[i-1])
				cnt++;
		}

		if (cnt < ans)
			ans = cnt;


		return;

			

	}
	for (int i = 0; i < k; i++)
		if (vis[i] == 0)
		{
			vis[i] = 1;
			order[dep] = i;
			calc(dep+1);
			vis[i] = 0;
		}
}
  
int main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		cin >> k;
		cin >> t;
		ans = 100000;
		for (int j = 0; j < k; j++)
			vis[j] = 0;

		calc(0);

		cout << "Case #" << i+1 << ": " << ans << endl;


	}
}
