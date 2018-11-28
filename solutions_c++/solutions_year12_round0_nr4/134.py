#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>

using namespace std;

struct Ponto {
	int x,y;
	
	Ponto(int x = 0, int y = 0) : x(x) , y(y) {}
	Ponto operator + (Ponto p){return Ponto(x+p.x, y+p.y);}
	Ponto operator - (Ponto p){return Ponto(x-p.x, y-p.y);}
	//cuidado com overflow daqui pra baixo
	int operator % (Ponto p){return x*p.y - y*p.x;}
	int operator * (Ponto p){return x*p.x + y*p.y;}
	int norma2(){return x*x + y*y;}
	int dist(Ponto p){return (x-p.x)*(x-p.x) + (y-p.y)*(y-p.y);}
	Ponto operator / (int a){return Ponto(x/a, y/a);}
}p,ps[30000];

char ent[100];

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	int z,h,w,d;
	scanf("%d", &z);
	for(int _ = 1; _ <= z; ++_){
		int resp = 0, inix, iniy;
		scanf("%d %d %d", &h, &w, &d);
		d *= d;
		for(int i = 0; i < h; ++i){
			scanf("%s", ent);
			for(int j = 1; j < w; ++j){
				if(ent[j] == 'X') p = Ponto(inix=j,iniy=h-1-i);
			}
		}
		h-=2, w-=2;
		
		int tot = 0;
		for(int i = -62; i <= 62; ++i){
			for(int j = -62; j <= 62; ++j){
				if(!i && !j) continue;
				int a = j*w, b = i*h;
				if(i&1) b += h-iniy+1;
				else b += iniy;
				if(j&1) a += w-inix+1;
				else a += inix;
				ps[tot] = Ponto(a,b);
				if(p.dist(ps[tot]) <= d) ++tot;
			}
		}
		//printf("%d %d\n", iniy, tot);
		int d1, d2;
		double dd1, dd2;
		for(int i = 0; i < tot; ++i){
			//if(p.dist(ps[i]) > d) continue;
			for(int j = 0; j < tot; ++j){
				if(i==j) continue;
				//if((d1=p.dist(ps[j])) > d) continue;
				if(((p-ps[i])%(p-ps[j])) == 0){
					if((d1=p.dist(ps[j])) <= (d2=p.dist(ps[i]))){
						dd1 = sqrt(d1);
						dd2 = sqrt(d2);
						dd1 += sqrt(ps[j].dist(ps[i]));
						if(dd1-1e-3 <= dd2)
							goto hell;
					}
				}
			}
			resp++;
			hell:;
		}
		printf("Case #%d: %d\n", _, resp);
	}
	return 0;
}


