#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++){
		printf("Case #%d: ",test);
		int n, p[2]={1,1}, t[2]={0,0};
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			char s[5];
			int b;
			scanf("%s%d",s,&b);
			int k = s[0]=='O'?0:1;
			int tt = t[k]+abs(b-p[k])+1;
			p[k] = b;
			t[k] = tt<=t[!k]?t[!k]+1:tt;
		}
		printf("%d\n", max(t[0],t[1]));
	}
}
