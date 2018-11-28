#include<stdio.h>
#include<string.h>
#define Max 0x7fffffff
#define Min 0x80000000
#define PName "q1"
#define Maxn 100
#define Maxq 1000
#define Maxl 100

void init(void);
void process(void);
void out(void);

FILE *in = fopen(PName".in" , "r");
FILE *op = fopen(PName".out" , "w");
int check[Maxn + 1];
char Name[Maxn + 1][Maxl + 1];
char tmp[Maxl + 1];
int query[Maxq + 1];
int Dy[Maxq + 1][Maxn + 1];
int ans;
int n;
int q;

int main(void){
	int T , i;
	fscanf(in , "%d" , &T);
	for(i=1; i<=T; i++){
		init();
		process();
		fprintf(op , "Case #%d: " , i);
		out();
	}
	fclose(in);
	fclose(op);
	return 0;
}

int find(char t[Maxl + 1]){
	int i;
	for(i=1; i<=n; i++){
		if(strcmp(t , Name[i]) == 0) return i;
	}
	return -1;
}

void trim(char t[Maxl + 1]){
	if(t[strlen(t) - 1] == '\n') t[strlen(t) - 1] = 0;
}

void init(void){
	int i;
	fscanf(in , "%d\n" , &n);
	for(i=1; i<=n; i++){
		fgets(Name[i] , Maxl , in);
		trim(Name[i]);
	}
	fscanf(in , "%d\n" , &q);
	for(i=1; i<=q; i++){
		fgets(tmp , Maxl , in);
		trim(tmp);
		query[i] = find(tmp);
	}
}

void process(void){
	int i , j = 0 , k;
	ans=0;
	memset(check , 0 , sizeof(check));
	memset(Dy , 0 , sizeof(Dy));
	for(i=1; i<=q; i++){
		if(check[query[i]] == ans){
			j++;
			check[query[i]]++;
			if(j == n){
				ans++;
				j=1;
				check[query[i]]++;
			}
		}
	}
	Dy[1][query[1]] = Max;
	int sw;
	for(i=2; i<=q; i++){
		for(j=1; j<=n; j++){
			Dy[i][j] = Max;
			if(query[i] == j) continue;
			for(k=1; k<=n; k++){
				if(j == k){
					sw = 0;
				} else{
					sw = 1;
				}
				if(Dy[i - 1][k] == Max) continue;
				if(Dy[i][j] > Dy[i - 1][k] + sw){
					Dy[i][j] = Dy[i - 1][k] + sw;
				}
			}
		}
	}
	int ans2 = Max;
	for(i=1; i<=n; i++){
		if(Dy[q][i] < ans2){
			ans2 = Dy[q][i];
		}
	}
	if(ans != ans2){
		printf("shit!!\n");
	}
}

void out(void){
	fprintf(op , "%d\n" , ans);
}