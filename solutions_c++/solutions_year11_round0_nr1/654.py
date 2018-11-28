#include <iostream>
using namespace std;

const int maxn = 110;

int n, pos[maxn];
char c[maxn];

int main() {
	int t, tt;
	cin >> t;
	for (tt = 0; tt < t; tt++) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> c[i] >> pos[i];
		}

		int pos1 = 1, pos2 = 1;
		int ptr1 = 0, ptr2 = 0;
		int tot = 0;

		while (ptr1 < n) {
			if (c[ptr1] == 'O')
				break;
			ptr1++;						
		}

		while (ptr2 < n) {
			if (c[ptr2] == 'B')
				break;
			ptr2++;						
		}

		while (ptr1 < n || ptr2 < n) {
			tot++;
			bool pr = false;
			if (ptr1 < n) {
				if (pos1 < pos[ptr1])
					pos1++;
				else if (pos1 > pos[ptr1])
					pos1--;
				else {
					// check i can press the buttom
					if (ptr1 < ptr2) {
						ptr1++;
						while (ptr1 < n) {
							if (c[ptr1] == 'O')
								break;
							ptr1++;						
						}
						pr = true;
					}
				}
			}

			if (ptr2 < n) {
				if (pos2 < pos[ptr2])
					pos2++;
				else if (pos2 > pos[ptr2])
					pos2--;
				else {
					// check i can press the buttom
					if (ptr2 < ptr1) {
						if (pr)
							continue;
						ptr2++;
						while (ptr2 < n) {
							if (c[ptr2] == 'B')
								break;
							ptr2++;
						}
					}
				}
			}
		}
				
		printf("Case #%d: %d\n", tt + 1, tot);
	}
}
