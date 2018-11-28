#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int maxn=110;

int t, k;
int n, m;
int a[maxn], b[maxn], c[maxn], d[maxn];

void get_time(int &t) {
	string tmp;
	cin>>tmp;
	t=(tmp[0]-'0')*10*60+(tmp[1]-'0')*60+(tmp[3]-'0')*10+(tmp[4]-'0');
}

void getinfo() {
	cin>>k>>n>>m;
	for (int i=0; i<n; i++) {
		get_time(a[i]);
		get_time(b[i]);
	}
	for (int i=0; i<m; i++) {
		get_time(c[i]);
		get_time(d[i]);
	}
}

int get_ans(int a[], int b[], int n, int m) {
	int ans=m;
	sort(a,a+n);
	sort(b,b+m);
	bool e[maxn];
	memset(e,false,sizeof(e));
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			if ((b[j]>=a[i]+k)&&(!e[j])) {
				ans--;
				e[j]=true;
				break;
			}
	return ans;
}

void work() {
	int ansa=get_ans(d,a, m, n);
	int ansb=get_ans(b,c, n, m);
	printf("%d %d\n",ansa,ansb);
}

int main() {
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>t;
	for (int i=0; i<t; i++) {
		printf("Case #%d: ",i+1);
		getinfo();
		work();
	}
	return 0;
}
