#include <vector>
#include <string>
#include <iostream>
using namespace std;
template <class T> void out(T A[], int n) {for (int i = 0; i<n; i++) cout << A[i] << ' '; cout << endl;}  

int ts, no;
int n, ans;
vector<int> a;

void get() 
{
	char ch;
	int ret = 0;
	for (int i=0; i<n; i++)
	{
		while (1)
		{
			cin >> ch;
			if (ch == '0' || ch == '1')
			{
				break;
			}
		}
		if (ch == '1')
		{
			ret = i;
		}
	}
	a.push_back(ret);
}

main() {
	freopen("a1.in", "r", stdin);
	freopen("1.out", "w", stdout);

	cin >> ts;
	for (int no=0; no<ts; no++) {
		cout << "Case #" << no+1 << ": ";
		cin >> n;
		a.clear();
		for (int i=0; i<n; i++)
		{
			get();
		}
		ans = 0;
		for (int i=0; i<n; i++)
		{
			int j;
			for (j=0; ; j++)
			{
				if (a[j] <= i)
				{
					break;
				}
			}
			ans += j;
			int k = a.size();
			for (; j<k-1; j++)
			{
				swap(a[j], a[j+1]);
			}
			a.pop_back();
		}
		cout << ans << endl;
	}
}
