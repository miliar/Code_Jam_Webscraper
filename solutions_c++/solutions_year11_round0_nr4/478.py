#include <iostream>
#include <algorithm>

struct Tdata {
	int value;
	int pos;
} data[1100];

bool compare(const Tdata &a,const Tdata &b) 
{
	if (a.value < b.value) return true; else return false;
}

int main()
{
    //freopen("a.txt", "r", stdin);
	//freopen("b.txt", "w", stdout);

	int t, n;

	std::cin >> t;
	for (int i = 0; i < t; i++) {
		std::cin >> n;
		for (int j = 0; j < n; j++) {
			std::cin >> data[j].value;
			data[j].pos = j;
		}
		std::sort(data, data + n, compare);
		double res = 0;
		for (int j = 0; j < n; j++) {
			int length = 1;
			int p = data[j].pos;
			while (p != j) {
				length ++;
				p = data[p].pos;
			}
			if (length != 1) res += 1;
		}
		printf("Case #%d: %0.6lf\n", i + 1, res);
	}
	return 0;
}