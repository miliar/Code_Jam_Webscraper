#include <iostream>
#include <cstdio>
#include <algorithm>
#include <memory.h>
using namespace std;

int k;
char buf[2000];
int ar[256][256];
int s[256];
int res[256];
int in[256];

void solve(){
	scanf("%d\n", &k);
	gets(buf);
	memset(ar, 0, sizeof(ar));
	memset(in, 0, sizeof(in));
	memset(s, 0, sizeof(s));
	for (int i=1; buf[i]; ++i){
		ar[buf[i-1]][buf[i]]=1;
		ar[res[buf[i-1]]][buf[i]]=1;
		ar[res[buf[i-1]]][res[buf[i]]]=1;
		ar[buf[i-1]][res[buf[i]]]=1;
	}
	int os=0;
	int n=0;
	for (int i=1; i<256; ++i){
		for (int j=1; j<256; ++j)
			s[i]+=ar[i][j], os+=ar[i][j], in[j]+=ar[i][j];
	}
	for (int i=1; i<256; ++i)
		n+=max(0, s[i]-in[i]);
	cout<<os+max(1, n);
	cout<<endl;
}

int main(){
	res['o']='0';
	res['i']='1';
	res['e']='3';
	res['a']='4';
	res['s']='5';
	res['t']='7';
	res['b']='8';
	res['g']='9';
	freopen("input (2).txt", "r", stdin);
	freopen("output.txt","w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i=0; i<t; ++i){
		cout<<"Case #"<<i+1<<": ";
		solve();
	}
}