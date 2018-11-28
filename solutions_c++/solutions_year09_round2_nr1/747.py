#include <cstdio>
#include <map>
#include <string>

using namespace std;

struct nodo{
  double w;
  char fea[116];
  nodo *hi;
  nodo *hd;
};

nodo *leer_nodo() {
  int ch = getchar();
  nodo *r = 0;

  while( ch != ')' ) {
    if( ch == '(' ) {
      r = new nodo();
      scanf("%lf", &r->w);
      r->hi = r->hd = 0;
    }
    else if( ch >= 'a' && ch <= 'z' ) {
      r->fea[0] = ch;
      int j;
      ch = getchar();
      for(j=1; ch >= 'a' && ch <= 'z'; j++) {
	r->fea[j] = ch;
	ch = getchar();
      }

      r->fea[j] = 0;
      r->hi = leer_nodo();
      r->hd = leer_nodo();
    }
    ch = getchar();
  }

  return r;
}

void borrar_arbol(nodo *r) {
  if( r->hi ) borrar_arbol(r->hi);
  if( r->hd ) borrar_arbol(r->hd);
  delete r;
}

int main() {
  int N, L, A, nf;
  char str[16];
  double P;

  scanf("%d", &N);
  for(int ncases=1; ncases<=N; ncases++) {
    scanf("%d", &L);

    //Leer arbol en L lineas
    nodo *raiz = leer_nodo();

    printf("Case #%d:\n", ncases);

    //Leer animales
    scanf("%d", &A);
    for(int i=0; i<A; i++) {
      scanf("%s", str);
      scanf("%d", &nf);
      map<string,int> tabla;
      for(int j=0; j<nf; j++) {
	scanf("%s", str);
	tabla[str] = 1;
      }

      //Calcular Probabilidad
      P=1.0;
      nodo *r = raiz;
      while( r->hi && r->hd ) {
	P = P*r->w;
	if( tabla[r->fea] )
	  r = r->hi;
	else
	  r = r->hd;
      }
      P = P*r->w;

      printf("%.7f\n", P);
    }

    //Borrar arbol
    borrar_arbol(raiz);
  }

  return 0;
}
