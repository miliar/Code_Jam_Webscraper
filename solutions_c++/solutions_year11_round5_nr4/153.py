#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
#include<cmath>
using namespace std;

int tc;
char b[155],tb[155];

int main() {
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		scanf("%s",b);
		int len=strlen(b);
		int q=0;
		for (int i=0; i<len; i++) {
			if (b[i]=='?') q++;
			tb[i]=b[i];
		}
		tb[len]=0;
		long long now=0,ti;
		for (int i=0; i<(1<<q); i++) {
			int ind=0;
			now=0;
			for (int j=0; j<len; j++) {
				now*=2;
				if (b[j]=='1') now++;
				if (b[j]=='?') {
					if (i & (1<<ind)) { now++; tb[j]='1'; }
					else tb[j]='0';
					ind++;
				}
				
			}
			//for (int j=0; j<len; j++) printf("%c",tb[j]);
			//printf("  %lld\n",now);
			ti=(long long)sqrt(now);
			for (long long j=ti-10; j<=ti+10; j++)
				if (j*j==now) {
					//printf("%lld %lld\n",j,now);
					goto bye;
				}
			
		}
		bye:
		printf("Case #%d: ",T);
		for (int i=0; i<len; i++) printf("%c",tb[i]);
		printf("\n");
	}
}
