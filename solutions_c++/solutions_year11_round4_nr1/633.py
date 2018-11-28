#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN=1000;
const int MAXL=1000*1000+1;

pair<int,int> extremites[2*MAXN+2];
int vitesses[MAXL+1];

void resoud(){
	int L,W,R,T,N;
	scanf("%d%d%d%d%d",&L,&W,&R,&T,&N);
	for (int i=0;i<N;i++){
		scanf("%d%d%d",&extremites[2*i].first,&extremites[2*i+1].first,&extremites[2*i].second);
		extremites[2*i+1].second=-extremites[2*i].second;
	}
	extremites[2*N]=make_pair(L,-1);
	sort(extremites,extremites+2*N+1);
	int vitesse=0,ancPos=0;
	for (int i=0;i<2*N+2;i++){
		for (int j=ancPos;j<min(L,extremites[i].first);j++)
			vitesses[j]=vitesse;
//		printf("va en %d, vitesse %d : %f (%f)\n",extremites[i].first,vitesse,nouv,temps);
		if (extremites[i].first==L)
			break;
		ancPos=extremites[i].first;
		vitesse+=extremites[i].second;
	}
	sort(vitesses,vitesses+L);
	double temps=0;
	bool cours=true;
	for (int i=0;i<L;i++){
//		printf("%d,%f\n",vitesses[i],temps);
		if (cours){
			double l=min(1.,(vitesses[i]+R)*(T-temps));
			temps+=l/(vitesses[i]+R);
			temps+=(1.-l)/(vitesses[i]+W);
			cours=l==1.;
//			printf("l=%f\n",l);
		}
		else {
			temps+=1./(vitesses[i]+W);
		}
	}
	printf("%.9f",temps);
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
