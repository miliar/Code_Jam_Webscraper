#include <stdio.h>
FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
char elist[300];
int ecnt;
char combine[100][4];
char opposite[100][3];
int C,D,N;
char data[300];
void input()
{
	int i;
	fscanf(fin,"%d",&C);
	for (i=0;i<C;i++){
		fscanf(fin,"%s",&combine[i]);
	}
	fscanf(fin,"%d",&D);
	for (i=0;i<D;i++){
		fscanf(fin,"%s",&opposite[i]);
	}
	fscanf(fin,"%d",&N);
	fscanf(fin,"%s",&data);
}
void pro()
{
	int i,j,k;
	bool cflag;
	bool dflag;
	ecnt=0;
	for (i=0;i<N;i++){
		elist[ecnt] = data[i];
		cflag = false;
		for (j=0;j<C;j++){
			if (elist[ecnt] == combine[j][0]){
				if (ecnt > 0 && combine[j][1] == elist[ecnt-1]){
					elist[ecnt] = 0;
					elist[ecnt-1] = combine[j][2];
					cflag = true;
					break;
				}
			}else if (elist[ecnt] == combine[j][1]){
				if (ecnt > 0 && combine[j][0] == elist[ecnt-1]){
					elist[ecnt] = 0;
					elist[ecnt-1] = combine[j][2];
					cflag = true;
					break;
				}
			}
		}
		if (cflag) continue;
		dflag = false;
		for (j=0;j<D;j++){
			if (elist[ecnt] == opposite[j][0]){
				for (k=ecnt-1;k>=0;k--){
					if (elist[k] == opposite[j][1]){
						dflag =true;
						break;
					}
				}
			}else if (elist[ecnt] == opposite[j][1]){
				for (k=ecnt-1;k>=0;k--){
					if (elist[k] == opposite[j][0]){
						dflag = true;
						break;
					}
				}
			}
			if (dflag) break;
		}
		if (dflag){
			ecnt=0;
			continue;
		}
		ecnt++;
	}
}
void output()
{
	int i;
	fprintf(fout,"[");
	for (i=0;i<ecnt-1;i++){
		fprintf(fout,"%c, ",elist[i]);
	}
	if (ecnt != 0) fprintf(fout,"%c",elist[ecnt-1]);
	fprintf(fout,"]\n");
}
int main()
{
	int i,t;
	fscanf(fin,"%d",&t);
	for (i=0;i<t;i++){
		input();
		pro();
		fprintf(fout,"Case #%d: ",i+1);
		output();
	}
	return 0;
}