#include <cstdio>
#include <cstring>

struct nodo{
	bool hay;
	int hijo[26];
};

nodo Dict[6000*15];
int nodos=1;

int nuevo_nodo(){
	Dict[nodos].hay=false;
	memset(Dict[nodos].hijo, -1, sizeof(int)*26);
	return nodos++;
}

void inserta_palabra(char pal[], int a){
	if(pal[0]==0){
		Dict[a].hay=true;
		return;
	}
	if(Dict[a].hijo[pal[0]-'a']==-1){
		Dict[a].hijo[pal[0]-'a']=nuevo_nodo();
	}
	inserta_palabra(pal+1, Dict[a].hijo[pal[0]-'a']);
}

int cuenta(char pal[], int a){
	int r=0;
	if(Dict[a].hay)
		r++;
	if(pal[0]==0)
		return r;
	if(pal[0]=='('){
		int k, i;
		for(k=1; pal[k]!=')'; k++) { }
		for(i=1; i<k; i++){
			if(Dict[a].hijo[pal[i]-'a']!=-1){
				r+=cuenta(pal+k+1, Dict[a].hijo[pal[i]-'a']);
			}
		}
	}else{
		if(Dict[a].hijo[pal[0]-'a']==-1){
			return r;
		}else{
			return cuenta(pal+1, Dict[a].hijo[pal[0]-'a'])+r;
		}
	}
	return r;
}

int L, D, N;
char Pal[1000000];

int main(){
	int raiz=nuevo_nodo();
	int i, k, h;
	scanf("%d %d %d", &L, &D, &N);
	for(i=0;i<D;i++){
		scanf("%s", Pal);
		inserta_palabra(Pal, raiz);
	}
	for(i=1;i<=N;i++){
		scanf("%s", Pal);
		k=cuenta(Pal, raiz);
		printf("Case #%d: %d\n", i, k);
	}
	return 0;
}
