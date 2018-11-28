#include<stdio.h>
#include<algorithm>
#define Maxn 200
#define Max 0x7fffffff
#define Min 0x80000000
#define PName "q2"

void init(void);
void process(void);
void out(void);

FILE *in = fopen(PName".in" , "r");
FILE *op = fopen(PName".out" , "w");
struct TRAIN{
	int type;
	int time;
} A[Maxn + 1] , B[Maxn + 1];
int IndexA[Maxn + 1] , IndexB[Maxn + 1];
int nA , nB;
int T;
int ansA , ansB;

bool PRIA(int a , int b){
	if(A[a].time < A[b].time) return true; else if(A[a].time > A[b].time) return false; else{
		if(A[a].type > A[b].type) return true; else return false;
	}
}

bool PRIB(int a , int b){
	if(B[a].time < B[b].time) return true; else if(B[a].time > B[b].time) return false; else{
		if(B[a].type > B[b].type) return true; else return false;
	}
}

int main(void){
	int T;
	int i;
	fscanf(in , "%d" , &T);
	for(i=1; i<=T; i++){
		ansA = ansB  = Max;
		fprintf(op , "Case #%d: " , i);
		init();
		process();
		out();
	}
	fclose(in);
	fclose(op);
	return 0;
}

void init(void){
	int i;
	int tt , mm , time;
	int a , b;
	fscanf(in , "%d" , &T);
	fscanf(in , "%d %d" , &a , &b);
	nA=nB=0;
	for(i=1; i<=a; i++){
		fscanf(in , "%d:%d" , &tt , &mm);
		time = tt * 60 + mm - T;
		nA++;
		A[nA].type = -1;
		A[nA].time = time;

		fscanf(in , "%d:%d" , &tt , &mm);
		time = tt * 60 + mm;
		nB++;
		B[nB].type = 1;
		B[nB].time = time;
	}
	for(i=1; i<=b; i++){
		fscanf(in , "%d:%d" , &tt , &mm);
		time = tt * 60 + mm - T;
		nB++;
		B[nB].type = -1;
		B[nB].time = time;

		fscanf(in , "%d:%d" , &tt , &mm);
		time = tt * 60 + mm;
		nA++;
		A[nA].type = 1;
		A[nA].time = time;
	}
	for(i=1; i<=nA; i++){
		IndexA[i] = i;
	}
	for(i=1; i<=nB; i++){
		IndexB[i] = i;
	}
	std::sort(&IndexA[1] , &IndexA[nA+1] , PRIA);
	std::sort(&IndexB[1] , &IndexB[nB+1] , PRIB);
}

void process(void){
	int ca = 0 , cb = 0 , i , ii;
	for(i=1; i<=nA; i++){
		ii = IndexA[i];
		ca += A[ii].type;
		ii = IndexB[i];
		cb += B[ii].type;
		if(ansA > ca) ansA = ca;
		if(ansB > cb) ansB = cb;
	}
	ansA = -ansA;
	ansB = -ansB;
	if(ansA < 0){
		ansA = 0;
	}
	if(ansB < 0){
		ansB = 0;
	}
}

void out(void){
	fprintf(op , "%d %d\n" , ansA , ansB);
}