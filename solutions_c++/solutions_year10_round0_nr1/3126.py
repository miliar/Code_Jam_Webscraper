#include<stdio.h>
#include<string>
#include<vector>

using namespace std;

int cnt;

void process(int n, int k){
	int lim = (1 << (n));
	int state = k % lim;
	if(state == lim - 1) printf("Case #%d: ON\n", ++cnt);
	else printf("Case #%d: OFF\n", ++cnt);
}

int main(){
	cnt = 0;
	FILE* pFile;
	char buffer [100];
	int T = 0;
	pFile = fopen ("A-large.in" , "r");
	for(int i = 0; !feof(pFile); i++){
		fgets(buffer, 100, pFile);
		if(i == 0) {
			sscanf(buffer, "%d\n", &T);
			continue;
		}
		int n = -1, k = -1;
		sscanf(buffer, "%d %d\n", &n, &k);
		process(n, k);
	}	
	fclose (pFile);
	//if(cnt != T) printf("error\n");
	getchar();
	return 0;
}
