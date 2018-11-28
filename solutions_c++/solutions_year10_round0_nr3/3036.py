#include<stdio.h>
#include<string>
#include<vector>

using namespace std;

int cnt;
int grp[1001];

void process(int r, int k, int n){
	int sol = 0, front = 0;
	for(int l = 0; l < r; l++){
		int st = k;
		int i;
		for(i = front; st >= 0;){
			if(st >= grp[i]){
				st -= grp[i];
			}else break;
			i = (i + 1) % n;
			if(i == front) break;
		}
		front = i;
		sol += k - st;
	}
	printf("Case #%d: %d\n", ++cnt, sol);
}

int main(){
	cnt = 0;
	FILE* pFile;
	char buffer [100];
	int T = 0, flag = 1;
	pFile = fopen ("C-small-attempt1.in" , "r");
	while(!feof(pFile)){
		fgets(buffer, 100, pFile);
		if(flag) {
			sscanf(buffer, "%d\n", &T);
			flag = 0;
			continue;
		}
		int r = -1, k = -1, n = -1;
		sscanf(buffer, "%d %d %d\n", &r, &k, &n);
		memset(grp, 0, sizeof(grp));
		for(int i = 0; i < n; i++){
			fscanf(pFile, "%d ", &grp[i]);
		}
		process(r, k, n);
	}	
	fclose(pFile);
	getchar();
	return 0;
}
