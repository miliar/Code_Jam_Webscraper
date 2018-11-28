#include <stdio.h>
#include <string.h>

int main(int argc,char** argv) {
	FILE *input = fopen("C:/Documents and Settings/Mina/Desktop/A-large.in","rb");
	FILE *output = fopen("C:/Documents and Settings/Mina/Desktop/A-large.out","wb");
	char buffer[101] = {0};
	int N = 0;
	fgets(buffer,101,input);
	sscanf(buffer,"%d",&N);
	for(int n = 0;n < N;n++) {
		int S = 0,Q = 0,switches = 0;
		bool *x;
		char (*engines)[101] = {0},(*queries)[101] = {0};
		fgets(buffer,101,input);
		sscanf(buffer,"%d",&S);
		engines = new char[S][101];
		for(int s = 0;s < S;s++) {
			fgets(engines[s],101,input);
		}
		fgets(buffer,101,input);
		sscanf(buffer,"%d",&Q);
		queries = new char[Q][101];
		for(int q = 0;q < Q;q++) {
			fgets(queries[q],101,input);
		}
		x = new bool[S];
		for(int s = 0;s < S;s++) {
			x[s] = false;
		}
		for(int q = 0;q < Q;q++) {
			int last_engine;
			for(int s = 0;s < S;s++) {
				if(!strcmp(engines[s],queries[q])) {
					x[s] = true;
					last_engine = s;
					break;
				}
			}
			bool c = true;
			for(int s = 0;s < S;s++) {
				if(!x[s]) {
					c = false;
					break;
				}
			}
			if(c) {
				switches++;
				for(int s = 0;s < S;s++) {
					x[s] = false;
				}
				x[last_engine] = true;
			}
		}
		delete []x;
		sprintf(buffer,"Case #%d: %d\n",n + 1,switches);
		fputs(buffer,output);
		delete []queries;
		delete []engines;
	}
	fclose(output);
	fclose(input);
	return 0;
}