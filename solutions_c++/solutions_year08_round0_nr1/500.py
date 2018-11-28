#include <algorithm>
#include <string>

#define small(x, y) ((x) < (y) ? (x) : (y))

using namespace std;
FILE *in, *out;

string list[102];
int query[1002], a, b;
int D[2][1002];

int index(string str){
    for(int i=1;i<=a;i++)
	if(list[i] == str)
	    return i;
    return -1;
}

int main(){
    in = fopen("A.in", "r");
    out = fopen("A.out", "w");

    int n;
    fscanf(in, "%d", &n);
    for(int x=0;x<n;x++){
	fscanf(in, " %d ", &a);
	for(int i=1;i<=a;i++){
	    char engine[102];
	    fgets(engine, 101, in);
	    list[i] = string(engine);
	}

	fscanf(in, " %d ", &b);
	for(int i=1;i<=b;i++){
	    char engine[102];
	    fgets(engine, 101, in);
	    query[i] = index(string(engine));
	}

	for(int j=1;j<=a;j++)
	    D[0][j] = 0;

	int sw=0;
	for(int i=1;i<=b;i++){
	    sw = 1-sw;
	    for(int j=1;j<=a;j++){
		D[sw][j] = 0x7ffffff;
		if(query[i] == j) continue;
		for(int k=1;k<=a;k++){
		    if(j == k)
			D[sw][j] = small(D[sw][j], D[1-sw][k]);
		    else
			D[sw][j] = small(D[sw][j], D[1-sw][k]+1);
		}
	    }
	}

	int result=0x7ffffff;

	for(int j=1;j<=a;j++)
	    result = small(result, D[sw][j]);

	fprintf(out, "Case #%d: %d\n", x+1, result);
    }
    fclose(in);
    fclose(out);
    return 0;
}