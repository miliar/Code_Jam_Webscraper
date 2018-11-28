#include <cstdio>
#include <list>
#include <cstring>
#include <iostream>

using namespace std;

struct no {
  char c;
  list<no> prox;
  no(char novo):c(novo) { };
};

list<no> inicio;

int L, D, N, caso=1, tamatual;
long long resultado;
char palavra[2000];

void inserir(int pos, list<no>& atual) {
  if(pos == L) return;
  //list<no>::iterator itant = atual.begin();
  for(list<no>::iterator it = atual.begin(); it != atual.end(); ++it) {
    if(palavra[pos] == it->c) {
      inserir(pos+1, it->prox);
      return;
    } else if(palavra[pos] > it->c) {
      list<no>::iterator novo = atual.insert(it, no(palavra[pos]));
      inserir(pos+1, novo->prox);
      return;
    }
  }
  atual.push_back(no(palavra[pos]));
  inserir(pos+1, atual.back().prox);
}

void procurar(int pos, list<no>& atual) {
  if(pos == tamatual) {
    resultado++;
    return;
  }
  if(palavra[pos] == '(') {
    int fecha = pos + 1;
    for(; palavra[fecha] != ')'; ++fecha);
    for(int posatual = pos+1; posatual < fecha; ++posatual) {
      for(list<no>::iterator it = atual.begin(); it != atual.end(); ++it) {
        if(palavra[posatual] == it->c) {
          procurar(fecha+1, it->prox);
          break;
        } else if(palavra[posatual] > it->c) {
          break;
        }
      }    
    }
  } else {
    for(list<no>::iterator it = atual.begin(); it != atual.end(); ++it) {
      if(palavra[pos] == it->c) {
        procurar(pos+1, it->prox);
        return;
      } else if(palavra[pos] > it->c) {
        return;
      }
    }
  }
}

void atravessar(string str, list<no>& atual) {
  for(list<no>::iterator it = atual.begin(); it != atual.end(); ++it) {
    cout << str << it->c << endl;
    atravessar(str + it->c, it->prox);
  }
}

int main() {
  scanf("%d %d %d ", &L, &D, &N);
  for(int i = 0; i < D; ++i) {
    scanf("%s", palavra);
    inserir(0, inicio);
  }
  for(int i = 0; i < N; ++i) {
    resultado = 0ll;
    scanf("%s", palavra);
    tamatual = strlen(palavra);
    procurar(0, inicio);
    printf("Case #%d: %d\n", caso++, resultado);
    //atravessar("", inicio);
    //printf("\n");
  }
  return 0;
}
