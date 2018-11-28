#include<stdio.h>
#include<math.h>

int n;
class step{
public:
	char color;
	int pos;
} seq[100];

int main(void){
	int T;
	char c;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");

	fscanf(fin,"%d",&T);
	for(int i=1;i<=T;i++){
		fscanf(fin,"%d",&n);
		for(int j=0;j<n;j++){
			fscanf(fin,"%1s %d",&seq[j].color,&seq[j].pos);
		}

		int co=1, cb=1;
		int to=0, tb=0;
		int tm = 0;
		for(int j=0;j<n;j++){
			if(seq[j].color == 'O'){
				int tn = abs(seq[j].pos - co);
				co = seq[j].pos;
				to = to + tn;
				if(tm < to) tm = to;
				tm += 1;
				to = tm;
			} else if(seq[j].color == 'B'){
				int tn = abs(seq[j].pos - cb);
				cb = seq[j].pos;
				tb = tb + tn;
				if(tm < tb) tm = tb;
				tm += 1;
				tb = tm;
			}
		}
		fprintf(fout,"Case #%d: %d\n",i,tm);
	}
	fcloseall();
}