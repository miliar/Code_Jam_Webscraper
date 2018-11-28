#include <iostream>
#include <list>

using namespace std;

struct trip{
	int ini;
	int fim;
	int usado;
};
int compare (const void * a, const void * b)
{
  return ( (*(trip*)a).ini - (*(trip*)b).ini);
}
int N,NA,NB,T,h,m,X;
trip listA[101];
trip listB[101];

int procurarEmA(int atual){
	//procurar em A
	for(int j=0;j<NA;j++){
		if(listA[j].usado==0 && (listB[atual].fim+T)<=listA[j].ini){
			//cout << "b " << atual <<" " << listB[atual].ini/60 << ":" << listB[atual].ini%60 << " " << listB[atual].fim/60 << ":" << listB[atual].fim%60 << " encaixa em a " << j <<" " << listA[j].ini/60 << ":"  << listA[j].ini%60 << " " << listA[j].fim/60 << ":"  << listA[j].fim%60 << endl;
			listA[j].usado=1;
			return j;
		}
	}
	return -1;
}
int procurarEmB(int atual){
	//procurar em B
	for(int j=0;j<NB;j++){
		if(listB[j].usado==0 && (listA[atual].fim+T)<=listB[j].ini){
			//cout << "a " << atual <<" " << listA[atual].ini/60 << ":" << listA[atual].ini%60 << " " << listA[atual].fim/60 << ":" << listA[atual].fim%60 << " encaixa em b " << j <<" " << listB[j].ini/60 << ":"  << listB[j].ini%60 << " " << listB[j].fim/60 <<":"<< listB[j].fim%60 << endl;
			listB[j].usado=1;
			return j;
		}
	}
	return -1;
}

int main(){
	X=0;
	
	scanf("%d",&N);
	for(int i=0;i<N;i++){
		scanf("%d",&T);
		scanf("%d %d",&NA,&NB);
		
		char dots;
		for(int j=0;j<NA;j++){
			scanf("%d%c%d",&h,&dots,&m);
			trip aux;
			aux.ini=(h*60)+m;
			scanf("%d%c%d",&h,&dots,&m);
			aux.fim=(h*60)+m;
			aux.usado=0;
			listA[j]=aux;
		}
		
		qsort (listA, NA, sizeof(trip), compare);
		/*
		printf("NA:\n");
		for(int j=0;j<NA;j++){
			printf("    %2d:%2d ",listA[j].ini/60,listA[j].ini%60);
			printf("    %2d:%2d\n",listA[j].fim/60,listA[j].fim%60);
		}//*/
		for(int j=0;j<NB;j++){
			scanf("%d%c%d",&h,&dots,&m);
			trip aux;
			aux.ini=(h*60)+m;
			scanf("%d%c%d",&h,&dots,&m);
			aux.fim=(h*60)+m;
			aux.usado=0;
			listB[j]=aux;

		}
		qsort (listB, NB, sizeof(trip), compare);
		/*
		printf("NB:\n");
		for(int j=0;j<NB;j++){
			printf("    %2d:%2d ",listB[j].ini/60,listB[j].ini%60);
			printf("    %2d:%2d\n",listB[j].fim/60,listB[j].fim%60);
		}//*/

		int atual=0;
		int ta=0,tb=0;
		char aoub='b';
		while(42){
			//achar o menor
			int menor=99999999,amenor=-1,bmenor=-1;
			for(int j=0;j<NA;j++){
				//cout << "j=" << j << " usado A = "<< listA[j].usado << endl;
				if(listA[j].usado==0 && listA[j].fim<menor){
					menor=listA[j].fim;
					amenor=j;
					//cout << "menor = " << menor << endl;
					break;
				}
			}
			for(int j=0;j<NB;j++){
				if(listB[j].usado==0 && listB[j].fim<menor){
					menor=listB[j].fim;
					bmenor=j;
					break;
				}
			}
			if(amenor==-1 && bmenor!=-1){
				atual=bmenor;
				aoub='b';
			}else if(amenor!=-1 && bmenor==-1){
				atual=amenor;
				aoub='a';
			}else if(bmenor!=-1 && amenor!=-1){
				if(listB[bmenor].fim<listA[amenor].fim){
					atual=bmenor;
					aoub='b';
				}else{
					atual=amenor;
					aoub='a';
				}
			}
			//cout << "menor " << aoub << " " << atual << " " << menor <<  " = " << menor/60 << ":" << menor%60 << endl;
			if(atual==-1) break;
			//o primeiro possível
			if(aoub=='b'){
				listB[atual].usado=1;
			}else{
				listA[atual].usado=1;
				//cout << "a utilizado \n";
			}
			while(atual!=-1){
				if(aoub=='b'){
					//procurar em A
					if(atual!=-1) atual = procurarEmA(atual);
					//procurar em B
					if(atual!=-1) atual = procurarEmB(atual);
				}else{
					//procurar em B
					if(atual!=-1) atual = procurarEmB(atual);
					//procurar em A
					if(atual!=-1) atual = procurarEmA(atual);
				}

			}
			//cout <<"\n";
			if(aoub=='b'){
				tb++;
			}else{
				ta++;
			}
			
		}
		printf("Case #%d: %d %d\n",++X,ta,tb);
	}
	return 0;
}
