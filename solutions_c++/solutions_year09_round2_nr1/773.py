#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
using namespace std;

typedef struct No no;
struct No{
	no * sim;
	no * nao;
	double peso;
	char c[1000];
};


struct StrCmp : public std::binary_function<char*, char*, bool>
{
bool operator()(char* x, char* y)
{
return strcmp(x, y) < 0;
}
};

set<char *,StrCmp> con;
char s[1000];
char s2[1000][1000];
int ind;
double peso;

void ler(no *ptr);

void percorre(no * ptr)
{
	peso *= ptr->peso;
	if(ptr->sim!=NULL && ptr->nao != NULL){
		if(con.find(ptr->c) != con.end()){
			percorre(ptr->sim);
		}else{
			percorre(ptr->nao);
		}
	}
}

int l;

int main()
{
	
	no raiz;
	int n, cases = 1, t;
	char * aux;
	
	raiz.sim = NULL;
	raiz.nao = NULL;	
	raiz.peso = 0.0;
	
	scanf("%d ",&n);
	while(n--){
		
		scanf("%d ",&l);
		ler(&raiz);
		aux = s;
		while(l>0){			
			aux = gets(aux);
			l--;
		}
		scanf("%d ",&l);
		
		printf("Case #%d:\n",cases++);
		while(l--){
			scanf("%s ",s);
			scanf("%d ",&t);
			con.clear();
			while(t--){
				scanf("%s ",s2[t]);
				con.insert(s2[t]);
			}
			peso = 1.0;
			percorre(&raiz);
			
			printf("%.7lf\n",peso);
		}
		
		
	}
	
	
	return 0;
}




void ler(no *ptr)
{
	char c;
	double d;
	
	if(l<0) return;
	
	c = getchar();
	INICIO:
	while(c!='(' && c!=')') c = getchar();
	if(c==')') { l--; if(l>0) {c = getchar(); goto INICIO;}else {return;} }
	
	scanf("%lf ",&d);
	scanf("%s ",s);
	l--;
	if(s[0] ==')'){
		ptr->sim = NULL;
		ptr->nao = NULL;
		ptr->peso = d;
		ptr->c[0] = '\0';
	}else{
		ptr->sim = (no*)malloc(sizeof(no));
		ptr->nao = (no*)malloc(sizeof(no));
		ptr->peso = d;
		strcpy(ptr->c, s);
		ler(ptr->sim);
		ler(ptr->nao);
	}
}
























