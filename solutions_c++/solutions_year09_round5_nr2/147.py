#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

#define MOD 10009

int n;
char s[21][55];

int na[21];
int id[21][26];
int fr[21][26];

char x[25];
int d;
int val;

int ix[10];

int cnt[30];

void process(){
	int res = 0;
	int run = 1;

	int i;
	for(i=0;x[i];++i){
		if(x[i]!='+')
			run = (run*cnt[x[i]-'a'])%MOD;
		else{
			res = (res + run)%MOD;
			run = 1;			
		}
	}
	res = (res + run)%MOD;
	val = (val + res)%MOD;
}

void bktk(int m){
	
	if(m==d){
		process();
		return;
	}

	int i,j;
	for(i=0;i<n;++i){
		for(j=0;j<na[i];++j)
			cnt[id[i][j]] += fr[i][j];
		bktk(m+1);
		for(j=0;j<na[i];++j)
			cnt[id[i][j]] -= fr[i][j];

//		for(j=0;j<s[i][j];++j)
//			cnt[s[i][j]-'a']++;
//		bktk(m+1);
//		for(j=0;j<s[i][j];++j)
//			cnt[s[i][j]-'a']--;
	}
}


int main(){
	
	int i,k,j,run;
	int T,N,l;
	scanf("%d",&T);

	for(N=1;N<=T;N++){
		
		scanf("%s%d",x,&k);
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%s",s[i]);
			l = strlen(s[i]);
			sort(s[i],s[i]+l);
			na[i] = 0;
			run = 1;
			for(j=1;j<l;j++){
				if(s[i][j]==s[i][j-1])
					run++;
				else{
					id[i][na[i]] = s[i][j-1]-'a';
					fr[i][na[i]] = run;
					run = 1;
					na[i]++;
				}
			}
			id[i][na[i]] = s[i][j-1]-'a';
			fr[i][na[i]] = run;
			run = 1;
			na[i]++;
		}

		printf("Case #%d:",N);

		for(d=1;d<=k;d++){
			memset(cnt,0,sizeof(cnt));
			val = 0;
			bktk(0);
			printf(" %d",val);
		}
		printf("\n");
	}

	return 0;
}
