#include "stdio.h"
#include "string.h"
#include <vector>
using namespace std;

char ** get_sub_str(int L, char * buf) {
	char **p = new char * [L];
	char c;
	char *temp;
	temp = new char [27];
	int j, k=0;
	for (int i=0; i<L; i++) {
		c = buf[k++];
		if ( c == '(' ) {
			j=0;
			while ( (c = buf[k++]) != ')' ) {
				temp[j] = c;
				j++;
			}
			temp[j]='\0';
			p[i] = new char [strlen(temp) + 1];
			strcpy(p[i], temp);
		} else {
			p[i] = new char [2];
			p[i][0] = c;
			p[i][1] = '\0';
		}
	}
	return p;
}

int main ( int argc,char *argv[] ) {
	FILE *fin, *fout;
	fin = fopen ( argv[1], "r" );
	if ( ! fin ) return 0;
	int L, D, N;
	fscanf( fin, "%d %d %d\n", &L, &D, &N);
	char ** charset;
	charset = new char* [D];
	int i,j,k,kk,l,ll;
	for ( i=0; i<D; i++ ) {
		charset[i] = new char [L+1];
		fscanf(fin, "%s\n", charset[i]);
	}
	vector <int> ** dataset;
	dataset = new (vector <int> * [L]);
	for (i=0; i<L; i++) dataset[i] = new (vector <int> [26]);
	for (i=0; i<D; i++) {
		for(j=0; j<L; j++) {
			//printf("%d ", i);
			dataset[j][charset[i][j]-'a'].push_back(i);
			//dataset[j][charset[i][j]-'a'][dataset[j][charset[i][j]-'a'].size()-1]=i;
		}
	}
	for (i=0; i<L; i++) {
		for(j=0; j<26; j++) {
			for (k=0; k<dataset[i][j].size(); k++) {
				//printf("(i=%d, char= %c):%d   \n",i, j+'a', dataset[i][j][k]);
			}
		}
	}
	fout = fopen ( argv[2], "w" );
	char buf[4096];
	char ** test;
	int *match;
	int num;
	match = new int[D];
	for ( i=0; i<N; i++ ) {
		for ( j=0; j<D; j++ ) match[j] = 0;
		fscanf(fin, "%s\n", buf);
		//printf("string:%s\n",buf);
		test = get_sub_str(L, buf);
		for (j=0; j<L; j++) {
			//printf("%s\n", test[j]);
			kk = strlen(test[j]);
			for(k=0; k<kk; k++) {
				ll = dataset[j][test[j][k]-'a'].size();
				for (l=0; l<ll; l++) {
					match[dataset[j][test[j][k]-'a'][l]]++;
				}
			}
		}
		//printf("\n");
		num = 0;
		for (j=0; j<D; j++) {
			//printf("match [%d] : %d\n", j, match[j]);
			if ( match[j] == L ) num ++;
		}
		fprintf(fout, "Case #%d: %d\n", i+1, num);
		//printf("%d\n", num);
	}
	fclose ( fin );
	if ( ! fout ) return 0;
	fclose (fout);
	return 1;
}