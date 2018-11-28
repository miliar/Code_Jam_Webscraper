#include <iostream>
using namespace std;

int main (int argc, char * const argv[]) {
	int t=0, T;
	scanf("%d",&T);//cin >>T;
	while(t<T){
		t++;
		cout << "Case #" << t << ": ";
		char D[101][12];
		char P[100];
		char L[27];
		char e[100][100];
		int n=0,m=0,N, M;
		scanf("%d %d",&N, &M);
		while(n<N){
			scanf("%s",D[n]);
			D[n][11]=strlen(D[n]);
			n++;
		}

		while(m<M){
			m++;
			memset(e,0,100*100);
			memset(P,0,100);
			for(int i=0;i<N;i++){
				for(int j=0;j<N;j++){
					if(i==j) e[i][j]=1;
					if(D[i][11]!=D[j][11]) e[i][j]=1;
				}
			}
			scanf("%s",L);
			for(int y=0;y<26;y++){ //letra dicha
				for(int i=0;i<N;i++){ //palabra elegida
					bool tiene=false;
					for(int k=0;k<D[i][11];k++){ //letra de la palabra
						if(D[i][k]==L[y]){
							tiene=true;
							break;
						}
					}
					if(tiene){
						for(int j=0;j<N;j++){ //palabra a comparar
							if(!e[i][j]){
								for(int k=0;k<D[i][11];k++){ //letra de la palabra
									if(D[i][k]==L[y] && D[j][k]!=L[y]){
										e[i][j]=1;
										goto a;
									}else{
										if(D[j][k]==L[y] && D[i][k]!=L[y]){
											e[i][j]=1;
											goto a;
										}
									}
								}
							}
							a: continue;
						}
					}else{
						for(int j=0;j<N;j++){ //palabra a comparar
							if(!e[i][j]){
								for(int k=0;k<D[i][11];k++){ //letra de la palabra
									if(D[j][k]==L[y]){
										tiene=true;
										e[i][j]=1;
										continue;
									}
								}
							}
						}
						if(tiene){
							P[i]++;
						}
					}
				}
			}
			int mejor, mp;
			mp=-1;
			for(int i=0;i<N;i++){
				if(mp<P[i]){
					mejor=i;
					mp=P[i];
				}
			}
			if(m>1) cout << " ";
			cout << D[mejor];
			if(m==M) cout << endl;
		}

	}

	return 0;
}
