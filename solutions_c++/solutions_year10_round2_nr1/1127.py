#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <vector>

using namespace std;

class Tnode{
public:
	string s;
	vector<Tnode> v;
};

int dab=0;
vector<Tnode> add_string(Tnode* n, char *str){
	if (str[0] == 0) return n->v;
	int L = strlen(str);
	int i;
	string dir="";
	for (i=0;i<L;++i){
		if (str[i] == '/' || str[i] == 10){
			break;
		}else{
			dir.push_back(str[i]);
		}
	}
	int j;
	for (j=0;j<int(n->v.size());++j){
		if (n->v[j].s.compare(dir) == 0){
			if (i+1 >= L) return n->v;
			else return add_string(&(n->v[j]), str+i+1);
		}
	}
	Tnode temp;
	temp.s = dir;
	n->v.push_back(temp);
	++dab;
	if (i+1 >= L) return n->v;
	else return add_string(&(n->v[j]), str+i+1);
}
int main(void)
{
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");

	int T, N, M;
	int i;
	int test_case;
	char str[500]={0};
	string temp;
	fscanf(fin, "%d", &T);
	for (test_case = 1; test_case <= T; ++test_case){
		fscanf(fin, "%d %d", &N, &M);
		fgets(str, 500, fin);
		Tnode vec;
		for (i=0;i<N;++i){
			fgets(str, 500, fin);
			add_string(&vec, str+1);
		}
		dab = 0;
		for (i=0;i<M;++i){
			fgets(str, 500, fin);
			add_string(&vec, str+1);
		}
		fprintf(fout, "Case #%d: %d\n", test_case, dab);
	}
	
	fclose(fin);
	fclose(fout);
	return 0;
}