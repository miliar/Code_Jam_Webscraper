#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

void resoud(){
	int N;
	scanf("%d",&N);
	int nbFixe=0;
	for (int i=1;i<=N;i++){
		int v;
		scanf("%d",&v);
		nbFixe+=(v==i ? 1 : 0);
	}
	printf("%d",N-nbFixe);
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		resoud();
		puts("");
	}
	return 0;
}
