#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN=200;

int position[MAXN],nombre[MAXN];


void resoud(){
	int N,L;
	scanf("%d%d",&N,&L);
	for (int i=0;i<N;i++)
		scanf("%d%d",&position[i],&nombre[i]);
	double debut=0,fin=1e8;
	while (debut+1e-7<fin){
		double temps=(debut+fin)/2;
		double anc=-1e9;
		bool possible=true;
		for (int i=0;i<N;i++)
			for (int j=0;j<nombre[i];j++){
				anc=max(position[i]-temps,anc+L);
				if (anc>position[i]+temps)
					possible=false;
			}
		if (possible)
			fin=temps;
		else
			debut=temps;
	}
	printf("%.7f",debut);
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
