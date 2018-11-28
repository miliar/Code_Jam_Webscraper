#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

string ans;
char sc[10];

int C, D, N;
int com[300][300], at[300][300];
char inp[300];

int top;
char st[300];

void init() {
	scanf("%d", &C);
	memset(com, 0, sizeof(com));
	memset(at, 0, sizeof(at));
	for (int i=1;i<=C;i++) {
		scanf("%s", sc);
		com[sc[0]][sc[1]] = sc[2];
		com[sc[1]][sc[0]] = sc[2];
	}
	scanf("%d", &D);
	for (int i=1;i<=D;i++) {
		scanf("%s", sc);
		at[sc[0]][sc[1]] = at[sc[1]][sc[0]] = 1;
	}
	scanf("%d", &N);
	scanf("%s", inp);
}

void work() {
	top = 0;
	for (int i=0;i<N;i++) {
		char x = inp[i];
		st[++top] = x;
		while (top>=2 && com[st[top]][st[top-1]]>0) {
			st[top-1] = com[st[top]][st[top-1]];
			top --;
		}
		for (int i=1;i<top;i++)
			if (at[st[i]][st[top]] == 1) {
			    top = 0;
			    break;
			}
	}
	cout<<"[";
	for (int i=1;i<=top;i++) {
		if (i>1) cout<<", ";
		cout<<st[i];
	}
	cout<<"]";
	cout<<endl;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++) {
		init();
		cout<<"Case #"<<ti<<": ";
		work();
	}
	return 0;
}
