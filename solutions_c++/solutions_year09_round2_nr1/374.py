#include<cstdio>
#include<cstring>
#include<set>
#include<string>
#include<cassert>

using namespace std;
char text[10000];
using namespace std;
int N;

struct node {
	double weight;
	string f;
	int left, right;
	int itself;
} tree[1000];

int tn = 0;
int ti = 0;

char ttt[100];

bool isNumber(char c)
{
	if('0' <= c && c <= '9') return true; else return false;
}


int maketree()
{
	int i = tn++;

	tree[i].left = -1;
	tree[i].right = -1;
	tree[i].f = "";
	tree[i].itself = i;
	tree[i].weight = 0.0;

	while(text[ti] == ' ' || text[ti] == '\n' || text[ti] == '(' || text[ti] == ')') ti++;
	
	assert('0' <= text[ti] && text[ti] <= '9');

	int tt = 0;
	while(isNumber(text[ti]) || text[ti] == '.') {
		ttt[tt++] = text[ti++];
	}
	ttt[tt++] = '\0';

	tree[i].weight = atof(ttt);

	while(text[ti] == ' ') ti++;
	
	if(text[ti] == ')') {
		ti++;
	}
	else {
		tt = 0;
		while(isalpha(text[ti])) {
			ttt[tt++] = text[ti++];
		}
		ttt[tt++] = '\0';
		tree[i].f.assign(ttt);
		tree[i].left = maketree();
		tree[i].right = maketree();
	}

	return i;
}

int main()
{
	FILE *infile = fopen("a.in", "rt"), *outfile = fopen("a.out", "wt");
	fscanf(infile, "%d", &N);
	for(int loop=1; loop<=N; loop++) {
		int L;
		fscanf(infile, "%d\n", &L);
		int len = 0;

		while(L--) {
			fgets(text+len, 1000, infile);
			len = strlen(text);
		}
		
		tn = 0;
		ti = 0;
		maketree();

		int A;
		fscanf(infile, "%d", &A);
		
		fprintf(outfile, "Case #%d:\n", loop);

		while(A--) {
			char name[100];
			int n;
			set<string> s;
			string temp;
			char feature[100];
			fscanf(infile, "%s %d", name, &n);
			while(n--) {
				fscanf(infile, "%s", feature);
				temp.assign(feature);
				s.insert(temp);
			}
			int i = 0;
			double result = 1.0;
			while(1) {
				result *= tree[i].weight;
				if(tree[i].left == -1) break;

				if(s.find(tree[i].f) != s.end()) 
				//if(s.find("cool") != s.end()) 
					i = tree[i].left;
				else 
					i = tree[i].right;
			}
			fprintf(outfile, "%.7lf\n", result);
		}
	}
	

	fclose(infile);
	fclose(outfile);
	return 0;
}
