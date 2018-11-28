#include <cstdio>
#include <algorithm>

using namespace std;

int resoud(){
	int N,nbModif,but,reste;
	scanf("%d%d%d",&N,&nbModif,&but);
	int total=0;
	reste=nbModif;
	for (int i=0;i<N;i++){
		int v;
		scanf("%d",&v);
		if ((v+2)/3>=but)
			total++;
		else if (reste && v>=2 && v<=28){
			if (v%3==0 && v/3==but-1) reste--;
			if (v%3==2 && v/3==but-2) reste--;
		}
	}
	return total+nbModif-reste;
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
		printf("Case #%d: %d\n",i+1,resoud());
	return 0;
}
