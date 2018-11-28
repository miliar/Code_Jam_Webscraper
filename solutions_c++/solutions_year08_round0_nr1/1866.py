#include <iostream>
#include <fstream>
#include <map>
#include <string>

using namespace std;

typedef pair<string, bool> psb;

int N, S, Q;
char aux[128];
map<string, bool> bckp, cur;
int ssleft, needed;

void print_map(map<string, bool> &m)
{
	for (map<string, bool>::iterator it = m.begin(); it != m.end(); ++it)
		cout << it->first << " " << it->second << endl;
	cout << endl;
}

int main(int argc, char *argv[]) 
{
	FILE *fi = fopen("A-large.in", "r");
//	FILE *fi = fopen("saving.in", "r");
	fscanf(fi, "%d\n", &N);
	int i;
	int cs = 1;
	FILE *fo = fopen("saving.out", "w");
	while (N--) {
		fscanf(fi, "%d\n", &S);
		for (i = 0; i < S; ++i) {
			fgets(aux, 128, fi);
			bckp.insert(psb(aux, false));
		}

		//print_map(bckp);
		cur = bckp;
		ssleft = S;
		needed = 0;

		fscanf(fi, "%d\n", &Q);
		for (i = 0; i < Q; ++i) {
			fgets(aux, 128, fi);
			if (cur[aux]) {
//				cout << aux << "  Already used. Left: " << ssleft << endl;
				continue;
			} else {
				if (ssleft == 1) {
//					cout << "At " << i << "th query. Switching engines." << endl;
					++needed;
					ssleft = S;
					cur = bckp;
				} 
				--ssleft;
				cur[aux] = true;
//				cout << aux << "  Just used. Left: " << ssleft << endl;
			}
		}

//		cout << needed << endl;
		fprintf(fo, "Case #%d: %d\n", cs, needed);
		++cs;
	}
	fclose(fo);
	fclose(fi);

	return 0;
}

