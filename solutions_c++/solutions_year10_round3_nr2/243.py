#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
using namespace std;

FILE* fin = fopen("B-large.in", "r");
FILE* fout = fopen("B-large.out", "w");

int main()
{
	int t, i;
	__int64 l, p, c, a, b;
	fscanf(fin, "%d", &t);
	for(i = 1; i <= t; ++i){
		fscanf(fin, "%I64d%I64d%I64d", &l, &p, &c);
		int ret = 0;
		while (l * c < p){
			__int64 a = sqrt(double(p * l));
			__int64 b = a + 1;
			if (p * l > a * b){
				p = b;
			}
			else{
				l = a;
			}
			ret++;
		}
		fprintf(fout, "Case #%d: %I64d\n", i, ret);
	}
	return 0;
}