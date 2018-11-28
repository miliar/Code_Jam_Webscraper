#include"iostream"
#include"stdio.h"
#include"algorithm"
#include"queue"
#include"string.h"
#include"vector"
#include"stack"
#include"set"
#define N 105
using namespace std;
struct node {

	char name[5];
	int in[2];
} a[N], b[N];
char result[N];
int index;
char s[N];
int c, d, n;
void init() {
	index = 0;
	memset(result, 0, sizeof(result));
}

void update(char temp) {
	for (int j = 0; j < d; ++j) {
		if (b[j].name[0] == temp) {
			b[j].in[0]++;
		} else if (b[j].name[1] == temp) {
			b[j].in[1]++;
		}
	}
}
void change(char temp) {
	for (int j = 0; j < d; ++j) {
		if (b[j].name[0] == temp) {
			b[j].in[0]--;
		} else if (b[j].name[1] == temp) {
			b[j].in[1]--;
		}
	}
}
void solve(int n) {
	for (int i = 0; i < n; ++i) {
		char temp = s[i];
		if (index == 0) {
			result[index++] = temp;
			update(temp);
		} else {
			while (index >= 1) {
				int j;
				for (j = 0; j < c; ++j) {
					if (a[j].name[0] == temp && a[j].name[1] == result[index
							- 1] || a[j].name[1] == temp && a[j].name[0]
							== result[index - 1]) {
						change(result[index - 1]);
						result[--index] = a[j].name[2];
						temp = result[index];
						break;
					}
				}
				if (j == c) {
					result[index] = temp;
					break;
				}
			}
			update(result[index]);
			index++;
		}
		for (int j = 0; j < d; ++j) {
			if (b[j].in[0] && b[j].name[1] == result[index - 1] || b[j].in[1]
					&& b[j].name[0] == result[index - 1]) {
				for (int k = 0; k < c; ++k) {
					a[k].in[0] = a[k].in[1] = 0;
				}
				for (int k = 0; k < d; ++k) {
					b[k].in[0] = b[k].in[1] = 0;
				}
				index = 0;
				break;
			}
		}
		//cout << index << " ";
	}
	//cout << endl;
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; ++i) {
		init();
		scanf("%d", &c);
		for (int j = 0; j < c; ++j) {
			scanf("%s", a[j].name);
			a[j].in[0] = a[j].in[1] = 0;
		}
		scanf("%d", &d);
		for (int j = 0; j < d; ++j) {
			scanf("%s", b[j].name);
			b[j].in[0] = b[j].in[1] = 0;
		}
		scanf("%d", &n);
		scanf("%s", s);
		solve(n);
		printf("Case #%d: [", i + 1);
		for (int j = 0; j < index; ++j) {
			if (j == 0)
				printf("%c", result[j]);
			else
				printf(", %c", result[j]);
		}
		printf("]\n");
	}
	return 0;
}
