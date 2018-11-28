#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<set>
using namespace std;

FILE *fin, *fout;
int q;
int ntoken, ptoken;
string token[ 8000];

set < string > S;

int nnode;
struct node {
	string feature;
	int l, r;
	double p;
} Node[ 8000];


void make_tree( int index) {

	Node[ index].feature = "";
	Node[ index].l = -1;
	Node[ index].r = -1;
	Node[ index].p = 0;

	char buf[ 20];
	strcpy( buf, token[ ptoken + 1].c_str());
	sscanf( buf, "%lf", &Node[ index].p);

	if ( token[ ptoken + 2].compare( ")") == 0) {
		ptoken += 3;
		return ;
	} else {
		Node[ index].feature = token[ ptoken + 2];
		ptoken += 3;
		
		Node[ index].l = nnode++;
		make_tree( Node[ index].l);
		
		Node[ index].r = nnode++;
		make_tree( Node[ index].r);

		ptoken ++;
	}
}

double getp() {
	double ret = 1;
	int p = 0;

	while ( 1) {
		ret *= Node[ p].p;
		if ( Node[ p].feature.size()) {
			if ( S.count( Node[ p].feature))
				p = Node[ p].l;
			else
				p = Node[ p].r;
		} else
			break;
	}

	return ret;
}

int main( void) {

	fin = fopen ( "input.txt", "rt");
	fout = fopen ( "output.txt", "wt");

	int testnum;
	fscanf( fin, "%d", &testnum);

	for ( int i = 1; i <= testnum; i++) {

		ntoken = 0;
		int nopen = 0;
		int line;
		fscanf( fin, "%d", &line);
		while( 1) {
			string tmp, t;
			char buf[ 100];
			fscanf( fin, "%s", buf);
			tmp = buf;
			for ( int j = 0; j < tmp.size(); j++) {
				if ( tmp[ j] == '(') {
					tmp = tmp.substr( 0, j) + " ( " + tmp.substr( j + 1);
					j+=2;
				}
				if ( tmp[ j] == ')') {
					tmp = tmp.substr( 0, j) + " ) " + tmp.substr( j + 1);
					j+=2;
				}
			}

			tmp += " ";
			t = "";

			for ( int j = 0; j < tmp.size(); j++) {
				if ( tmp[ j] == '(') nopen++;
				if ( tmp[ j] == ')') nopen--;
				if ( tmp[ j] == ' ' && t.size()) {
					token[ ntoken++] = t;
					t = "";
				}
				if ( tmp[ j] != ' ')
					t += tmp[ j];
			}
			if ( nopen == 0) break;
		}

		nnode = 1;
		ptoken = 0;
		make_tree( 0);

		fscanf( fin, "%d", &q);

		fprintf( fout, "Case #%d:\n", i);
		for ( int j = 0; j < q; j++) {
			char buf[ 20];
			int nfeature;

			fscanf ( fin, "%s", buf);
			fscanf( fin, "%d", &nfeature);

			S.clear();

			for ( int k = 0; k < nfeature; k++) {
				fscanf( fin, "%s", buf);
				S.insert( (string) buf);
			}

			fprintf( fout, "%.7lf\n", getp());		
		}
	}

	return 0;
}
