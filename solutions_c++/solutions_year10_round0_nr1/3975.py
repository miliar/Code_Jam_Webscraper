#include <stdio.h>
#include <string.h>

#define N 11
#define K 1001

int ans[N][K];
int status[N][K];
int power[N][K];

#define HT_SIZE 101

typedef struct HT
{
	int key1, key2;
	int idx;
	HT *next;
}HT;

HT ht[HT_SIZE];
int insert_count = 0;

int insertht(int key1, int key2, int v)
{
	int key;
	HT *pht;
	key = (key1 * key2) % HT_SIZE;
	pht = ht[key].next;
	while(pht) {
		if(pht->key1 == key1 && pht->key2 == key2) return pht->idx;
		else pht = pht->next;
	}
	insert_count++;
	return -1;
}

void initht()
{
	memset(ht, 0, sizeof(ht));
}

void init()
{
	int i, j;
	memset(status, 0, sizeof(status));//on or off
	memset(ans, 0, sizeof(ans));//true or false
	memset(power, 0, sizeof(power));//power or not
	power[1][0] = 1;
	for(i = 1; i < K; i++) {
		power[1][i] = 1;
		status[1][i] = (1 - status[1][i-1]);
		ans[1][i] = (status[1][i] & power[1][i]);
	}
	for(i = 2; i < N; i++) {
		for(j = 1; j < K; j++) {
			power[i][j] = (power[i-1][j] & status[i-1][j]);
			//if(i == 2) status[i][j] = 
			if(power[i][j-1]) status[i][j] = (1 - status[i][j-1]);
			else status[i][j] = status[i][j-1];
			ans[i][j] = (power[i][j] & status[i][j]);
		}
	}
/*	for(i = 10; i < N; i++) 
	{
		printf("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii = %d\n", i);
		for(j = 0; j < K; j++) {
			printf("%d\n", ans[i][j]);
		}
		printf("----------------------------------\n");
	}*/
}
int main()
{
	int t;
	int i;
	int n, k;
//	freopen("Download A-small.in","r",stdin);freopen("Download A-small.out3","w",stdout);
	freopen("abig.in","r",stdin);freopen("abig.out","w",stdout);

//	freopen("ans.out","w",stdout);
//	init();
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		scanf("%d %d", &n, &k);
	//	printf("Case #%d: %s\n", i, ans[n][k] ? "ON" : "OFF");
		k %= (1<<n);
		printf("Case #%d: %s\n", i, ( (k + 1>= (1<<n) && ( (k & ( k + 1) ) == 0) )  || n ==1 && k %2 == 1   )? "ON" : "OFF");
	}
	return 0;
}