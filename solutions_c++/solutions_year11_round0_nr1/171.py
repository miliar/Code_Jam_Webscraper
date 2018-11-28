#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<map>
#include<iostream>
using namespace std;

int tc;
int st1,st2,c[105],n,at1,at2;
char s[105][3];

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		scanf("%d",&n);
		st1=0; st2=0; at1=1; at2=1;
		for (int i=0; i<n; i++) {
			scanf("%s%d",s[i],&c[i]);
			if (s[i][0]=='O') {
				st1+=abs(at1-c[i])+1;
				at1=c[i];
				st1=max(st1,st2+1);
			}
			else {
				st2+=abs(at2-c[i])+1;
				at2=c[i];
				st2=max(st1+1,st2);
			}
		}
		printf("Case #%d: %d\n",T,max(st1,st2));
	}
}
