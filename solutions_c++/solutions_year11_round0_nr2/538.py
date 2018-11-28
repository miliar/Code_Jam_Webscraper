// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
char comb[8][8];
char opos[8][8];
char *chars="QWERASDF";
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
int abs(int x) {
if(x<0) return -x;
return x;
}

int max(int a,int b) {
	if(a>b) return a;
	return b;
}
int ppp(char c) {
REP(i,8) if(chars[i]==c) return i;

return -1;
}
int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	scanf("%d ",&T);
	
	REP(xx,T) {
		//printf("%d\n",xx);
		string s;
		REP(i,8) REP(j,8) {
			comb[i][j]=0;
			opos[i][j]=0;
		}
		int n;
		scanf("%d",&n);
		static char p[1000];
		REP(i,n) {
			scanf("%s",p);
			int a=ppp(p[0]);
			int b=  ppp(p[1]);
			comb[a][b]=p[2];
			comb[b][a]=p[2];
		}
		scanf("%d",&n);
		REP(i,n)  {
			scanf("%s",p);
			int a = ppp(p[0]);
			int b = ppp(p[1]);
			opos[a][b]=1;
			opos[b][a]=1;
		}
		int cnt[8]={0,0,0,0,0,0,0,0};
		scanf("%d",&n);
		scanf("%s",p);
		REP(i,n)  {
			int m=s.size();
			int a=ppp(p[i]);
           // printf("%c\n",p[i]);
			if(m>0) {
				//combine
				int b=ppp(s[m-1]);
				if(b!=-1 && comb[a][b]) {
					s[m-1]=comb[a][b];
					cnt[b]--;
					//printf("comb\n");
					continue;
				}
				//opose
				int clear=0;
				REP(j,8) {
					if(opos[a][j] && cnt[j]>0) clear=1;
				}
				if(clear) {
					REP(j,8) cnt[j]=0;
					s.resize(0);
					//printf("clear\n");
					continue;
				}
				//printf("add\n");

			}
			s.push_back(p[i]);
			cnt[a]++;
		}



		
		
		printf("Case #%d: [",xx+1);
		REP(i,s.size()) {
			if(i) printf(", ");
			printf("%c",s[i]);
		}
		printf("]\n");
	}
	return 0;
}

