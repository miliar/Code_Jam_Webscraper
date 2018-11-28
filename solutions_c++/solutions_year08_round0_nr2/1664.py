#include<cstdio>
#define tm 10000005
#define DISP 0
#define VA 1
struct estado{
	int hora, pasa,donde;
};

bool operator<(const estado &a, const estado &b){
	if(a.hora==b.hora)
		return a.pasa<b.pasa;
	return a.hora<b.hora;
}

estado monticulo[tm];
int indice=1;

void metele(estado x){
	estado aux;
	int act=indice, papa;
	monticulo[indice++]=x;
	papa = (act>>1);
	while(papa > 0 && monticulo[act] < monticulo[papa])
	{
		aux = monticulo[act];
		monticulo[act] = monticulo[papa];
		monticulo[papa] = aux;
		act = papa;
		papa = (act>>1);
	}
}

estado sacale()
{
	estado ret = monticulo[1], aux;
	int hijo, hijo2, act;
	indice--;
	monticulo[1] = monticulo[indice];
	act = 1;
	hijo = (act << 1);
	hijo2 = hijo + 1;
	if(hijo2 < indice && monticulo[hijo2] < monticulo[hijo])
		hijo = hijo2;
	while(hijo < indice && monticulo[hijo] < monticulo[act])
	{
		aux = monticulo[act];
		monticulo[act] = monticulo[hijo];
		monticulo[hijo] = aux;
		act = hijo;
		hijo = (act << 1);
		hijo2 = hijo + 1;
		if(hijo2 < indice && monticulo[hijo2] < monticulo[hijo])
			hijo = hijo2;		
	}
	return ret;
}


void rollo(int ncaso){
	int vienen,A,B;
	int resA,resB;
	int aHora,aMin, bHora,bMin;
	estado aux;
	//int hora, pasa,donde;
	scanf("%d%d%d",&vienen,&A,&B);
	for(int i=0;i<A;i++){
		scanf("%d:%d %d:%d",&aHora,&aMin,&bHora,&bMin);
		aMin+=aHora*60;
		bMin+=bHora*60;
		aux.hora=aMin;
		aux.pasa=VA;
		aux.donde=0;
		metele(aux);
		//sumar minutos
		aux.hora=bMin+vienen;
		aux.pasa=DISP;
		aux.donde=1;
		metele(aux);
	}
	for(int i=0;i<B;i++){
		scanf("%d:%d %d:%d",&aHora,&aMin,&bHora,&bMin);
		aMin+=aHora*60;
		bMin+=bHora*60;
		aux.hora=aMin;
		aux.pasa=VA;
		aux.donde=1;
		metele(aux);
		//sumar minutos
		aux.hora=bMin+vienen;
		aux.pasa=DISP;
		aux.donde=0;
		metele(aux);
	}
	int cU=0, cD=0;
	resA =0;
	resB =0;
	while(indice > 1)
	{
		aux = sacale();
		if(aux.donde==0){
			if(aux.pasa==DISP)
				cU++;
			else
				if(cU==0)
					resA++;
				else
					cU--;
		}
		else{
			if(aux.pasa==DISP)
				cD++;
			else
				if(cD==0)
					resB++;
				else
					cD--;
		}
	}
	printf("Case #%d: %d %d\n",ncaso,resA,resB);
}

int main(){
	int casos;
	scanf("%d",&casos);
	for(int i=1;i<=casos;i++)
		rollo(i);
	return 0;
}

