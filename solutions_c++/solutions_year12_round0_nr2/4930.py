#include <cstdio>
#include <cstring>
#define M 111

using namespace std;

int cas,n,s,p,vet[M];

int main(){
	scanf("%d",&cas);
	for ( int c = 1 ; c <= cas ; c++ ){
		printf("Case #%d: ",c);
		scanf("%d%d%d",&n,&s,&p);
		int teste=0;
		for ( int i = 0 ; i < n ; i++ ){
			scanf("%d",&vet[i]);
			int calc=vet[i]/3;
			int calc2=vet[i]%3;
			if ( calc2 == 0 && calc >= p ) teste++;
			else if ( calc2 == 0 && s > 0 && calc+1 >= p && vet[i] >= 3 ){
				teste++;
				s--;
			}			
			else if ( calc2 == 1 && calc+calc2 >= p ) teste++;
			else if ( calc2 == 2 ){
				if ( calc+calc2 > p ){
					teste++;
				}else if ( calc+calc2 == p && s > 0 ){
					teste++;
					s--;
				}
			}
		}
		printf("%d\n",teste);
	}
	return 0;
}
// 5 5 5 -> Se for divis�vel por 3 posso tranformar em um best result se necess�rio (4,5,6) !
// 5 5 6 -> Se obtiver resto 1 tbm posso transformar (4,6,6) ! OBS : n�o aumenta o valor, logo n�o importa
// 5 5 7 -> Posso tentar fazer n�o ser best result se for necess�rio pra mim (5,6,6)!