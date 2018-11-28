#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
struct line{
	int a, b;
}l[1001];
FILE* fin = fopen("A-large.in", "r");
FILE* fout = fopen("A-large.out", "w");
bool operator < (line& a, line& b)
{
	return a.a < b.a;
}
int main()
{
	int Case, T;
	fscanf(fin, "%d",&Case); 
	for(T = 1; T <= Case; T++){
		int n, i, j;
		fscanf(fin, "%d", &n);
		for(i = 0; i < n; i++){
			fscanf(fin, "%d%d", &l[i].a, &l[i].b);
		}
		sort(l, l + n);
		int ret = 0;
		for(i = 0; i < n; i++)
			for(j = i; j < n; j++){
				if(l[i].b > l[j].b)
					ret++;
			}
		fprintf(fout, "Case #%d: %d\n", T, ret);
	}
	return 0;
}