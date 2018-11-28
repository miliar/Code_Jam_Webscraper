#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
const int LAST = 10000;

using namespace std;

int nrT;
vector<string> colors;
unsigned short best[10100], old1[10100], old2[10100];
int st[500], fn[500], n, N;
unsigned fnOk[500], stOk[500];
string cul[500], sng[500];

void solve(){
	printf("Case #%d: ", ++nrT);
	scanf("%d\n", &n);
	char str[500];
	for (int i=0; i<n; i++){
		scanf("%s %d %d\n", str, st+i, fn+i);
		cul[i] = str;
	}
	for (int i=0; i<n; i++)
		for (int j=i+1; j<n; j++)
			if (cul[i] > cul[j]){
				swap(cul[i], cul[j]);
				swap(st[i], st[j]);
				swap(fn[i], fn[j]);
			}
	for (int i=0; i<n; i++)
		if (cul[i]!= cul[i+1])
			sng[N++] = cul[i];
	int bestSol = LAST;
/*
	for (int a=0; a<N; a++){
		memset(best, 0x3f, sizeof(best));
		best[0] = 0;
		for (int i=0; i<n; i++)
			if (cul[i]==sng[a])
				for (int k=st[i]; k<=fn[i]; k++)
					if (best[st[i]-1]+1 < best[k])
						best[k] = best[st[i]-1]+1;
		if (best[LAST] < bestSol) bestSol = best[LAST];
		memcpy(old1, best, sizeof(best));
		for (int b=a+1; b<N; b++){
			memcpy(best, old1, sizeof(best));
			for (int i=0; i<n; i++)
				if (cul[i]==sng[b])
					for (int k=st[i]; k<=fn[i]; k++)
						if (best[st[i]-1]+1 < best[k])
							best[k] = best[st[i]-1]+1;
			if (best[LAST] < bestSol) bestSol = best[LAST];
			memcpy(old2, best, sizeof(best));
			for (int c=b+1; c<N; c++){
				memcpy(best, old2, sizeof(best));
				for (int i=0; i<n; i++)
					if (cul[i]==sng[c])
					for (int k=st[i]; k<=fn[i]; k++)
						if (best[st[i]-1]+1 < best[k])
							best[k] = best[st[i]-1]+1;
					if (best[LAST] < bestSol) bestSol = best[LAST];
			}
		}
	}
*/
	for (int a=0; a<N; a++)
		for (int b=a; b<N; b++)
			for (int c=b; c<N; c++){
				int nr = 0;
				bool bun = false;
				for (int i=0; i<n; i++)
					if (cul[i] == sng[a] || cul[i] == sng[b] || cul[i] == sng[c]){
						stOk[nr] = st[i];
						fnOk[nr++] = fn[i];
						if (fn[i] == LAST) bun = true;
				}
				if (!bun) continue;
				memset(best, 0x3f, sizeof(best));
				best[0] = 0;
				for (int i=0; i<nr; i++)
					for (int j=i+1; j<nr; j++)
						if (stOk[i] > stOk[j])
							swap(stOk[i], stOk[j]), swap(fnOk[i], fnOk[j]);
				for (int i=0; i<nr; i++)
					for (unsigned k=stOk[i]; k<=fnOk[i]; k++)
						if (best[stOk[i]-1]+1 < best[k])
							best[k] = best[stOk[i]-1]+1;
				if (best[LAST] < bestSol) bestSol = best[LAST];
			}
	if (bestSol == LAST)	printf("IMPOSSIBLE\n");
	else printf("%d\n", bestSol);
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int tst;
	scanf("%d", &tst);
	while (tst--){
		solve();
		fprintf(stderr, "%d\n", tst);
	}
    return 0;
}
