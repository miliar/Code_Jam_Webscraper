#include<stdio.h>
#include<stdlib.h>

FILE *fin;
FILE *fout;

char a[10][10];
char player[3] = "XO";

int check(int x){
	int ret = 0;
	bool ok = true;
	for(int man = 0;man < 2;++man){
		bool ok = true;
		for(int i = 0;i < 4;++i){
			if(a[x][i] != player[man] && a[x][i] != 'T'){
				ok = false;
				break;
			}
		}
		if(ok){
			if(man == 0)
				return 1;
			else
				return -1;
		}
	}
	return 0;
}

void tran(){
	char buff[10][10];
	for(int i = 0;i < 4;++i)
		for(int j = 0;j < 4;++j)
			buff[i][j] = a[i][j];
	for(int i = 0;i < 4;++i)
		for(int j = 0;j < 4;++j)
			a[i][j] = buff[j][i];
}

int main(){
	fin = fopen("A-large.in","r");
	fout = fopen("gcjout.txt","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int caseT = 1;caseT <= T;++caseT){
		for(int i = 0;i < 4;++i)
			fscanf(fin,"%s",a[i]);
		fprintf(fout,"Case #%d: ",caseT);
		int win = 0;
		for(int i = 0;i < 4;++i){
			win = check(i);
			if(win != 0){
				if(win == 1)
					fprintf(fout,"X won\n");
				else
					fprintf(fout,"O won\n");
				win = 1;
				break;;
			}
		}
		if(!win){
			tran();
			for(int i = 0;i < 4;++i){
				win = check(i);
				if(win != 0){
					if(win == 1)
						fprintf(fout,"X won\n");
					else
						fprintf(fout,"O won\n");
					win = 1;
					break;
				}
			}
			if(!win){
				for(int man = 0;man < 2;++man){
					bool ok = true;
					for(int i = 0;i < 4;++i){
						if(a[i][i] != player[man] && a[i][i] != 'T'){
							ok = false;
						}
					}
					if(ok == true){
						fprintf(fout,"%c won\n",player[man]);
						win = 1;
						break;
					}
				}
				if(!win){
					for(int man = 0;man < 2;++man){
						bool ok = true;
						for(int i = 0;i < 4;++i){
							if(a[i][3 - i] != player[man] && a[i][3 - i] != 'T'){
								ok = false;
							}
						}
						if(ok == true){
							fprintf(fout,"%c won\n",player[man]);
							win = 1;
							break;
						}
					}
				}
			}
		}
		if(!win){
			bool complete = true;
			for(int i = 0;i < 4;++i)
				for(int j = 0;j < 4;++j)
					if(a[i][j] == '.')
						complete = false;
			if(complete == true)
				fprintf(fout,"Draw\n");
			else
				fprintf(fout,"Game has not completed\n");
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

