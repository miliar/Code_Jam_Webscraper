#include <iostream>

using namespace std;
int test;

void go()
{
	int n;
	cout << "Case #" << ++test <<": ";
	cin >> n;
	int pos[] = {1, 1};
	int t[] = {0, 0};
	int free = 0, lst = -1;
	int total = 0;
	while (n--)
	{
		char x; int d;
		scanf(" %c %d", &x, &d);
		int idx = 0;
		if (x == 'O') idx = 1;
		int ajuta = 0;
		if (idx != lst) {lst = idx; ajuta = free; free = 0;}
		total += 1 + max(abs(pos[idx] - d) - ajuta, 0);
		free += 1 + max(abs(pos[idx] - d) - ajuta, 0);
		pos[idx] = d;
	}
//	cout << max(t[0], t[1]) << '\n';
	cout << total << '\n';
}
int main()
{
	int t;
	cin >> t;
	while (t--) go();
	return 0;
}
