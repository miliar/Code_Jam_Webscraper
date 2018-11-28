#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN=1000;

int taille[MAXN];
int R,k,N;
long long personne;
int premiere[MAXN],argentDebut[MAXN];

int next(int i){
	int nbPlaces=k;
	personne=0;
	for (int j=i;;j++){
		nbPlaces-=taille[j%N];
		if (nbPlaces<0 || j==i+N)
			return j%N;
		personne+=taille[j%N];
	}
}

long long resoud(){
	scanf("%d%d%d",&R,&k,&N);
	for (int i=0;i<N;i++)
		scanf("%d",&taille[i]);
	int debut=0,periode=0;
	long long argent=0;
	fill(premiere,premiere+N,0);
	while(1){
		debut=next(debut);
		argent+=personne;
		periode++;
//		printf("%d %d %lld\n",debut,periode,argent);
		if (periode==R)
			return argent;
		if (premiere[debut]!=0)
			break;
		premiere[debut]=periode;
		argentDebut[debut]=argent;
	}
//	printf("periode : %d [%lld] %lld\n",periode-premiere[debut],argent-argentDebut[debut],argent);
	argent+=((R-premiere[debut])/(periode-premiere[debut])-1)*(argent-argentDebut[debut]);
//	printf("%lld\n",argent);
	R=(R-premiere[debut])%(periode-premiere[debut]);
	for (int i=0;i<R;i++){
		debut=next(debut);
		argent+=personne;
	}
	return argent;
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: %lld\n",i+1,resoud());
	}
	return 0;
}
