#include<stdio.h>
#include<string>
#include<vector>

using namespace std;

int cnt;
vector<int> a, b;

void solve(){
	int ans = 0;
	for(int i = 0; i < a.size(); i++){
		for(int j = 0; j < i; j++){
			//printf("%d %d %d %d\n", a[i], a[j], b[i], b[j]);
			if(a[i] < a[j] && b[i] > b[j]) ans++;
			if(a[i] > a[j] && b[i] < b[j]) ans++;
		}
	}
	printf("Case #%d: %d\n", ++cnt, ans);
}

int main(){
	cnt = 0;
	a.clear(); b.clear();
	FILE* pFile;
	int T = 0;
	pFile = fopen ("A-large(2).in" , "r");
	fscanf(pFile, "%d\n", &T);
	for(int i = 0; i < T; i++){
		int N = 0;
		fscanf(pFile, "%d\n", &N);
		a.clear(); b.clear();
		for(int j = 0; j < N; j++){
			int A, B;
			fscanf(pFile, "%d %d\n", &A, & B);
			a.push_back(A); b.push_back(B);
		}
		solve();
	}
	fclose(pFile);
	getchar();
	return 0;
}
