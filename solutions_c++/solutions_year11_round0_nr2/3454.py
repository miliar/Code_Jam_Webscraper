#include<iostream>
using namespace std;

#define CLR(a, b) (memset(a, b, sizeof(a)))

char cmb[30][30];
char inc[40][5];
char buf[110], res[110];
int nres;
bool mp1[30][30], mp2[30][30];
bool chk[110];

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int cas, c, d, n;
	scanf("%d", &cas);
	for(int t = 0; t < cas; t++){
		scanf("%d", &c);
		CLR(mp1, 0); CLR(mp2, 0); CLR(chk, 0);
		for(int j = 0; j < c; j++){
			scanf("%s", inc[j]);
			mp1[inc[j][0] - 'A'][inc[j][1] - 'A'] = 1;
			mp1[inc[j][1] - 'A'][inc[j][0] - 'A'] = 1;
			cmb[inc[j][0] - 'A'][inc[j][1] - 'A'] = inc[j][2];
			cmb[inc[j][1] - 'A'][inc[j][0] - 'A'] = inc[j][2];
		}
		scanf("%d", &d);
		for(int j = 0; j < d; j++){
			scanf("%s", inc[j]);
			mp2[inc[j][0] - 'A'][inc[j][1] - 'A'] = 1;
			mp2[inc[j][1] - 'A'][inc[j][0] - 'A'] = 1;
		}
		scanf("%d", &n);
		scanf("%s", buf);
		for(int i = 1; i < n; i++){
			int tpp = i - 1;
			while(tpp >= 0 && chk[tpp]) tpp--;
			if(tpp >= 0 && mp1[buf[i] - 'A'][buf[tpp] - 'A']){
				chk[tpp] = 1; buf[i] = cmb[buf[i] - 'A'][buf[tpp] - 'A'];
			}
			else{
				int p;
				for(p = 0; p < i; p++){
					if(!chk[p] && mp2[buf[i] - 'A'][buf[p] - 'A'])
						break;
				}
				if(p != i){
					for(p = 0; p <= i; p++)
						chk[p] = 1;
				}
			}
		}
		printf("Case #%d: [", t + 1);
		nres = 0;
		for(int i = 0; i < n; i++){
			if(!chk[i]) res[nres++] = buf[i];
		}
		for(int i = 0; i < nres; i++){
			if(i) printf(", ");
			printf("%c", res[i]);
		}
		printf("]\n");
	}
	return 0;
}