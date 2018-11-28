#include <iostream>

using namespace std;

int a[1005];
int used[1005];

int main()
{
  freopen("d.in", "r", stdin);
  freopen("d.out", "w", stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
		int n;
		cin >> n;
		for (int i = 1; i <= n; i++)
		{
			cin >> a[i];
			used[i] = 0;
		}
		int z = 0;
		for (int i = 1; i <= n; i++)
		{
			int x = 0;
			for (int j = i; !used[j]; j = a[j]) 
			{
				used[j] = 1;
				x++;
			}
			if (x > 1)
				z += x;
		}
		cout << z;
    cout << endl;
  }
  return 0;
}