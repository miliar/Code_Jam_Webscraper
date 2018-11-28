#include <cstdio>
#include <algorithm>

using namespace std;

int vus[10];

int resoud(){
	int A,B;
	scanf("%d%d",&A,&B);
	int nbChiffres=0,puiss=1,total=0;
	for (int tmp=A;tmp>0;nbChiffres++) tmp/=10,puiss*=10;
	for (int i=A;i<=B;i++){
		int bas=0,haut=i,p=1,mul=puiss;
		for (int j=0;j<nbChiffres;j++){
			bas+=(haut%10)*p;
			haut/=10;
			p*=10;
			mul/=10;
			int v=mul*bas+haut;
			bool vu=false;
			for (int k=0;k<j;k++) vu=vu || vus[k]==v;
//			if (i<v && v<=B && vu) printf("%d %d\n",i,v);
			total+=(i<v && v<=B && !vu ? 1 : 0);
			vus[j]=v;
		}
	}
	return total;
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
		printf("Case #%d: %d\n",i+1,resoud());
	return 0;
}
