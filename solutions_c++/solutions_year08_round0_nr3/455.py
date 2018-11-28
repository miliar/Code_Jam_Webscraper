#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>

using namespace std;

#define TOL 1e-8

typedef complex<double> point;

inline bool isequal(double,double);
inline double dot(const point&,const point&);
inline double cross(const point&,const point&);
int ccw(const point&,const point&,const point&);
inline bool inseg(const point&,const point&,const point&);
inline double dpline(const point&,const point&,const point&);
point projecao(const point&,const point&,const point&,double*);
int lcint(const point&,double,const point&,const point&,point*,point*);
int scint(const point&,double,const point&,const point&,point*,point*);
bool sortbyangle(const int &x,const int &y);
double polyarea(int n,const point *p);

double pi = 2*acos(0);
int dx[] = {-1,1,1,-1};
int dy[] = {-1,-1,1,1};
point d[4];
point help[10];
int pivot;

//testa igualdade com tolerancia, só pra doubles claro
inline bool isequal(double a,double b){
    if(fabs(a-b) < TOL) return true;
    return false;
}

//produto escalar, usar dot(p,p) = quadrado do modulo, ok para <int>
inline double dot(const point &p,const point &q){
    return real(conj(p) * q);
}

//produto vetorial, ok para <int>
inline double cross(const point &p,const point &q){
    return imag(conj(p) * q);
}

//ccw para segint, ok para <int>
int ccw(const point &a,const point &b,const point &c){
    double x;
    x = cross(b-a,c-a);
    if(isequal(x,0)){
    if(dot(a-b,c-b) < 0) return 1;
        if(dot(a-c,b-c) < 0) return -1;
        return 0;   
    }
    if(x < 0) return -1;
    return 1;
}

//verifica se um ponto pertence a um segmento, ok para <int>
inline bool inseg(const point &p,const point &a,const point &b){
    if(isequal(cross(p-a,p-b),0)){
        //-TOL se quiser estritamente dentro
        if(dot(p-a,p-b) < -TOL) return true; 
    }
    return false;
}

//IMPORTANTE: as rotinas de distancias retornam o quadrado da distancia!!!
//distancia de ponto a reta, ok para <int>
inline double dpline(const point &p,const point &a,const point &b){
	double d,x;
	x = cross(p-a,p-b);
	d = x*x/dot(a-b,a-b);
    	//d = x/sqrt(dot(a-b,a-b));
	return d;
}


//calcula a projecao de p em ab...pertence ao segmento ab <=> scale <= 1
point projecao(const point &p,const point &a,const point &b,double *scale){
    point ret;
	
    //*scale = fabs(dot(p-a,b-a))/dot(b-a,b-a);
    *scale = (dot(p-a,b-a))/dot(b-a,b-a);
    //ret = a + (*scale)*(b-a);
    //ret = ((*scale)*b + (sqrt(dot(b-a,b-a))-(*scale))*a)/sqrt(dot(b-a,b-a));
    ret = (*scale)*b + (1 - (*scale))*a;
    return ret;
}


//intersecção de reta com circunferencia
//cuidado com raio zero
int lcint(const point &c,double r,const point &a,const point &b,point *p,point *q){
    double d,x;
    point z,v;
    d = dpline(c,a,b);
    if(d > r*r+TOL) return 0;
    z = projecao(c,a,b,&x);
    x = sqrt(r*r-d);
    v = (b-a)/sqrt(dot(b-a,b-a));
    v *= x;
    *p = z+v;
    *q = z-v;
    if(isequal(d,r*r)){
        *p -= v;
        return 1;
    }
    return 2;
}

int scint(const point &c,double r,const point &a,const point &b,point *p,point *q){
    int k;
    bool inp,inq;
    k = lcint(c,r,a,b,p,q);
    if(!k) return 0;
    inp = inseg(*p,a,b);
    if(k == 2) inq = inseg(*q,a,b);
    else inq = false;
    if(inp && inq) return 2;
    else if(inp) return 1;
    else if(inq){
        *p = *q;
        return 1;    
    }
    return 0;
}

//ordena os pontos por angulo para o graham, supoe pivot global, ok para <int>
bool sorthull(const int &x,const int &y){
    double d;
    point z,w;

    if(x == pivot) return true;
    if(y == pivot) return false;
    z = help[x] - help[pivot];
    w = help[y] - help[pivot];

    d = imag(w * conj(z));
    //se for o mesmo angulo, o mais perto vem primeiro
    if(isequal(d,0)){
        if(dot(z,z) < dot(w,w)-TOL) return true;
        return false;
    }
    if(d > 0) return true;
    return false;
}


//ordena os pontos por ângulo, em torno da origem
//se não quiser origem, só subtrair o centro (antes!), ok para <int>
bool sortbyangle(const int &x,const int &y){
    double d;

    if((help[x].real() < 0) && (help[y].real() > 0)) return false;    
    if((help[y].real() < 0) && (help[x].real() > 0)) return true;
    if(isequal(help[x].real(),0) && (help[x].imag() < 0)) return true;    
    if(isequal(help[y].real(),0) && (help[y].imag() < 0)) return false;

    d = imag(conj(help[y]) * help[x]);
    //se for o mesmo angulo, o mais perto vem primeiro
    if(isequal(d,0)){
        if(dot(help[x],help[x]) < dot(help[y],help[y])-TOL) return true;
        return false;       
    }
    if(d < 0) return true;
    return false;   
}

