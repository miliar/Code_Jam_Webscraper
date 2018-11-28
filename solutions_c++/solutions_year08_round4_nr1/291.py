#include <cstdio>

FILE *in, *out;

int table[10002][2];
int gate[10002];
int calc[2][2][2];
int changable[10002];

void apply(int &x, int y){
    if(x > y) x = y;
}

int main(){
    int n;
    in  = fopen("A.in", "r");
    out = fopen("A.out", "w");
    fscanf(in, "%d", &n);

    for(int i=0;i<2;i++)
	for(int j=0;j<2;j++){
	    calc[0][i][j] = i|j;
	    calc[1][i][j] = i&j;
	}

    for(int t=0;t<n;t++){
	int i;
	int m, v;

	fscanf(in, "%d %d", &m, &v);
	for(i=1;i<=(m-1)/2;i++)
	    fscanf(in, "%d %d", &gate[i], &changable[i]);
	for(i=(m-1)/2+1;i<=m;i++){
	    int x;
	    fscanf(in, "%d", &x);
	    table[i][x] = 0;
	    table[i][1-x] = 100000;
	}

	for(i=(m-1)/2;i>0;i--){
	    int c1=i*2, c2=i*2+1;
	    table[i][0] = 100000;
	    table[i][1] = 100000;

	    for(int x=0;x<2;x++)
		for(int y=0;y<2;y++){
		    apply(table[i][calc[gate[i]][x][y]], table[c1][x] + table[c2][y]);
		    if(changable[i])
			apply(table[i][calc[1-gate[i]][x][y]], table[c1][x] + table[c2][y] + 1);
		}
	}

	fprintf(out, "Case #%d: ", t+1);
	if(table[1][v] < 100000)
	    fprintf(out, "%d\n", table[1][v]);
	else
	    fprintf(out, "IMPOSSIBLE\n");
    }
    fclose(in);
    fclose(out);
    return 0;
}
