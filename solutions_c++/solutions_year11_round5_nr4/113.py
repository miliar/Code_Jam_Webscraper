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

int T, qmark[25], qnum, len;
char initarr[80];
int curarr[80];
long long powtwo[62];

int main() { 
	FILE *fin = fopen("test.txt", "r");  
	FILE *fout = fopen("testans.txt", "w");
	
	powtwo[0] = 1;
	for (int i = 1; i < 62; i++) {
		powtwo[i] = powtwo[i-1]*2;
	}
	
	fscanf(fin, "%d", &T);
	
	for (int z = 1; z <= T; z++) {
		fscanf(fin, "%s", &initarr);
		len = strlen(initarr); qnum = 0;
		for (int i = 0; i < len; i++) {
			if (initarr[i] == '?') qmark[qnum++] = i;
		}
		int K = 1 << qnum;
		for (int i = 0; i < len; i++) {
			if (initarr[i] == '0') curarr[i] = 0;
			if (initarr[i] == '1') curarr[i] = 1;
		}
		//printf("here\n");
		for (int i = 0; i < K; i++) {
			for (int j = 0; j < qnum; j++) {
				int curbit = (i >> j) & 1;
				if (curbit == 0) {
					curarr[qmark[j]] = 0;
				} else {
					curarr[qmark[j]] = 1;
				}
			}
			long long cur = 0LL;
			for (int i = 0; i < len; i++) {
				cur += powtwo[len-1-i]*curarr[i];
			}
			//printf("cur %lld\n", cur);
			long long lo = 1, hi = 2147483647, mid = (lo+hi)/2;
			while (true) {
				if (hi < lo) break;
				if (lo >= hi-1) {
					if (lo*lo == cur) {
						//printf("Case #%d: ", z);
						fprintf(fout, "Case #%d: ", z);
						for (int i = 0; i < len; i++) {
							//printf("%d", curarr[i]);
							fprintf(fout, "%d", curarr[i]);
						}
						//printf("\n");
						fprintf(fout, "\n");
						break;
					} if (hi*hi == cur) {
						//printf("Case #%d: ", z);
						fprintf(fout, "Case #%d: ", z);
						for (int i = 0; i < len; i++) {
							//printf("%d", curarr[i]);
							fprintf(fout, "%d", curarr[i]);
						}
						//printf("\n");
						fprintf(fout, "\n");
						break;
					}
					break;
				}
				//printf("lo hi mid %lld %lld %lld\n", lo, hi, mid);
				if (mid*mid == cur) {
					//printf("Case #%d: ", z);
					fprintf(fout, "Case #%d: ", z);
					for (int i = 0; i < len; i++) {
						//printf("%d", curarr[i]);
						fprintf(fout,"%d", curarr[i]);
					}
					//printf("\n");
					fprintf(fout,"\n");
					break;
				} else if (mid*mid < cur) lo = mid;
				else hi = mid;
				mid = (lo+hi)/2;
			}
		}
	}
	
	
	
	
	//cin.get();
	
    return 0;
}

