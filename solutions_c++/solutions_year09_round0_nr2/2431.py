#include<stdio.h>
#include<iostream>
#include<vector>
#include<complex>
#include<map>
#include<string.h>
using namespace std;

typedef complex<int> point;

class pointLessThan {
public:
   bool operator( )(const point& a, const point& b) const {
     if (real(a)<real(b)) return true;
     if ((real(a)==real(b)) && (imag(a)<imag(b))) return true;
     return false;
   }
};


#define tamT 123
#define tamAlt 10123
#define tamH 123
#define tamW 123


bool dentroDim(point p,point dim){
  if ((real(p) < 0) || (real(p)>=real(dim))) return false;
  if ((imag(p) < 0) || (imag(p)>=imag(dim))) return false;
  return true;
}

vector < point > vizinhos(point p,point dimensions){
  vector <point> v(0);
  vector <point> desv(4);
  desv[0] = point (-1,0);
  desv[1] = point (0,-1);
  desv[2] = point (0,1);
  desv[3] = point (1,0);
  for(unsigned int i=0;i<desv.size();i++){
    if ( dentroDim(p+desv[i],dimensions) ){
      v.push_back(p+desv[i]);
    }
  }
  return v;
}

point achaLivre(char F[tamH][tamW+1],int H,int W){
  for(int lin=0;lin<H;lin++){
    for(int col=0;col<W;col++){
      if(F[lin][col] == 0){
	return (point (lin,col) );
      }
    }
  }
  return (point(-1,-1));
}

int main(){
  int T,H,W;
  int mapa[tamH][tamW];
  scanf("%d",&T);
  for(int numMapa=1;numMapa<=T;numMapa++){
    map <point,point,pointLessThan> pai;
    scanf(" %d %d ",&H,&W);
    for(int lin=0;lin<H;lin++){
      for(int col=0;col<W;col++){
	scanf("%d",&mapa[lin][col]);
      }
    }
    for(int lin=0;lin<H;lin++){
      for(int col=0;col<W;col++){
	point pAtual = point(lin,col);
	point pZero = point(0,0);
	vector <point> viz = vizinhos(pAtual,point(H,W));
	int valMin=tamAlt+1;
	int min=-1;
	for(unsigned int i=0;i<viz.size();i++){
	  int altViz=mapa[real(viz[i])][imag(viz[i])];
	  if (mapa[lin][col] > altViz){
	    if(valMin > altViz){
	      valMin = altViz;
	      min = i;
	    }
	  }
	}
	if(min != -1){
	  point p = viz[min];
	  pai[ pAtual ] = p ;
	}else{
	  pai[ pAtual ] = pAtual;
	}
      }
    }
    map <point,point,pointLessThan> paiDeTodos;
    for(int lin=0;lin<H;lin++){
      for(int col=0;col<W;col++){
	point p;
	point pAtual;
	p =pAtual= point(lin,col);
	while(pai[p]!=p)
	  p = pai[p];
	paiDeTodos[pAtual] = p;
      }
    }
    char final[tamH][tamW+1];
    char letraAtual='a';
    memset(final,0,sizeof(final));
    point livre;
    while( (livre = achaLivre(final,H,W)) != point(-1,-1)){
      final[real(livre)][imag(livre)] = letraAtual;
      for(int lin=0;lin<H;lin++){
	for(int col=0;col<W;col++){
	  if (paiDeTodos[livre] == paiDeTodos[point(lin,col)]){
	    final[lin][col] = letraAtual;
	  }
	}
      }
      letraAtual++;
    }
    printf("Case #%d:\n",numMapa);
    for(int lin=0;lin<H;lin++){
      for(int col=0;col<W;col++){
	printf("%c",final[lin][col]);
	if(col < W-1){
	  printf(" ");
	}
      }
      printf("\n");
    }
  }  
  return 0;
}
