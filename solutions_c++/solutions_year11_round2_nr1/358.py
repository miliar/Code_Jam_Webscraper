#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN=100;

char matrice[MAXN][MAXN+1];
int gains[MAXN],totaux[MAXN];
double OWP[MAXN];

void incr(int &gain,int &total,int mul,char c){
	if (c=='0')
		total+=mul;
	else if (c=='1'){
		total+=mul;
		gain+=mul;
	}
}

void resoud(){
	int N;
	scanf("%d",&N);
	for (int y=0;y<N;y++){
		int gain=0,total=0;
		scanf("%s",matrice[y]);
		for (int x=0;x<N;x++)
			incr(gain,total,1,matrice[y][x]);
		gains[y]=gain;
		totaux[y]=total;
	}
	for (int y=0;y<N;y++){
		double owp=0;
		for (int x=0;x<N;x++)
			if (matrice[y][x]!='.'){
				int g=gains[x],t=totaux[x];
				incr(g,t,-1,matrice[y][x]);
				g+=(matrice[y][x]=='0' ?  -1 : 1);
				owp+=g/(double)t;
			}
		OWP[y]=owp/totaux[y];
	}
	for (int y=0;y<N;y++){
		double WP=gains[y]/(double)totaux[y];
		double oowp=0;
		for (int x=0;x<N;x++)
			if (matrice[y][x]!='.')
				oowp+=OWP[x];
		oowp/=totaux[y];
		printf("%.9f\n",.25*WP+.5*OWP[y]+.25*oowp);
	}
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d:\n",i+1);
		resoud();
	}
	return 0;
}
