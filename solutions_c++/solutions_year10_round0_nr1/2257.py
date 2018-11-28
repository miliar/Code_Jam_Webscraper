#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

int mat[40];
void init(){
	memset(mat, 0, sizeof(mat));
	mat[1] = 1;
	for(int i = 2; i <= 31; ++i){
		int sum = 0;
		for(int j = 1; j < i; ++j)
			sum += mat[j];
		mat[i] = sum+1;
	}
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, n, k;
	init();
//	scanf("%d", &T);
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
	//	scanf("%d %d", &n,&k);
		cin>>n>>k;
		printf("Case #%d: ", tt);
		k = k%mat[n+1];
		if(k == mat[n+1]-1){
			printf("ON\n");
		}else {
			printf("OFF\n");
		}
	}
	return 0;	
}
