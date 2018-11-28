#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

#define ln printf("\n")
#define rep(a,b) for(int a = 0; a < b; a++)

using namespace std;

int d[111111];
int l[111111];

int n;
int end;

bool read(){
	scanf("%d", &n);
	
	rep(i,n){
		scanf("%d%d", &d[i], &l[i]);
	}
	scanf("%d", &end);
}

int cn = 1;
int f[111111];

void process(){
	printf("Case #%d: ", cn++);
	
	memset(f, 0, sizeof f);
	f[0] = d[0];
	bool possible = false;
	rep(i,n){
		for(int j = i+1; j < n; j++){
			if(d[j] > d[i] + f[i]) break;
			f[j] = max(f[j], d[j]-d[i]);
			f[j] = min(f[j], l[j]);
		}
		if(d[i] + f[i] >= end) possible = true;
	}
	
	
	
	if(!possible)printf("NO\n");
	else printf("YES\n");
}

int main(){
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t = -1;
	scanf("%d", &t);
	while(t-- && read()) process();
	
	//while(1);
	return 0;
}
