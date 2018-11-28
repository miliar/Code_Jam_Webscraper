#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
ll vec_x[900], vec_y[900];
void Process(const int &cas)
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		cin >> vec_x[i];
	for (int i = 0; i < n; i++)
		cin >> vec_y[i];
	sort(vec_x, vec_x+n);
	sort(vec_y, vec_y+n);
	ll res = 0ll;
	for (int i = 0; i < n; i++)
		res += vec_x[i] * vec_y[n-i-1];
	cout << "Case #" << cas << ": " << res << endl;
}
int main()
{
	int cas;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++) {
		Process(t);
	}
	return 0;
}
