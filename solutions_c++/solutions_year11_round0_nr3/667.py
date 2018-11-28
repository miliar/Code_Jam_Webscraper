#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

void resoud(){
	int N,somme=0,mini=1e9,xorsomme=0;
	scanf("%d",&N);
	for (int i=0;i<N;i++){
		int v;
		scanf("%d",&v);
		somme+=v;
		xorsomme^=v;
		mini=min(mini,v);
	}
	if (xorsomme)
		printf("NO");
	else
		printf("%d",somme-mini);
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
