#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

vector<char> lst;

char merge[256][256];
char destroy[256][256];

void reset() {
	lst.clear();
	lst.reserve(100);
	memset(merge, 0, sizeof(merge));
	memset(destroy, 0, sizeof(destroy));
}

void getmerge() {
	char a,b,c;
	scanf (" %c %c %c", &a, &b, &c);
	merge[a][b] = merge[b][a] = c;
}

void getdestroy() {
	char a,b;
	scanf (" %c %c", &a, &b);
	destroy[a][b] = destroy[b][a] = 1;
}

void getnext() {
	char a;
	scanf (" %c", &a);
	while(!lst.empty() && merge[lst.back()][a]) {
		a = merge[lst.back()][a];
		lst.pop_back();
	}
	for(int i=0;i<lst.size();i++) if (destroy[a][lst[i]]) {
		lst.clear();
		return;
	}
	lst.push_back(a);
}

void printlist() {
	putchar('[');
	for(int i=0;i<lst.size();i++) {
		putchar(lst[i]);
		if (i!=(int)lst.size()-1) {
			fputs(", ", stdout);
		}
	}
	putchar(']');
}

int main() {
	int t,n,c,d;
	scanf("%d", &t);
	for (int ca=0;ca<t;ca++) {
		reset();
		scanf("%d", &c);
		for(int i=0;i<c;i++) {
			getmerge();
		}
		scanf("%d", &d);
		for(int i=0;i<d;i++) {
			getdestroy();
		}
		scanf("%d", &n);
		for (int i=0;i<n;i++) {
			getnext();
		}
		printf("Case #%d: ",ca+1);
		printlist();
		putchar('\n');
	}
	return 0;
}
