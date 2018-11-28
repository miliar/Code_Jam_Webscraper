#include <cstdio>

using namespace std;

inline int cod(int ch) {
  return ch -'a';
}

struct nodo{
  nodo *hs[26];
};

struct list{
  nodo *r;
  list *sig;
};

bool find(list **LST, int x) {
  list *L=*LST, *Nu=0, *aux;
  bool ret = true;

  while( L ) {
    if( L->r->hs[cod(x)] != 0 ) {
      aux = Nu;
      Nu = new list();
      Nu->r = L->r->hs[cod(x)];
      Nu->sig = aux;

      ret = false;
    }

    aux = L;
    L = L->sig;
    delete aux;
  }

  *LST = Nu;
  return ret;
}

void find(list *LST, int x, int *mt) {
  list *L = LST;
  while( L ) {
    if( L->r->hs[cod(x)] )
      *mt = *mt +1;
    L = L->sig;
  }

  for(L=LST; L;) {
    list *aux = L;
    delete aux;
    L=L->sig;
  }
}

bool find(list **LST, int *pos, int vtrue) {
  list *L=*LST, *Nu=0, *aux;
  bool ret = true;

  while( L ) {
    for(int i=0; i<26; i++) {
      if( pos[i] == vtrue ) {
	if( L->r->hs[i] != 0 ) {
	  aux = Nu;
	  Nu = new list();
	  Nu->r = L->r->hs[i];
	  Nu->sig = aux;
	  
	  ret = false;
	}
      }
    }

    aux = L;
    L = L->sig;
    delete aux;
  }

  *LST = Nu;
  return ret;
}

void find(list *LST, int *pos, int vtrue, int *mt) {
  list *L = LST;
  while( L ) {
    for(int i=0; i<26; i++) {
      if( pos[i] == vtrue ) {
	if( L->r->hs[i] != 0 )
	  *mt = *mt + 1;
      }
    }
    L = L->sig;
  }

  for(L=LST; L;) {
    list *aux = L;
    delete aux;
    L=L->sig;
  }
}


int main() {
  int L, D, N, ch, sig=1;
  nodo arbol[5000*15]; //Maximo 5000 palabras de longitud 15

  scanf("%d %d %d", &L, &D, &N);
  getchar();

  //Inicializamos el arbol
  for(int i=0; i<D*L; i++) {
    for(int j=0; j<26; j++)
      arbol[i].hs[j] = 0;
  }

  for(int i=0; i<D; i++) {
    nodo *nd=&arbol[0]; //raiz
    for(int l=0; l<L; l++) {
      ch = getchar();

      if( nd->hs[cod(ch)] == 0 ) {
	nd->hs[cod(ch)] = &arbol[sig];
	nd = &arbol[sig];
	sig++;
      }
      else
	nd = nd->hs[cod(ch)];
    }
    getchar(); //Fin de linea
  }

  int pos[26], vtrue=-1;
  for(int i=0; i<26; i++)
    pos[i] = -1;

  for(int ncase=1; ncase<=N; ncase++) {
    int match=0;
    list *lista=new list();

    lista->r = &arbol[0];
    lista->sig = 0;

    for(int l=1; l<=L; l++) {
      ch = getchar();
      vtrue++;
      if( ch == '(' ) {
	ch = getchar();
	while( ch != ')' ) {
	  pos[cod(ch)] = vtrue;
	  ch = getchar();
	}

	if( l==L ) {
	  find(lista, pos, vtrue, &match);
	}
	else {
	  if( find(&lista, pos, vtrue) ) {
	    //Leer hasta fin linea
	    while( ch != '\n' && ch != EOF)
	      ch = getchar();
	    break;
	  }
	}
      }
      else {
	if( l==L ) {
	  find(lista, ch, &match);
	}
	else {
	  if( find(&lista, ch) ) {
	    //Leer hasta fin linea
	    while( ch != '\n' && ch != EOF)
	      ch = getchar();
	    break;
	  }
	}
      }
    }
    if( ch != '\n' )
      getchar(); //Fin de linea

    printf("Case #%d: %d\n", ncase, match);
  }

  return 0;
}
