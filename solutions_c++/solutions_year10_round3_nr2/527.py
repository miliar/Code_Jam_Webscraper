#include<stdio.h>
#include<string>
#include<vector>

using namespace std;

int cnt;

void process(int l, int p, int c){
	int ans = 0;
	int f = 0;
	//printf("%d %d %d\n", l, p, c);
	for(int i = l * c * c; i < p; i *= (c * c)){
		//printf("%d\n", i);
		f++;
	}
	if(f == 0){
		if(l * c >= p) ans = 0;
		else ans = 1;
	}
	else{
		if(f % 2 == 0) ans = (f) / 2 + 2;
		else ans = (f + 1) / 2 + 1;
	}
	printf("Case #%d: %d\n", ++cnt, ans);
}

int main(){
	cnt = 0;
	FILE* pFile;
	int T = 0;
	pFile = fopen ("B-small-attempt1.in" , "r");
	fscanf(pFile, "%d\n", &T);
	for(int i = 0; i < T; i++){
		int L, P, C;
		fscanf(pFile, "%d %d %d\n", &L, &P, &C);
		//printf("%d %d %d\n", L, P, C);
		process(L, P, C);
	}
	fclose(pFile);
	getchar();
	return 0;
}