//calcula a area com sinal do poligono
//+ se anti-horário (acho), ok para <int>, retorna o dobro
double polyarea(int n,const point *p){
    int i,k;
    double ret;
    
    if(n < 3) return 0;
    
    ret = 0;
    for(i=0;i<n;i++){
        k = (1+i) % n;
        ret += p[i].real() * p[k].imag() - p[k].real() * p[i].imag();
    }
    return ret;
}


int main(){
    
    int tst,lp;
    int n;
    int i,j,k,h;
    double f,R,t,r,g;
    
    point inter[20],poly[20];
    int isz,psz;
    int ind[10];
    
    point c,p,q;
    
    double x,y;
    double area;

    /*
    printf("%d\n",scint(point(0,0),1.0-0.1-0.25,point(-0.66,-0.26),point(-0.26,-0.26),&p,&q));
    return 0;
    */
    
    scanf("%d",&tst);
    
    for(lp=1;lp<=tst;lp++){
        printf("Case #%d: ",lp);
        scanf("%lf %lf %lf %lf %lf",&f,&R,&t,&r,&g);
        
        r += f;
        g -= 2*f;
        t += f;
        R -= t;
        
        if(g <= TOL){
            printf("%.6lf\n",1.0);
            continue;
        }
        if(r >= R){
            printf("%.6lf\n",1.0);
            continue;            
        }
        
        n = 10 + (int) (ceil((R-g/2-r)/(g+2*r)+TOL)+TOL);
        //printf("%d\n",n);
        
        for(h=0;h<4;h++){
            d[h] = point(g/2*dx[h],g/2*dy[h]);    
        }
        
        area = 0;
        for(i=1;i<=n;i++){
            if(i == 0) continue;
            for(j=1;j<=n;j++){
                if(j == 0) continue;
                if(i > 0) x = (g/2+r) + (i-1)*(g+2*r);
                else x = -(g/2+r) + (i+1)*(g+2*r);
                
                if(j > 0) y = (g/2+r) + (j-1)*(g+2*r);
                else y = -(g/2+r) + (j+1)*(g+2*r);
                
                c = point(x,y);
                
                isz = psz = 0;
                
                for(h=0;h<4;h++){
                    if(dot(c+d[h],c+d[h])+TOL < R*R) poly[psz++] = c+d[h];  
                }
                
                if(psz == 0){
                    //if(x*x+y*y+TOL < R*R) area += g*g;
                    continue;    
                }
                
                if(psz == 4){
                    area += g*g;
                    continue;    
                }
                
                //printf("   %d\n",psz);
                
                for(h=0;h<4;h++){
                    switch(scint(point(0,0),R,c+d[h],c+d[(h+1)%4],&p,&q)){
                        case 0:
                            break;
                        case 1:
                            help[isz++] = p;
                            break;
                        case 2:
                            help[isz++] = p;
                            help[isz++] = q;
                            //printf("oii\n");
                            break;
                    }    
                }
                
                
                //pedaços circulares
                for(h=0;h<isz;h++){
                    ind[h] = h;    
                }
                sort(&ind[0],&ind[isz],sortbyangle);
                for(h=0;h<isz;h++) inter[h] = help[ind[h]];
                
                double th,seg,buf = 0;
                for(h=0;h<isz-1;h++){
                    seg = dot(inter[h]-inter[h+1],inter[h]-inter[h+1]);
                    if(isequal(seg,0)) continue;
                    th = acos((2*R*R-seg)/(2*R*R));
                    
                    if(isz > 2 && (isequal(inter[h].real(),inter[h+1].real()) || isequal(inter[h].imag(),inter[h+1].imag()))){
                        //area -= (th-sin(th))*R*R/2;
                        //printf("oie\n");
                    }
                    else{
                        //area += (th-sin(th))*R*R/2;
                        //printf("%.10lf %.10lf %.10lf\n",th,sin(th),th-sin(th));
                        area += th*R*R/2 - sin(th)*R*R/2;
                    }
                    
                }
                
                //printf("   %d\n",isz);
                
                for(h=0;h<isz;h++){
                    poly[psz++] = inter[h];    
                }
                
                pivot = 0;
                for(h=1;h<psz;h++){
                    if(isequal(poly[h].real(),poly[pivot].real()) && poly[h].imag() < poly[pivot].imag()){
                        pivot = h;    
                    }
                    else if(poly[h].real() < poly[pivot].real()){
                        pivot = h;    
                    }   
                }
                
                for(h=0;h<psz;h++){
                    help[h] = poly[h];
                    ind[h] = h;
                }
                sort(&ind[0],&ind[psz],sorthull);
                for(h=0;h<psz;h++) poly[h] = help[ind[h]];
                
                //for(h=0;h<psz;h++) printf("oie %.6lf %.6lf\n",poly[h].real(),poly[h].imag());
                //printf("\n\n");
                
                while(polyarea(psz,poly) < 0){
                    
                }
                
                area += fabs(polyarea(psz,poly))/2;
                
            }    
        }
        
        area *= 4;
        
        printf("%.6lf\n",1-area/(pi*(R+t)*(R+t)));
        
    }
    
    return 0;
    
}
