#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>

using namespace std;

const int maxsize=300;
const int maxn=110;
const int maxm=1010;

int t;
int n, m;

string s[maxn];
string q[maxm];

void getinfo() {
	cin>>n;
	char tmp[1000];
	cin.getline(tmp,maxsize);
	for (int i=0; i<n; i++) {
		cin.getline(tmp,maxsize);
		s[i]=tmp;
	}
	cin>>m;
	cin.getline(tmp,maxsize);
	for (int i=0; i<m; i++) {
		cin.getline(tmp,maxsize);
		q[i]=tmp;
	}
}

int go_next(int now, int x) {
	int i=now;
	while (q[i]!=s[x]) {
		i++;
		if (i==m) break;
	}
	return i;
}

void work() {
	int ans=0;
	int now=0;
	while (now!=m) {
		int next=0;
		for (int i=0; i<n; i++) {
			int v=go_next(now,i);
			if (v>next) next=v;
		}
		now=next;
		ans++;
	}
	if (ans>0) printf("%d\n",ans-1); else printf("%d\n",ans);
}

int main() {
	
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>t;
	
	for (int i=0; i<t; i++) {
		printf("Case #%d: ",i+1);
		getinfo();
		work();
	}

	return 0;
}
