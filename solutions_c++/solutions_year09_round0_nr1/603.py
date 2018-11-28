#include <cstdio>
#include <string>
#include <cstring>

#include <vector>

using namespace std;

#define REP(i,n) for (int i=0;i<n;i++)

string word[5000];
char buf[1024*1024];
int mark[15][26];


int main()
{
	int l, d, n;
	scanf("%d %d %d", &l, &d, &n);
	REP(i,d) { scanf("%s", buf); word[i]=buf; }
	REP(i,n) { 
		scanf("%s", buf);

		int wc=0;
		int blen = strlen(buf);

		REP(i,l) REP(j,26) mark[i][j]=0;

		REP(j,l) {
			if ( buf[wc]=='(' ) {
				wc++;
				while (buf[wc]!=')' )
				{
					char c = buf[wc];
					mark[j][c-'a']=1;
					wc++;
				}
				wc++;
			}
			else {
				char c = buf[wc++];
				mark[j][c-'a']=1;
			}
		}
		int succ=0;
		REP(j,d)
		{
			bool fail=false;
			REP(k,l)
			{
				int c = word[j][k]-'a';
				if (mark[k][c]==0) {
					fail=true;
					break;
				}
			}
			if (!fail) succ++;
		}
		printf("Case #%d: %d\n", i+1, succ);
	}
	return 0;
}