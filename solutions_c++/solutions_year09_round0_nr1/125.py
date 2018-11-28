#include<string>
#include<algorithm>
#include<memory>
#include<string>
using namespace std;
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)
#define cs c_str()
#define sz size()
int L,D,N;

string word[5100];
int chk[512][26], n;
int doit(string x) {
	int ans = 0;
	
	memset(chk, 0, sizeof (chk));
	n = 0;
	FOR(i,0,x.sz) {
		if(x[i]=='(') {
			FOR(j,i+1,x.sz) {
				if(x[j]==')') {
				   i = j;
			   	   break;
				}
				chk[n][x[j]-'a'] = 1;
			}
			n++;
		}
		else {
			chk[n][x[i] - 'a'] = 1;
			n++;
		}
	}	

	FOR(i,0,D) {
		// for each word, check if it can be interpreted as x

		if(word[i].sz != n) continue;
		bool nope = false;
		FOR(j,0,n) {
			if(!chk[j][word[i][j] - 'a']) {
				nope = true;
			}
		}
		if(!nope)
			ans++;
	}

	return ans;
}

int main() {
	freopen("A.in","r",stdin);
	scanf("%d%d%d",&L,&D,&N);
	FOR(i,0,D) {
		char buff[1024];
		scanf("%s",buff);	
		word[i] = buff;
	}
	int e = 0;
	FOR(i,0,N) {
		char buff[1024];
		scanf("%s",&buff);
		int ans = 0;
		ans = doit(buff);
		printf("Case #%d: %d\n", ++e, ans);
	}
	return 0;
}
