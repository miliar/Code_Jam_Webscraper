#include <cstdio>
#include <cassert>
#define MAXN 1000
#include <iostream>
using namespace std;
#include <string>
#include <vector>
#include <algorithm>

string read(){
	string tmp = "";
	char c;
	scanf("%c", &c);
	while (c=='\n') scanf("%c", &c);
	while (c!='\n'){tmp.push_back(c);if (scanf("%c", &c)==EOF) break;}
//	cout<<tmp<<endl;
	return tmp;
}

vector<string> a;
int rez[MAXN];

int main(){
	freopen("universe.in", "rt", stdin);
	freopen("universe.out", "wt", stdout);
	int t;
	scanf("%d\n", &t);
	for (int w = 0; w < t; w++){
		int n,m;
		scanf("%d\n", &n);
		a.clear();
		while (n--) a.push_back(read());
		n = a.size();
		for (int i = 0; i < n; i++) rez[i] = 0;
		sort(a.begin(),a.end());
		scanf("%d", &m);
		while (m--){
			string qqq = read();
			int tmp = lower_bound(a.begin(),a.end(),qqq)-a.begin();
			assert(a[tmp]==qqq);
			rez[tmp] = 1000000000;
			for (int i = 0; i < n; i++) if (rez[tmp]>rez[i]+1) rez[tmp]=rez[i]+1;
		}
		int tmp = rez[0];
		for (int i = 0; i < n; i++) if (tmp>rez[i]) tmp = rez[i];
		printf("Case #%d: %d\n", w+1,tmp);
	}
	fclose(stdin);
	fclose(stdout);
}
