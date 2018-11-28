#include <cstdio>
#include <cstring>

int t;
char **a, **c;
char *d1, *d2, *r;
void scrie(){
	int i, j;
	for (i = 0; i<4; i++){
		for (j=0; j<4; j++)
			printf ("%c ",c[i][j]);
		printf("\n");
	}
	printf ("\n");
}
char check_line(char *b){
	int j;
	bool ok = true;
	for (j = 0; j<4; j++)
		if (b[j] != b[0] && b[j]!='T') ok = false;
	if (ok) return b[0];
	for (j = 1; j<4; j++)
		if (b[j] == '.') return '.';
	return '?';
}

void read(){
	int i, j, k, l;
	bool finished, found;
	FILE *f = fopen ("A-small-attempt0.in", "r");
	FILE *g = fopen ("A-small-attempt0.out", "w");
	fscanf (f, "%d", &t);
	for (i = 1; i<=t; i++){
		finished = true; found = false;
		l = 0;
		a = new char*[4];
		c = new char*[4];
		d1 = new char[4];
		d2 = new char[4];
		r = new char[10];
		fprintf (g,"Case #%d: ", i);
		for (j = 0; j<4; j++, l++){
			a[j] = new char[4];
			c[j] = new char[4];
			fscanf (f, "%s",a[j]);
			d1[j] = a[j][j];
			d2[j] = a[j][3-j];
			r[l] = check_line(a[j]);
		}
		for (j = 0; j<4; j++)
			for (k = 0; k<4; k++)
				c[j][k] = a[k][j]; 
		for (j = 0; j<4; j++, l++)
			r[l] =  check_line(c[j]);
		r[l] = check_line(d1);
		r[++l] = check_line(d2);
		for (j = 0; j<10; j++){
			if (r[j] == '.') finished = false;
			if (r[j] == 'X'){found = true; fprintf (g,"X won"); break;}
			if (r[j] == 'O'){found = true; fprintf (g,"O won"); break;}
		}
		if (!found)
			if (finished) fprintf (g,"Draw");
			else fprintf (g,"Game has not completed");
		fprintf (g,"\n");
		delete[] a;
		delete[] c;
		delete[] r;
		delete[] d1;
		delete[] d2;
	}
	fclose (f);
}

int main(){
	read();
	return 0;
}
