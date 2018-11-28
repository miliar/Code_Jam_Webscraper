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

int com_mat[30][30];
int ops_mat[30][30];
int magicka[150];
char seq_str[200];

int main() {
    int t = 0;
	FILE *fout = fopen("b.out", "w");
	scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii){
		int c = 0;
		scanf("%d", &c);
		char com_str[10];
		memset(com_mat, -1, sizeof(com_mat));
		for (int i = 0; i < c; ++i){
			scanf("%s", com_str);
			//printf("%s\n", com_str);
			int a = com_str[0] - 'A', b = com_str[1] - 'A', val = com_str[2] - 'A';
			com_mat[a][b] = val;
			com_mat[b][a] = val;
		}

		int d = 0;
		scanf("%d", &d);
		char ops_str[10];
		memset(ops_mat, 0, sizeof(ops_mat));
		for (int i = 0; i < d; ++i){
			scanf("%s", ops_str);
			int a = ops_str[0] - 'A', b = ops_str[1] - 'A';
			ops_mat[a][b] = 1;
			ops_mat[b][a] = 1;
		}
		
		int n = 0;
		scanf("%d", &n);
		scanf("%s", seq_str);
		memset(magicka, -1, sizeof(magicka));	
		int pos = 1;
		for (int i = 0; i < n; ++i){
			int num = seq_str[i] - 'A';
			magicka[pos++] = num;
			if (pos <= 2)
				continue;
			if (com_mat[magicka[pos - 2]][magicka[pos - 1]] > -1){
				pos -= 1;
				magicka[pos - 1] = com_mat[magicka[pos - 1]][magicka[pos]];
				continue;
			}
			for (int j = 1; j < pos - 1; ++j){
				if (ops_mat[magicka[j]][num]){
					pos = 1;
					break;
				}
			}
		}
		//printf("pos : %d\n", pos);
		fprintf(fout, "Case #%d: [", ii + 1);
		if (pos <= 1){
			fprintf(fout, "]\n");
			continue;
		}
		fprintf(fout, "%c", magicka[1] + 'A');
		for (int i = 2; i < pos; ++i){
			fprintf(fout, ", %c", magicka[i] + 'A');
		}
		fprintf(fout, "]\n");
	}
	fclose(fout);
    return 0;
}

