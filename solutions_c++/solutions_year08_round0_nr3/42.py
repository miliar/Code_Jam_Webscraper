#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#define TOTAL (2.0 * M_PI)
#define find serem

using namespace std;

int a,b,c,d,e;
double jfly;
double jraket;
double lraket;
double lsenar;
double lbolong;
double lingkaranz;
int jmlcase;
double fx[4],fy[4];
int find;
double answer;
double atas,bawah,kiri,kanan;

bool incircle(double x,double y) {
	if ((x * x) + (y * y) < lingkaranz) return 1;
	return 0;
	}

double intersectx(double y) {
	double itung = lingkaranz - (y * y);
	return sqrt(itung);
	}

double intersecty(double x) {
	double itung = lingkaranz - (x * x);
	return sqrt(itung);
	}

void verify(void) {
	if (fx[find] >= kiri && fx[find] <= kanan && fy[find] >= bawah && fy[find] <= atas) find++;
	}

bool same(double abc,double def) {
		if (fabs(abc - def) < 0.00000001) return 1;
		return 0;
		}

int main() {
	
	scanf("%d",&jmlcase);
	for (e = 0;e < jmlcase;e++) {
		
		printf("Case #%d: ",e + 1);
		scanf("%lf%lf%lf%lf%lf",&jfly,&jraket,&lraket,&lsenar,&lbolong);
		
		lsenar *= 2.0;
		lbolong -= (2.0 * jfly);
		lsenar += (2.0 * jfly);
	
	//printf("%lf %lf %lf %lf %lf\n",jfly,jraket,lraket,lsenar,lbolong);
	if (lbolong < 0.0 || same(lbolong,0.0)) {
		printf("1.000000\n");
		//printf("lbolong\n");
		continue;
		}
	
	lingkaranz = pow(jraket - lraket - jfly,2);
	//printf("%lf\n",lingkaranz);
	
	atas = lsenar / 2.0 + lbolong;
	bawah = lsenar / 2.0;
	kiri = lsenar / 2.0;
	kanan = lsenar / 2.0 + lbolong;
	answer = 0;
	while (1) {
	//printf("%lf %lf %lf %lf\n",kiri,kanan,bawah,atas);
		if ((!incircle(kiri,bawah)) && same(kiri,lsenar / 2.0)) break;
		if ((!incircle(kiri,bawah))) {
			kiri = lsenar / 2.0;
			kanan = lsenar / 2.0 + lbolong;
			bawah = atas + lsenar;
			atas = bawah + lbolong;
			continue;
			}
		
		//find all intersections
		find = 0;
		fx[find] = intersectx(atas); fy[find] = atas;
		verify();
		fx[find] = kiri; fy[find] = intersecty(kiri);
		verify();
		fx[find] = intersectx(bawah); fy[find] = bawah;
		verify();
		fx[find] = kanan; fy[find] = intersecty(kanan);
		verify();
		if (find < 2) {
			//it doesn't intersect the outer area
			answer += ((kanan - kiri) * (atas - bawah));
			}
		if (find >= 2) {
			//printf("%lf %lf %lf %lf\n",fx[0],fy[0],fx[1],fy[1]);
			answer += ((fx[0] - kiri) * (atas - bawah));
			answer += ((fy[1] - bawah) * (kanan - kiri));
			answer -= ((fx[0] - kiri) * (fy[1] - bawah));
			
			//find the sinus
			double irvan = fx[0] - fx[1];
			irvan *= irvan;
			double gogo = fy[0] - fy[1];
			gogo *= gogo;
			double jarak = sqrt(irvan + gogo);
			//printf("%lf %lf\n",jarak,lingkaranz);
			double jarijari = sqrt(lingkaranz);
			
			
			double syn = jarak / 2.0;
			syn /= jarijari;
			//printf("%lf\n",syn);
			double sudut = asin(syn);
			//printf("%lf\n",sudut);
			sudut *= 2.0;
			double luasjuring = sudut / 2.0 * lingkaranz;
			
			double s = sqrt(lingkaranz) * 2.0 + jarak;
			s /= 2.0;
			double luassegitiga = s * (s - jarijari) * (s - jarijari) * (s - jarak);
			luassegitiga = sqrt(luassegitiga);
			//printf("%lf\n",luassegitiga);
			luasjuring -= luassegitiga;
			answer += luasjuring;
			
			double kaki1 = fx[1] - fx[0];
			double kaki2 = fy[0] - fy[1];
			answer += ((kaki1 * kaki2) / 2.0);
			}
		
		kiri = kanan + lsenar;
		kanan = kiri + lbolong;
		}
	
	
	double akhirnya = ((M_PI * jraket * jraket));
	//printf("rebecca : %lf %lf\n",answer, akhirnya);
	answer *= 4.0;
	answer /= akhirnya;

	printf("%.6lf\n",1.0 - answer);
	}
//	printf("%d\n",e);
		
	
	return 0;
	}

