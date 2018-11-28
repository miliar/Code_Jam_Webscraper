#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <climits>
#include <cstring>
#include <cctype>
#define x first
#define y second
#define in(x, n) (0 <= (x) && (x) < n)
using namespace std;

typedef pair<int, int> Point;

int ccw(pair<int, int> &p0, pair<int, int> &p1, pair<int, int> &p2){
    int dx1, dx2, dy1, dy2;
    dx1=p1.x-p0.x;
    dx2=p2.x-p0.x;
    dy1=p1.y-p0.y;
    dy2=p2.y-p0.y;
    if(dx1*dy2>dy1*dx2)
        return 1;
    if(dx1*dy2<dy1*dx2)
        return -1;
    if(dx1*dx2<0 || dy1*dy2<0)
        return -1; //p2 se encuentraen una posicion a la que podemos llegar llendo de p0 a p1 y p1 a p2 com
    if(dx1*dx1+dy1*dy1 < dx2*dx2+dy2*dy2)
        return 2;  //inverso a las manecillas del reloj
    return 0;      //p2 se encuentra en el segmento entre p0 y p1
}

bool interseccion(pair<int, int> p0, pair<int, int> p1, pair<int, int> p2, pair<int, int> p3)
{
    int valor1, valor2;
/*    imprime(p0);
    imprime(p1);
    imprime(p2);
    imprime(p3);*/
    valor1 = ccw(p0, p1, p2);
    valor2 = ccw(p0, p1, p3);
    if(valor1 == 0 || valor2 == 0 || valor1 != valor2){
        valor1 = ccw(p2, p3, p0);
        valor2 = ccw(p2, p3, p1);
        if(valor1 == 0 || valor2 == 0 || valor1 != valor2)
            return true;
    }
    return false;
}


int main(){
	register int a, b, i, j, n, m, t, k, z, p, q, cont;
	pair<int, int> v[1002];
	set<string> s;
	string cad, aux;
	cin >> t;
	for(z = 1; z <= t; z++){
		cin >> n;
		for(j = 0; j < n; j++){
			cin >> v[j].x >> v[j].y;
		}
		for(i = cont = 0; i < n; i++){
			for(j = i+1; j<n; j++){
				if(interseccion(pair<int, int> (0, v[i].x), pair<int, int> (1, v[i].y), pair<int, int> (0, v[j].x), pair<int, int> (1, v[j].y)))
					cont++;
			}
		}
		cout << "Case #"<< z<<": "<<cont << endl;
		s.clear();
	}
	return 0;
}
