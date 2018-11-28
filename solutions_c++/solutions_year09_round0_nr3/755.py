#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <functional>
#include <algorithm>
#include <string>
#include <vector>


using namespace std;

#define LMAX 555
#define MOD 10000
const char PAT[] = "welcome to code jam";
const int Plen = 19;
//const char PAT[] = "www";
//const int Plen = 3;
int T[2][Plen]={{0}};
// int T[LMAX][Plen]; // T[i][j] = ile dopasowañ w ci¹gu 1..i (lub krótszym) mamy wzorca 1..j 
char buf[LMAX]={0};

int main() {
	int N; scanf("%i ", &N);

	// CASES
	for(int icase=1; icase<=N; ++icase) {
		// INIT, IN
		buf[0]=0;
		fgets(buf, LMAX, stdin);
		int Tlen = strlen(buf);
		while(Tlen>0 && isspace(buf[Tlen-1])) { buf[--Tlen]=0; }
		memset(T,0,sizeof(T));
		int cur=0;

		// SOLVE
		for(int i=0; i<Tlen; ++i) {
			cur = 1-cur;
			for(int j=0; j<Plen; ++j) {
				T[cur][j] = T[1-cur][j];
				if(PAT[j]==buf[i]) {
					if(j>0)
						T[cur][j] = (T[cur][j]+T[1-cur][j-1])%MOD;
					else
						T[cur][j] = (T[cur][j]+1)%MOD;
				}
			}
		}

		printf("Case #%i: %04d\n", icase, T[cur][Plen-1]);

	}

	return 0;
}

/*
3
elcomew elcome to code jam
wweellccoommee to code qps jam
welcome to codejam

---

Case #1: 0001
Case #2: 0256
Case #3: 0000


*/



