/**********************************************************************
Author: sproblvem
Created Time:  2011/6/4 22:15:12
File Name: a.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}

int kase;

int ww[1200][3];
double speed[320];
double res[320];

int main() {
	FILE *fout = fopen("a.out", "w");
	scanf("%d", &kase);
	for (int ii = 0; ii < kase; ++ii){
		for (int j = 0; j < 310; ++j){
			speed[j] = 0;
			res[j] = 0;
		}
		int x, s, r, t, n;
		scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
#if 0
		if (ii == 10){
			printf("%d %d %d %d %d\n", x, s, r, t, n);
		}	
#endif
		int acc = r - s;
		int ww_total = 0;
		for (int j = 0; j < n; ++j){
			scanf("%d%d%d", &ww[j][0], &ww[j][1], &ww[j][2]);
			speed[s + ww[j][2]] += ww[j][1] - ww[j][0];
			ww_total += ww[j][1] - ww[j][0];
		}
		speed[s] += x - ww_total;
		double left = (double)t;
		for (int i = 0; i <= 300; ++i){
			if (speed[i] == 0)
				continue;
			if (left){
				if (speed[i] / (double)(i + acc) <= left){
					res[i + acc] += speed[i];
					left -= speed[i] / (double)(i + acc);
				}
				else{
					res[i + acc] += (double)(i + acc) * left;
					res[i] += speed[i] - (double)(i + acc) * left;
					left = 0;
				}
			} else{
				res[i] += speed[i];
			}
		}
		double final = 0;
		for (int i = 1; i <= 300; ++i){
			final += res[i] / (double)i;	
		}
		fprintf(fout, "Case #%d: %lf\n", ii + 1, final);
	}
	fclose(fout);
    return 0;
}

