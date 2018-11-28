#include<cstdio>
#include<set>

using namespace std;

char dic[5000][16];
int check[5000];
char str[500];
int L, D, N;


int main()
{
	FILE *infile = fopen("a.in", "rt");
	
	fscanf(infile, "%d %d %d", &L, &D, &N);
	int loop, i, j;

	for(i=0; i<D; i++) {
		fscanf(infile, "%s", dic[i]);
	}

	FILE *outfile = fopen("a.out", "wt");
	for(loop=1; loop<=N; loop++) {
		fscanf(infile, "%s", str);
		for(i=0; i<D; i++) check[i] = 0;
		
		int sp = 0;
		for(i=0; i<L; i++) {
			set<char> cs;
			if(str[sp] != '(') cs.insert(str[sp]);
			else 
				while(str[++sp] != ')') cs.insert(str[sp]);
			sp++;
			for(j=0; j<D; j++) {
				if(check[j] == 1) continue;
				if(cs.find(dic[j][i]) == cs.end()) check[j] = 1;
			}
		}

		int result = 0;
		for(i=0; i<D; i++)
			if(check[i] == 0) result++;
	
		fprintf(outfile, "Case #%d: %d\n", loop, result);
	}
	
	fclose(outfile);
	fclose(infile);
	return 0;
}
