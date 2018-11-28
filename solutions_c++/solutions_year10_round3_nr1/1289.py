#include <iostream>
#include <math.h>
#include <stdlib.h>

using namespace std;

typedef struct Ponto
{
    float x, y;
    void imprime(const char *s)
    {
        cout << s << ": " << x << "," << y << endl ;
    }
} Ponto;

typedef struct Segmento{
	Ponto a,b;
}Segmento;


Ponto Meio(Ponto P1, Ponto P2)
{
    Ponto P;
    P.x = (P1.x+P2.x)/2.0;
    P.y = (P1.y+P2.y)/2.0;
    return P;
}
int Lado(Ponto P1, Ponto P2, Ponto P)
{
    Ponto V1, V2;
    V1.x = P2.x - P1.x;
    V1.y = P2.y - P1.y;
    V2.x = P.x - P1.x;
    V2.y = P.y - P1.y;
    //V1.imprime("V1");
    //V2.imprime("V2");
    float k = V1.x * V2.y - V1.y * V2.x;
    if (fabs(k) < 0.0001)
        return 0;
    if (k>0)
        return -1;
    else return 1;
}

int existeIntersec(Segmento s1, Segmento s2)
{
    int La, Lb, L1, L2;
    La = Lado(s1.a, s1.b, s2.a);
    Lb = Lado(s1.a, s1.b, s2.b);
    if (La == Lb) return 0;
    L1 = Lado(s2.a, s2.b, s1.a);
    L2 = Lado(s2.a, s2.b, s1.b);
    if (L1 == L2) return 0;
    return 1;
}

int existeIntersec(Ponto P1, Ponto P2, Ponto PA, Ponto PB)
{
    int La, Lb, L1, L2;
    La = Lado(P1, P2, PA);
    Lb = Lado(P1, P2, PB);
    
    if (La == Lb) return 0;
    L1 = Lado(PA, PB, P1);
    L2 = Lado(PA, PB, P2);
    if (L1 == L2) return 0;
    return 1;
}
Ponto calcIntersecDIV_BIN(Ponto P1, Ponto P2, Ponto PA, Ponto PB)
{
    int La, Lb, Lm;
    Ponto Pm;
    do
    {
//        La = Lado(P1, P2, PA);
//        Lb = Lado(P1, P2, PB);
//        if (La == Lb) return 0;
        Pm = Meio (PA, PB);
        Lm = Lado(P1, P2, Pm);
        if (Lm == 0) // encontrou a interseccao
            return Pm;
        La = Lado(P1, P2, PA);
        Lb = Lado(P1, P2, PB);
        if (La == Lm) // descarta o PA
            PA = Pm;
        if (Lb == Lm) PB = Pm;
    }
    while (1);
}
/* ********************************************************************** */
/*                                                                        */
/*  Calcula a interseccao entre 2 retas (no plano "XY" Z = 0)             */
/*                                                                        */
/* k : ponto inicial da reta 1                                            */
/* l : ponto final da reta 1                                              */
/* m : ponto inicial da reta 2                                            */
/* n : ponto final da reta 2                                              */
/*                                                                        */
/* s: valor do parâmetro no ponto de interseção (sobre a reta KL)      */
/* t: valor do parâmetro no ponto de interseção (sobre a reta MN)      */
/*                                                                        */
/* ********************************************************************** */
int intersec2d(Ponto k, Ponto l, Ponto m, Ponto n, float &s, float &t)
{
    double det;
    det = (n.x - m.x) * (l.y - k.y)  -  (n.y - m.y) * (l.x - k.x);
    if (det == 0.0)
        return 0 ; // nao ha intersecao
    s = ((n.x - m.x) * (m.y - k.y) - (n.y - m.y) * (m.x - k.x))/ det ;
    t = ((l.x - k.x) * (m.y - k.y) - (l.y - k.y) * (m.x - k.x))/ det ;
    return 1; // ha intersecao
}

int calcIntersecEQU_RETA(Ponto P1, Ponto P2, Ponto PA, Ponto PB, Ponto &Pm)
{
    float s,t;
    if (!intersec2d(P1,P2, PA, PB, s, t))
        return 0;
    if ((s < 0) || (s>1) || (t<0) || (t>1) )
       return 0;
    Pm.x = P1.x + (P2.x-P1.x)*s;
    Pm.y = P1.y + (P2.y-P1.y)*s;
    return 1;
}
int main(int argc, char *argv[])
{
    Ponto A, B, C, D, P1, P2;
    
    Ponto Pontos[2001];
    Segmento Seg[1001];
    int a,b;
    int cont;
    
    int t,n,i,j,teste;
    
    scanf("%d",&t);
    
    
    
    
    for(teste=1;teste<=t;teste++){
	
		scanf("%d",&n);
		
		for(i=0;i<n;i++){
			scanf("%d %d",&a,&b);
			Pontos[2*i].x = 1;
			Pontos[2*i].y = a;
			
			
			Pontos[2*i+1].x = 2;
			Pontos[2*i+1].y=b;
			
			Seg[i].a = Pontos[2*i];
			Seg[i].b = POntos[2*i+1];
			
			
		}
		
		cont = 0;
		for(i=0;i<n;i++){
		 for(j=i+1;j<n;j++){
		 	if(existeIntersec(Seg[i] , Seg[j]) ) cont++;
		 }
		}
		
		printf("Case #%d: %d\n",teste,cont);
	
	}
    
    
    
    
    return EXIT_SUCCESS;
}


