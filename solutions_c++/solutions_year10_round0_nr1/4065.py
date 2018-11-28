#include <stdio.h>
#include <iostream>

using namespace std;

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int test_count;
	cin >> test_count;

for (int test = 0; test < test_count ; test++)
{
	int n, k;
	cin >> n >> k;

	int c = 0;
	while (k & 1) {
		c++;
		k >>= 1;
	}

	printf("Case #%d: ", test + 1);
	cout << ((c >= n) ? "ON" : "OFF");
	cout << endl;
}

}