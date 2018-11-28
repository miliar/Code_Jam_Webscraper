#include <cstdio>
#include <cstdlib>
#include <algorithm>
#define AND 1
#define OR 0
#define MAXM 20000

using namespace std;

typedef struct {int val;int type;int akhir;int change;} card;

int want;
int type;
int dp[2][MAXM * 2];
bool sudah[2][MAXM * 2];
card gate[MAXM * 2];
int n;
int a,b,c,d,e;
int jmlcase;

inline int lc(int abc) {
	return abc * 2;
	}

inline int rc(int abc) {
	return abc * 2 + 1;
	}

inline int pa(int abc) {
	return abc / 2;
	}

int getit(int value,int posisi) {
	//printf("%d %d\n",value,posisi);
	//printf("%d %d : %d\n",value,posisi,dp[value][posisi]);
	if (gate[posisi].akhir) return dp[value][posisi];
	if (sudah[value][posisi]) return dp[value][posisi];
	sudah[value][posisi] = 1;
	//this is and
	int aa;
	for (aa = 0;aa < 2;aa++) {
	int tambah = 0;
	if (gate[posisi].type == aa) tambah = 1;
	if (tambah == 0 || gate[posisi].change) {
		if (value == (aa + 1) % 2) {
			tambah += getit((aa + 1) % 2,lc(posisi));
			tambah += getit((aa + 1) % 2,rc(posisi));
		//	printf("asd %d %d %d %d\n",posisi,gate[posisi].type,(aa + 1) % 2,lc(posisi));
		//	printf("tambah = %d\n",tambah);
			dp[value][posisi] = min(dp[value][posisi],tambah);
			}
		if (value == aa) {
			//one of them must be false
			
			dp[value][posisi] = min(dp[value][posisi],tambah + getit((aa + 1) % 2,lc(posisi)) + getit(aa,rc(posisi)));
			dp[value][posisi] = min(dp[value][posisi],tambah + getit(aa,lc(posisi)) + getit(aa,rc(posisi)));
			dp[value][posisi] = min(dp[value][posisi],tambah + getit(aa,lc(posisi)) + getit((aa + 1) % 2,rc(posisi)));
			}
		}
	}
//	printf("%d %d : %d\n",value,posisi,dp[value][posisi]);
	return dp[value][posisi];
	}


int main() {
	scanf("%d",&jmlcase);
	for (e = 0;e < jmlcase;e++) {
	memset(sudah,0,sizeof(sudah));
	printf("Case #%d: ",e + 1);
	scanf("%d%d",&n,&want);
	//printf("%d %d\n",n,want);
	for (a = 1;a <= (n - 1) / 2;a++) {
		scanf("%d%d",&b,&c);
		gate[a].type = b;
		gate[a].change = c;
		gate[a].akhir = 0;
		}
	
	for (a = 0;a < MAXM;a++) {
		for (b = 0;b < 2;b++) {
			dp[b][a] = 9999999;
			}
		}
	
	for (a = 1;a <= (n + 1) / 2;a++) {
		b = a + (n - 1) / 2;
		gate[b].akhir = 1;
		//printf("b %d\n",b);
		scanf("%d",&(gate[b].val));
		dp[gate[b].val][b] = 0;
		}
	
	int xxx = getit(want,1);
	if (xxx > 100500) {
		printf("IMPOSSIBLE\n");
		}
	else printf("%d\n",xxx);
	}
	
	
	return 0;
	}

