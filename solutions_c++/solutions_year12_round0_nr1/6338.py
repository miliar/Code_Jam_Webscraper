#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

char vet[1000];



int main(){

vet[97] = 'y';
vet[111] = 'k';
vet[122] = 'q';
vet[101] = 'o';
vet[106] = 'u';
vet[117] = 'j';
vet[112] = 'r';
vet[114] = 't';
vet[109] = 'l';
vet[108] = 'g';
vet[115] = 'n';
vet[110] = 'b';
vet[99] = 'e';
vet[107] = 'i';
vet[100] = 's';
vet[120] = 'm';
vet[118] = 'p';
vet[121] = 'a';
vet[102] = 'c';
vet[119] = 'f';
vet[105] = 'd';
vet[98] = 'h';
vet[116] = 'w';
vet[104] = 'x';
vet[103] = 'v';
vet[113] = 'z';
vet[32] = 32;


	FILE *out = fopen("out.out", "w");
	FILE *in = fopen("in.in", "r");
	int t, intAsc, k, i;
	char str[110];


	while (fscanf(in, "%d", &t) > 0){
		for (i = 0; i < t; i++){
			fscanf(in, " %100[^\n]", str);
			for(k = strlen(str); k >= 0; k--){
				intAsc = str[k];
				str[k] = vet[intAsc];
			}
			fprintf(out, "Case #%d: %s\n",i+1, str);
		}
	}
}
