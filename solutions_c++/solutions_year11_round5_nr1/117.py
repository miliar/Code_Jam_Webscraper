#include <iostream> 
#include <vector> 
#include <cstdio> 
#include <cstring> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <string> 
#include <sstream> 
#include <ctime> 
#include <cmath> 

using namespace std; 

int T, W, L, U, G;
int lx[105], ly[105], ux[105], uy[105];
double l[1005], u[1005], area[1005];

int main() { 
	FILE *fin = fopen("test.txt", "r");  
	FILE *fout = fopen("testans.txt", "w");
	
	fscanf(fin, "%d", &T);
	
	for (int z = 1; z <= T; z++) {
        //printf("Case #%d: %d\n", z);
        fprintf(fout, "Case #%d:\n", z);
        
		fscanf(fin, "%d %d %d %d", &W, &L, &U, &G);
		for (int i = 1; i <= L; i++) {
			fscanf(fin, "%d %d", &lx[i], &ly[i]);
			l[lx[i]] = ly[i];
			if (i == 1) continue;
			double slope = (double)(ly[i]-ly[i-1])/(lx[i]-lx[i-1]);
			for (int j = lx[i-1]+1; j < lx[i]; j++) {
				l[j] = l[j-1] + slope;
			}
		}
		//for (int i = 1; i <= W; i++) printf("%.7f\n", l[i]);
		//printf("here");
		for (int i = 1; i <= U; i++) {
			fscanf(fin, "%d %d", &ux[i], &uy[i]);
			u[ux[i]] = uy[i];
			if (i == 1) continue;
			double slope = (double)(uy[i]-uy[i-1])/(ux[i]-ux[i-1]);
			for (int j = ux[i-1]+1; j < ux[i]; j++) {
				u[j] = u[j-1] + slope;
			}
		}
		//for (int i = 1; i <= W; i++) printf("%.7f\n", u[i]);
		//printf("here");
		double totarea = 0;
		for (int i = 1; i <= W; i++) {
			totarea += 0.5*(u[i-1]-l[i-1]+u[i]-l[i]);
			area[i] = 0.5*(u[i-1]-l[i-1]+u[i]-l[i]);
		}
		//for (int i = 1; i <= W; i++) printf("%.7f\n", totarea);
		double curarea = 0;
		int curnum = 1;
		//printf("here");
		for (int i = 1; i <= W; i++) {
            //printf("i is %d\n", i);
            //printf("%.7f\n", curnum*totarea/G);
            //printf("%d\n", i);
			if (curnum == G) break;
			//printf("%d\n", i);
			//printf("%.7f\n", curarea+area[i]);
			if (curarea + area[i] <= curnum*totarea/G) {
				curarea += area[i]; continue;
			}
			//printf("%d\n", i);
			double lo = 0.0, hi = 1.0, mid = (lo+hi)/2;
			int cnt = 0;
			while (cnt < 100) {
                //printf("%d\n", cnt);
				double ld = u[i-1]-l[i-1], rd = u[i]-l[i];
				double height = mid*rd + (1-mid)*ld;
				double thisarea = 0.5*mid*(ld+height);
				if (curarea + thisarea <= curnum*totarea/G) lo = mid;
				else hi = mid;
				mid = (lo+hi)/2;
				cnt++;
			}
			//printf("mid is %.7f\n", mid);
			//printf("%.7f\n", i-1+mid);
			fprintf(fout, "%.7f\n", i-1+mid);
			curnum++;
			i--;
		}
	}
	
	
	
	
	//cin.get();
	
    return 0;
}

