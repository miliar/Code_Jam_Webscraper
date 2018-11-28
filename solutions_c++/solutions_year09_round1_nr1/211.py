
#include <cstdio>
#include <cstdlib>
#include <cstring>

#define LEN 60000

int base[100];
int bptr;

bool table[LEN];

bool sx[11][LEN];

bool happy(int x, int b){
	
	int s = 0;
	
	if(x == 1){
		return true;
	}

	if(table[x]){
		return false;
	}

	table[x] = true;

	while(x){
		int t = x%b; 
		x/=b;
		s += t*t;
	}

	if(s == 1){
		return true;
	}else if(table[s]){
		return false;
	}else{
		return happy(s, b);
	}
}

int main(){
	
	int T;
	char buf[1000];

	scanf("%d", &T);
	gets(buf);

	for(int i=2; i<LEN; ++i){
		for(int j=2; j<=10; ++j){
			memset(table, 0, sizeof(table));
			sx[j][i] = happy(i, j);
		}
	}

	for(int testcase=1; testcase <= T ; ++testcase){
		
		gets(buf);
		
		bptr = 0;

		for(char *x=strtok(buf, " "); x !=NULL; x=strtok(NULL, " ")){
			
			int value = atoi(x);

			base[bptr++] = value;	
		}
		
		int ans = -1;

		for(int i=2; i<LEN; ++i){
			int cnt = 0;
			for(int j=0; j<bptr; ++j){
				if(sx[base[j]][i]){
					++cnt;
				}
			}
			if(cnt == bptr){
				ans = i;
				break;
			}
		}

		printf("Case #%d: %d\n", testcase, ans);
	}
	return 0;
}
