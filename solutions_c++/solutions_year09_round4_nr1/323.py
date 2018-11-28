#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int n;
		vector <int> list;

		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			int pos = -1;
			for (int j = 0; j < n; j++) {
				char c;

				scanf(" %c", &c);

				if (c == '1')
					pos = j;
			}
			list.push_back(pos);	
		}

		int ret = 0;

		for (int i = 0; i < n; i++) {
			int j;
			for (j = i; j < n; j++)
				if (list[j] <= i)
					break;
			for (int k = j; k != i; k--) {
				swap(list[k], list[k-1]);
				ret ++;
			}
		}
		
		printf("Case #%d: %d\n", t+1, ret);
	}

	return 0;
}
