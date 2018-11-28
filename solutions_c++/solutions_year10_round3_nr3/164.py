#include <stdio.h>
#include <string.h>

#include <algorithm>

using namespace std;

#define MAX 512
#define P 12345678987654321LL

typedef long long i64;

char bark[MAX][MAX];

int cnt[MAX];

i64 hashes[MAX][MAX];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;++i) {
			char row[MAX/4+1];
			scanf("%s",&row);
			for(int j=0;j<m;++j) {
				char c=row[j>>2];
				int x;
				if(c>='0' && c<='9')
					x=c-'0';
				else
					x=10+c-'A';
				bark[i][j]=((x>>(3-(j&3)))&1)+1;
			}
		}
		memset(cnt,0,sizeof(cnt));
		int ans=0;
		for(int s=min(m,n);s>0;--s) {
			i64 p=1;
			for(int i=0;i<s;++i)
				p*=P;
			// Cut out all s-size chess boards
			for(int i=0;i<=n-s;++i) {
				// Calc hashes
				for(int k=0;k<s;++k) {
					i64 hash=0;
					for(int j=0;j<m;++j) {
						hash=hash*P+bark[i+k][j];
						hashes[k][j]=hash;
					}
				}
				i64 etalon[2];
				etalon[0]=etalon[1]=0;
				for(int k=0;k<s;++k) {
					etalon[0]=etalon[0]*P+(1+(k&1));
					etalon[1]=etalon[1]*P+(2-(k&1));
				}
				for(int j=0;j<=m-s;++j) {
					if(bark[i][j]>2) continue;
					// Check
					int corner=bark[i][j]-1;
					bool ok=true;
					for(int k=0;k<s;++k) {
						i64 hash=hashes[k][j+s-1];
						if(j) hash-=hashes[k][j-1]*p;
						if(hash!=etalon[(k+corner)&1]) {
							ok=false;
							break;
						}
					}
					if(ok) {
						// Cut out
						for(int k=0;k<s;++k)
							for(int l=0;l<s;++l)
								bark[i+k][j+l]=3;
						if(!cnt[s]) ++ans;
						++cnt[s];
					}
				}
			}
		}
		printf("Case #%d: %d\n",test,ans);
		for(int s=min(n,m);s>0;--s)
			if(cnt[s])
				printf("%d %d\n",s,cnt[s]);
	}
	return 0;
}
