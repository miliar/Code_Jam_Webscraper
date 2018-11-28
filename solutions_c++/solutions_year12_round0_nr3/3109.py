#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

int A, B;
int PowTen[10];
int ret ;
void add(int &n) {
	
}
bool hash[2000009];
int main() {
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	int T;
	PowTen[0] = 1;
	for(int i = 1; i < 10; ++ i) {
		PowTen[i] = PowTen[i - 1] * 10;
	}
	scanf("%d", &T);
	for(int cas = 1;cas <= T; ++ cas) {
		scanf("%d%d", &A, &B);
		ret = 0;
		int t, Cnt;
		for( int i = A; i < B; ++ i) {
			t = i; Cnt= 0;
			while(t) {
				++ Cnt;
				t /= 10;
			}
			memset( hash, false, sizeof(hash));
			for(int j = 0; j < Cnt; ++ j) {
				int tmp = i % PowTen[j + 1] * PowTen[Cnt - j - 1]
						+ i / PowTen[j + 1]
						;
				if(tmp <= B && tmp > i && !hash[tmp]) {
						int tt = 0;
						int l = tmp;
						while(tmp)  {++ tt; tmp/=10;}
						if(tt == Cnt){
							++ ret;
							hash[l] = true;
						}
				}
			}
		}
		printf("Case #%d: %d\n", cas, ret);
	}
	return 0;
}
