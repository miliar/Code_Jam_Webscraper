#include <iostream>
#include <string>
#include <algorithm>
#include <string.h>
using namespace std;
int cases,L,D,N;
int controle[500][251];
int existe[150];
string dic[5000],pal[500];
int words[15];
void resolve (int cur, int curpos, int pos, int pare, int begin, int end, string aux);
int main() {

  int i,j;
  int exist,pos;
  scanf("%d %d %d",&L,&D,&N);
  getchar();
  memset(controle,-1,sizeof(controle));
  for (i = 0 ; i < D ; i++) {
    getline(cin,dic[i]);
  }
  sort(dic,dic+D);
  memset(existe,-1,sizeof(existe));
  for (i = 0 ; i < D ; i++) {
    if (existe[dic[i][0]] == -1) {
      existe[dic[i][0]] = i;
      //printf("Existe %c = %d\n",dic[i][0],i);
    }
  }
  for (i = 0 ; i < N ; i++) {
    getline(cin,pal[i]);
    exist = 0;
    for (j = 0 ; j < pal[i].size() ; j++) {
      if (pal[i][j] == ')') {
	controle[i][exist++] = j;
      }
    }
  }
  
  for (i = 0 ; i < N ; i++) {
    cases = 0;
    exist = 0;
    pos = 0;
    for (j = 0 ; j < pal[i].size() ; j++) {
      if (pal[i][j] == '(') {
	exist = 1;
	pos++;
      }
      else if (pal[i][j] == ')') {
	exist = 0;
      }
      else if (exist == 0) pos++;
    }
    if (pos == L) resolve(i,0,0,0,0,0,"");
    printf("Case #%d: %d\n",i+1,cases);
  }
  
  return 0;
}
  void resolve (int cur, int curpos, int pos, int pare, int begin, int end, string aux) {
    string aux2;
    int i,j,k,x;
    if (curpos == L) {
      cases++;
      return;
    }
    if (curpos == 0) {
      if (pal[cur][pos] != '(') {
	if (existe[pal[cur][pos]] == -1) {
	  //  printf("ID = %d\n",pal[cur][pos]);
	  return;
	}
	else {
	  aux2 = pal[cur][pos];
	  x = existe[pal[cur][pos]];
	  j = x+1;
	  while (j != D) {
	    if (pal[cur][pos] != dic[j][0])
	      break;
	    j++;
	  }
	  //	  printf("Soh tinha uma possibilidade, eu vou ter que buscar nas palavras de %d a %d\n",x,j);
	  resolve(cur,curpos+1,pos+1,pare,x,j,aux2);
	}
      }
      else {
	for (i = pos+1 ; i < controle[cur][pare] ; i++) {
	  if (existe[pal[cur][i]] != -1) {
	    x = existe[pal[cur][i]];
	    //   printf("X = %d\n",x);
	    for (j = x+1 ; j < controle[cur][pare] ; j++) {
	      if (dic[j][0] != pal[cur][i])
		break;
	    }
	    aux2 = pal[cur][i];
	    resolve(cur,curpos+1,controle[cur][pare]+1,pare+1,x,j,aux);
	  }
	}
      }
      return;
    }
    else {
      if (pal[cur][pos] != '(') {
	for (i = begin ; i < end ; i++) {
	  if (pal[cur][pos] == dic[i][curpos]) 
	    break;
	}
	if (i == end) return;
	for (j = i+1 ; j < end ; j++) {
	  if (pal[cur][pos] != dic[j][curpos])
	    break;
	}
	aux2 = aux + pal[cur][pos];
	resolve(cur,curpos+1,pos+1,pare,i,j,aux2);
      }
      else {
	for (i = pos+1 ; i < controle[cur][pare] ; i++) {
	  for (j = begin ; j < end ; j++) {
	    if (pal[cur][i] == dic[j][curpos]) {
	      break;
	    }
	  }
	  if (j != end) {
	    for (k = j+1 ; k < end ; k++) {
	      if (pal[cur][i] != dic[k][curpos]) {
		break;
	      }
	    }
	    aux2 = aux+pal[cur][i];
	    resolve(cur,curpos+1,controle[cur][pare]+1,pare+1,j,k,aux2);
	  }
	}
      }
      }
  }
