/**********************************************************************
Author: sproblvem
Created Time:  2011/5/7 13:54:33
File Name: c.cpp
Description: 
**********************************************************************/
#include <iostream>
using namespace std;
#define out(x) printf("%s: %I64d\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}
int main() {
    int t = 0;
	FILE *fout = fopen("c.out", "w");
	scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii){
		int n = 0;
		scanf("%d", &n);
		int min_val = 1000010;
		int sum = 0;
		int xor_sum = 0;
		for (int i = 0; i < n; ++i){
			int val = 0;
			scanf("%d", &val);
			sum += val;	
			xor_sum ^= val;
			min_val = min(min_val, val);
		}
		if (xor_sum == 0){
			fprintf(fout, "Case #%d: %d\n", ii + 1, sum - min_val);
		} else{
			fprintf(fout, "Case #%d: NO\n", ii + 1);
		}
	}
	fclose(fout);
    return 0;
}

