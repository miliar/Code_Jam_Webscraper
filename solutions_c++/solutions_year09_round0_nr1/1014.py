#include<stdio.h>
#include<string.h>

int l, d, nrs, n, i, j, test, dim, cnt[20][30];
char sir[100000];

struct trie{
	trie *fiu[30];

	trie(){
		memset(fiu, 0, sizeof(fiu));
	}
};
trie *q = new trie;

void bag(trie *q, int lng){
	if (lng == l + 1)
		return ;

	int nxt = sir[lng] - 'a' + 1;
	if (!q -> fiu[nxt])
		q -> fiu[nxt] = new trie;

	bag(q -> fiu[nxt], lng+1);
}
int calc(trie *q, int lng, int prd){
	if (lng == l){
		if (!cnt[lng][prd])
			return 0;
		return 1;
	}

	if (!cnt[lng][prd])
		return 0;
	int cate = 0;
	for (int i = 1; i <= 26; i ++)
		if ((q -> fiu[i]) != 0)
			cate += calc(q -> fiu[i], lng + 1, i);

	return cate;
}

int main()
{
	freopen("ab.in", "rt", stdin);
	freopen("ab.out", "wt", stdout);

	scanf("%d%d%d\n", &l, &d, &nrs);
	for (i = 1; i <= d; i ++){
		scanf("%s\n", sir+1);

		bag(q, 1);
	}

	for (test = 1; test <= nrs; test ++){
		scanf("%s\n", sir+1);
		n = strlen(sir+1);

		dim = 1; memset(cnt, 0, sizeof(cnt));
		for (i = 1; i <= n;)
			if (sir[i] != '('){
				cnt[dim][ sir[i] - 'a' + 1] = 1;
				i ++; dim ++;
			}
			else{
				for (j = i+1; sir[j] != ')'; j ++)
					cnt[dim][ sir[j] - 'a' + 1] = 1;
				i = j+1; dim ++;
			}

		cnt[0][0] = 1;
		printf("Case #%d: ", test);
		printf("%d\n", calc(q, 0, 0));
	}

	return 0;
}

