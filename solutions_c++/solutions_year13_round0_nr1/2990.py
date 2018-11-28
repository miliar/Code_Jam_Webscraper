#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

char map[4][4];
int main(int argc, char** argv) {
	int i,j,k,tmp1,tmp2;
	int round, completed,x,o;
	char no_use;
	FILE *in, *out;
	if (argc!=3) {
		printf("no\n");
		return 0;
	}
	in=fopen(argv[1],"r+");
	out=fopen(argv[2],"w+");
	if (in==NULL || out==NULL) {
		printf("no\n");
		return 0;
	}
	fscanf(in,"%d",&round);
	
	for (i=1;i<=round;i++) {
		completed=1;
		for (tmp1=0;tmp1<4;tmp1++) {
			for (tmp2=0;tmp2<4;tmp2++) {
				fscanf(in,"%c",&(map[tmp1][tmp2]));
				if (map[tmp1][tmp2]!='.' && map[tmp1][tmp2]!='X' && map[tmp1][tmp2]!='O' && map[tmp1][tmp2]!='T') {
					tmp2--;
					continue;
				}
				if (map[tmp1][tmp2]=='.') {
					completed=0;
				}
			}
		}

		for (tmp1=0;tmp1<4;tmp1++) {
			x=1;
			o=1;
			for (tmp2=0;tmp2<4;tmp2++) {
				if (map[tmp1][tmp2]!='X' && map[tmp1][tmp2]!='T') {
					x=0;
				}
				if (map[tmp1][tmp2]!='O' && map[tmp1][tmp2]!='T') {
					o=0;
				}
			}
		
			if (x==1 && o==1) {
				fprintf(out,"Case #%d: Draw\n",i);
				break;
			}
			if (x==1) {
				fprintf(out,"Case #%d: X won\n",i);
				break;
			}
			if (o==1) {
				fprintf(out,"Case #%d: O won\n",i);
				break;
			}
		}
		if (x==1 || o==1) {
			continue;
		}
		for (tmp2=0;tmp2<4;tmp2++) {
			x=1;
			o=1;
			for (tmp1=0;tmp1<4;tmp1++) {
				if (map[tmp1][tmp2]!='X' && map[tmp1][tmp2]!='T') {
					x=0;
				}
				if (map[tmp1][tmp2]!='O' && map[tmp1][tmp2]!='T') {
					o=0;
				}
			}
		
			if (x==1 && o==1) {
				fprintf(out,"Case #%d: Draw\n",i);
				break;
			}
			if (x==1) {
				fprintf(out,"Case #%d: X won\n",i);
				break;
			}
			if (o==1) {
				fprintf(out,"Case #%d: O won\n",i);
				break;
			}
		}
		if (x==1 || o==1) {
			continue;
		}
	
	
	x=1;
	o=1;
	tmp1=0;
	tmp2=0;
	for (;tmp1<4;) {
		if (map[tmp1][tmp2]!='X' && map[tmp1][tmp2]!='T') {
			x=0;
		}
		if (map[tmp1][tmp2]!='O' && map[tmp1][tmp2]!='T') {
			o=0;
		}
		tmp1++;
		tmp2++;
	}
	if (x==1 && o==1) {
		fprintf(out,"Case #%d: Draw\n",i);
		continue;
	}
	if (x==1) {
		fprintf(out,"Case #%d: X won\n",i);
		continue;
	}
	if (o==1) {
		fprintf(out,"Case #%d: O won\n",i);
		continue;
	}
	x=1;
	o=1;
	tmp1=0;
	tmp2=3;
	for (;tmp1<4;) {
		if (map[tmp1][tmp2]!='X' && map[tmp1][tmp2]!='T') {
			x=0;
		}
		if (map[tmp1][tmp2]!='O' && map[tmp1][tmp2]!='T') {
			o=0;
		}
		tmp1++;
		tmp2--;
	}
	if (x==1 && o==1) {
		fprintf(out,"Case #%d: Draw\n",i);
		continue;
	}
	if (x==1) {
		fprintf(out,"Case #%d: X won\n",i);
		continue;
	}
	if (o==1) {
		fprintf(out,"Case #%d: O won\n",i);
		continue;
	}
	
		if (completed==0) {
			fprintf(out,"Case #%d: Game has not completed\n",i);
		}
		else {
			fprintf(out,"Case #%d: Draw\n",i);
		}
	}
	fclose(in);
	fclose(out);
	return 0;
}
