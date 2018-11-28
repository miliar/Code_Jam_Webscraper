#include<iostream>
#include<cstdio>
#include<map>
#define db(a) \
cout << #a << " = " << a << endl
#define db2(a, b) \
cout << #a << " = " << a << " " << #b << " = " << b << endl
#define inf (1<<30)
#define foreach(it, m) \
for (typeof(m.begin()) it = m.begin(); it != m.end(); it++)
using namespace std;
int main() {
	freopen("in.in", "r", stdin);
	freopen("ou.out", "w", stdout);
	string m = "yhesocvxduiglbkrztnwjpfmaq", a;
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; i++) {
		getline(cin, a);
		printf("Case #%d: ", i + 1);
		for (int j = 0; j < a.size(); j++) {
			if (a[j] == 32) printf(" ");
			else printf("%c", m[a[j] - 'a']);
		}
		puts("");
	}
	return 0;
}
