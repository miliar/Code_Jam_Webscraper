#include <cstdio>
#include <cstring>
#include <cmath>

#include <algorithm>

using namespace std;

int N;
int plants[5][3];

struct Ponto {
	double x, y;
	
	Ponto () {
	
	}
	
	Ponto(double xNovo, double yNovo) {
		x = xNovo;
		y = yNovo;
	}
	
	Ponto operator +(Ponto p) {
		return Ponto(x+p.x, y+p.y);
	}
	
	Ponto operator -(Ponto p) {
		return Ponto(x-p.x, y-p.y);
	}
	
	double operator *(Ponto p) {
		return x*p.x + y*p.y;
	}
	
	Ponto operator /(double k) {
		return Ponto(x/k,y/k);
	}
	
	Ponto operator *(double k) {
		return Ponto(x*k,y*k);
	}
};

void read() {
	scanf("%d", &N);
	
	for (int i = 0; i < N; i++) {
		scanf("%d%d%d", &plants[i][0], &plants[i][1], &plants[i][2]);
	}
}

double dist(double x1, double y1, double x2, double y2) {
	return sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}

Ponto norm(Ponto v) {
	double tam = sqrt(v*v);
	return v/tam;
}

double calc2(int ind1, int ind2) {
	Ponto p1(plants[ind1][0], plants[ind1][1]);
	Ponto p2(plants[ind2][0], plants[ind2][1]);
	
	Ponto v = p2-p1;
	//printf("v %lf,%lf\n", v.x, v.y);
	Ponto vNorm = norm(v);
	//printf("vNorm %lf,%lf\n", vNorm.x, vNorm.y);
	
	Ponto q2 = p2 + vNorm*plants[ind2][2];
	Ponto q1 = p1 - vNorm*plants[ind1][2];
	//printf("p2 %lf,%lf\n", p2.x,p2.y);
	//printf("p1 %lf,%lf\n", p1.x,p1.y);
	//printf("q2 %lf,%lf\n", q2.x,q2.y);
	//printf("q1 %lf,%lf\n", q1.x,q1.y);
	
	Ponto m = (q1+q2)/2;
	
	return dist(q2.x, q2.y, m.x, m.y);

	/*
	int x1 = plants[ind1][0];
	int y1 = plants[ind1][1];
	
	int x2 = plants[ind2][0];
	int y2 = plants[ind2][1];

	double xMed = ((double)(x1+x2))/2;
	double yMed = ((double)(y1+y2))/2;
	
	double r = dist(x1, y1, xMed, yMed) + plants[ind1][2];
	double temp = dist(x2, y2, xMed, yMed) + plants[ind2][2];
	
	if (r > temp) {
		return r;
	} else {
		return temp;
	}
	*/
}

double calc3(int ind1, int ind2, int ind3) {
	int x1 = plants[ind1][0];
	int y1 = plants[ind1][1];
	
	int x2 = plants[ind2][0];
	int y2 = plants[ind2][1];
	
	int x3 = plants[ind3][0];
	int y3 = plants[ind3][1];

	double xMed = ((double)(x1+x2+x3))/2;
	double yMed = ((double)(y1+y2+y3))/2;
	
	double r = dist(x1, y1, xMed, yMed) + plants[ind1][2];
	double temp = dist(x2, y2, xMed, yMed) + plants[ind2][2];
	
	if (temp > r) {
		r = temp;
	}
	
	temp = dist(x3, y3, xMed, yMed) + plants[ind3][2];
	
	if (temp > r) {
		r = temp;
	}
	
	return r;
}

double menor(double a, double b) {
	if (a < b) {
		return a;
	} else {
		return b;
	}
}

void process() {
	double r;
	if (N == 1) {
		r = plants[0][2];
	} else if (N == 2) {
		//r = calc2(0,1);
		
		r = plants[0][2];
		
		if (plants[1][2] > r) {
			r = plants[1][2];
		}
	} else {
		//r = calc3(0,1,2);
		
		r = calc2(0,1);
		if (plants[2][2] > r) {
			r = plants[2][2];
		}
		
		double temp;
		temp = calc2(0,2);
		if (plants[1][2] > temp) {
			temp = plants[1][2];
		}
		r = menor(r,temp);
		
		temp = calc2(1,2);
		if (plants[0][2] > temp) {
			temp = plants[0][2];
		}
		r = menor(r,temp);
	}
	
	printf("%.6lf\n", r);
}

int main() {
	freopen("D-small-attempt2.in", "r", stdin);
	freopen("d.out", "w", stdout);
	
	int casos;
	scanf("%d", &casos);
	
	for (int i = 1; i <= casos; i++) {
		printf("Case #%d: ", i);
	
		read();
		process();
	}
	
	return 0;
}
