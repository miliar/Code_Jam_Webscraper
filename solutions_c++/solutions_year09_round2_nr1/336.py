#include <cstdio>
#include <cstdlib>
#include <set>
#include <string>

using namespace std;

typedef struct arv * Arv;
struct arv {
  double w;
  char nome[20];
  Arv esq;
  Arv dir;
};

struct arv buf[10000];
int alocado;

Arv leArv(){
  char c = '\0';
  double weight;
  Arv r = &buf[alocado++];
  
  while (c != '(')
    c = getchar();

  scanf("%lf", &weight);
  
  r->w = weight;
  r->nome[0] = '\0';
  r->esq = NULL;
  r->dir = NULL;

  c = getchar();
  while (c == ' ' || c == '\n') c = getchar();
  if (c == ')') return r;
  ungetc(c,stdin);

  scanf("%s", (r->nome));

  r->esq = leArv();
  r->dir = leArv();
  
  while (c != ')') c = getchar();

  //printf("%lf %s\n", r->w, r->nome);
  return r;
}

int main(){
  int n, l, a;
  set <string> atrib;

  scanf("%d", &n);

  for (int ka = 1; ka <= n; ka++){
      printf("Case #%d:\n", ka);
    scanf("%d", &l);
    alocado = 0;
    Arv r = leArv();

    scanf("%d", &a);
    for (int i = 0; i < a; i++){
      char nome[30];
      char carac[30];
      int t;
      atrib.clear();
      scanf("%s", nome);
      scanf("%d", &t);
      for (int j = 0; j < t; j++){
	scanf("%s", carac);
	atrib.insert(carac);
      }

      Arv r2 = r;
      double prob = r2->w;
      while (r2->esq != NULL){
	if (atrib.count(r2->nome) > 0){
	  r2 = r2->esq;
	  prob *= r2->w;
	}
	else{
	  r2 = r2->dir;
	  prob *= r2->w;
	}
      }
      printf("%lf\n", prob);
    }
  }

  return 0;
}
