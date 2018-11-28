#define MD(x) if (0) {x;}
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <string>
#include <sstream>
void MyAssert(int p){while (!p) printf("elfjdskf\n");}
using namespace std;
const int maxN = 110000;
int p[11][maxN];

int solve(int b, int x){
	int y = x;
//	MD(cout<<x<<" "<<p[b][x]<<endl;)
	MyAssert(x<maxN);
	if (p[b][x]!=-1){
		if (p[b][x]==true) return true;
		else return false;
	}
	p[b][x] = -2;

	int t = 0;
	while (x>0){
		int d = x%b;
		t += d*d;
		x /= b;
	}
	if (t==1){
		return p[b][y] = true;		
	}
	else{
		return p[b][y] = solve(b,t);		
	}	
}

bool ok(int n, int b[], int x){
	for (int i=0; i<n; i++)
		if (p[b[i]][x]==false) return false;
	return true;
}


int main(){
	memset(p,-1,sizeof(p));
	for (int i=2; i<=10; i++)
		for (int x=4; x<maxN; x++)
			solve(i,x);
	int tc;
	scanf("%d\n",&tc);
	for (int ti=1; ti<=tc; ti++){
		int b[20], n = 0;
		string s;
		getline(cin,s);
		MD(cout<<"s:"<<s<<endl;)
		istringstream in(s);
		while (in>>b[n]) n++;
		MD(cout<<"b:";for (int i=0; i<n; i++)cout<<b[i]<<" ";cout<<endl;)
		
		int ans = 2;
		for (; ans<maxN; ans++)
			if (ok(n,b,ans)) break;

		MyAssert(ans<maxN);
		printf("Case #%d: %d\n",ti,ans);
		
	}
	return 0;
}
