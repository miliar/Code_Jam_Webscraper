#include<stdio.h>

int T, Tcount, N, S, p;
int t[101], check[101], count;
FILE *fin, *fout;
void input();
void process();
void output();

void main(){
	fin = fopen("input.txt", "r");
	fout=  fopen("output.txt", "w");
	fscanf(fin,"%d\n", &T);
	for(Tcount = 1; Tcount <=T;Tcount++){
		input();
		process();
		output();
	}
	fclose(fin);
	fclose(fout);
}

void input(){
	int i;
	fscanf(fin,"%d%d%d",&N, &S, &p);
	for(i=1;i<=N;i++){
		fscanf(fin,"%d", &t[i]);
		check[i] = 0;
	}
}

void process(){
	int i;
	count = 0;
	for(i=1;i<=N;i++){
		if(t[i] % 3 == 0){
			if(t[i] / 3 >= p){
				count++;
				check[i] = 1;
			}
		}
		else{
			if(t[i] / 3 + 1 >= p){
				count++;
				check[i] = 1;
			}
		}
	}
	for(i=1;i<=N;i++){
		if(check[i] == 0){
			if(t[i] %3 == 1) continue;
			else if(S > 0 && t[i]%3== 2 && t[i]/3 +2 >= p && t[i]/3 + 2 <= 10){
				count++;
				S--;
			}
			else if(S > 0 && t[i]%3 == 0 && t[i]/3+1 >=p && t[i]/3 + 1 <= 10 && t[i]/3-1 >=0){
				count++;
				S--;
			}
		}
	}

}

void output(){
	fprintf(fout,"Case #%d: %d\n", Tcount, count);
}