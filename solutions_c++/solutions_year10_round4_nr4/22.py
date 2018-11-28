#include <stdio.h>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <math.h>

using namespace std;

#define lint long long

#define sz size()
#define pb push_back

#define FOR(i,n) SFOR(i,0,n)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

int A[2][400][400];

#define _pi 3.14159265358979323846

double Seg(double R, double f) {
	return f*R*R/2 - R*R*sin(f)/2;
}

int main() {
	int t,tt,i,j,k,p,q;
	int N, K,B,T;
	int x1, x2, y1, y2;
	FILE *fp = fopen("D.in", "r");
	FILE *fp1 = fopen("D.out", "w");
	fscanf(fp, "%d", &tt);
	FOR(t,tt) {
		fscanf(fp,"%d%d",&i,&N);
		fscanf(fp,"%d%d%d%d",&x1,&y1,&x2,&y2);
		double R1, R2, d = sqrt(abs(x1-x2)*abs(x1-x2)*1.0 + abs(y1-y2)*abs(y1-y2));
		double f1, f2;
		fprintf(fp1,"Case #%d:", t+1);
		FOR(k,N) {
			fscanf(fp,"%d%d",&i,&j);
			R1 = sqrt(abs(x1-i)*abs(x1-i)*1.0 + abs(y1-j)*abs(y1-j));
			R2 = sqrt(abs(x2-i)*abs(x2-i)*1.0 + abs(y2-j)*abs(y2-j));
			if (R1 < R2) swap(R1, R2);

			if (R1 > R2 + d) {
				fprintf(fp1," .9lf",_pi*R2*R2);
				continue;
			}
			if (R1*R1 > d*d + R2*R2) {
				f1 = acos((R1*R1 + d*d - R2*R2)/(2*R1*d));
				f2 = acos((R1*R1 - d*d + R2*R2)/(2*R1*R2));
				fprintf(fp1, " %.9lf",_pi*R2*R2 - Seg(R2,2*(f1+f2)) + Seg(R1,2*f1));
			}
			else {
				f1 = acos((R1*R1 + d*d - R2*R2)/(2*R1*d));
				f2 = acos((R2*R2 + d*d - R1*R1)/(2*R2*d));
				fprintf(fp1, " %.9lf",Seg(R1,2*f1) + Seg(R2,2*f2));
			}
		}
		fprintf(fp1,"\n");
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}