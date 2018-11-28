#include <iostream>
#include <cassert>
using namespace std;

bool visited[2000001];
const int n_choose_2[] = {0, 0, 1, 3, 6, 10, 15, 21};

int main()
{
	int T;
	cin >> T;
	getchar();
	for (int i = 1; i <= T; ++i) {
		int A, B;
		cin >> A >> B;
		int power10 = 1;
		while (power10 * 10 <= A) power10 *= 10;
		for (int j = A; j <= B; ++j) visited[j] = false;
		int result = 0, group_size = 0;
		for (int j = A; j <= B; ++j) {
			if (visited[j]) continue;
			int curr = j;
			group_size = 0;
			do {
				if (A <= curr && curr <= B) {
					group_size++;
					visited[curr] = true;
				}
				int leading_digit = curr / power10;
				curr %= power10;
				curr *= 10;
				curr += leading_digit;
			} while (curr != j);
			assert(group_size <= 7);
			result += n_choose_2[group_size];
			//if (group_size > 1) {
			//	cout << "j = " << j << endl;
			//	cout << "group_size = " << group_size << endl;
			//	cout << "result = " << result << endl;
			//}
		}
		cout << "Case #" << i << ": " << result << endl;
	}

	return 0;
}
