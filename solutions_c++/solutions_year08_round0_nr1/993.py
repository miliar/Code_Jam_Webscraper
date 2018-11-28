#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()

using namespace std;

int ileTestow, ileWysz, ileZap, w[1000], dp[1000][100];
char t[100][102], tmp[102];

inline bool ok( char s1[], char s2[]){
	for(int a=0; s1[a]!=0 || s2[a]!=0 ; a++) if( s1[a] != s2[a] ) return false;
	return true;
}

int main(){
	
	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		scanf("%d\n",&ileWysz);

		for(int a=0; a<ileWysz; a++){
			char c;
			int i=0;
			while( (c=getchar())!='\n' ) t[a][i++] = c;
			t[a][i]=0;
		}

		scanf("%d\n",&ileZap);
		
		for(int a=0; a<ileZap; a++){
			char c;
			int i=0;
			while( (c=getchar())!='\n' ) tmp[i++] = c;
			tmp[i]=0;

			for(int b=0; b<ileWysz; b++) if( ok(t[b],tmp) ){
				w[a] = b;
				break;
			}
		}

		for(int a=0; a<ileWysz; a++) dp[ileZap-1][a]=1;
		dp[ileZap-1][ w[ileZap-1] ]=0;
		
		for(int a=ileZap-2; a>=0; a--) for(int b=0; b<ileWysz; b++)
			if( w[a] == b ){
				dp[a][b] = 0;
			} else {
				dp[a][b] = dp[a+1][b]+1;	
			}

		int score=-1,gdzie=0,bonus;

		while( gdzie < ileZap ){
			bonus = 0;
			for(int a=0; a<ileWysz; a++) bonus = max(bonus, dp[gdzie][a]);
			gdzie+=bonus;
			score++;
		}

		if( score==-1 ) score=0;

		printf("Case #%d: %d\n",q,score);
		
	}

	return 0;
}
