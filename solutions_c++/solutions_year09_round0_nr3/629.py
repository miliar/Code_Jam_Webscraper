#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for (int i=0;i<n;i++)

char buf[1024];

int getint()
{
	fgets(buf, 1024, stdin);
	int num;
	sscanf(buf, "%d", &num);
	return num;
}

const char* wel = "welcome to code jam";
int t[19][500];

int main()
{
	int tlen = strlen(wel);
	int n = getint();
	REP(tcase,n) {
		fgets(buf, 1024, stdin);
		int qlen = strlen(buf);

		REP(i,qlen)
			if ( buf[i]==wel[0] )
				t[0][i]=1;
			else
				t[0][i]=0;

		for (int i=1;i<tlen;i++) {
			REP(j,qlen) {
				if ( buf[j]!= wel[i] ) {
					t[i][j]=0; continue;
				}

				int sum=0;
				REP(k,j)
					sum = (sum+t[i-1][k])%10000;

				t[i][j]=sum;
			}
		}
		
		int tsum=0;
		REP(i,qlen) tsum=(tsum+t[tlen-1][i])%10000;
		printf("Case #%d: %04d\n", tcase+1, tsum);
	}
	return 0;
}
