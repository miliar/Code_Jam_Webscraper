#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <iostream>
#include <vector>

using namespace std;

#define ll long long
#define ull unsigned long long
#define PB push_back
#define MP make_pair

int O,B,to,tb;
int now,T,n;
char s[10];

int main(){
	scanf("%d",&T);
	
	for (int t=1;t<=T;t++) {
		printf("Case #%d: ",t);
		scanf("%d",&n);
		O=B=1; tb=to=now=0;
		for (int i=1;i<=n;i++) {
			int x; scanf("%s%d",s,&x);
			if (s[0]=='O') {
				now=max(now,to+abs(O-x))+1;
				O=x; to=now;
			}
			else {
				now=max(now,tb+abs(B-x))+1;
				B=x; tb=now;
			}
		}
		
		printf("%d\n",now);
	}

	return 0;
}
