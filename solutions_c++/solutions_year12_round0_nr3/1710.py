#include<stdio.h>
#include<string.h>

int T, Tcount, A,B, count = 0;
char check[2223][2223];
int stack[11],top;
FILE *fin, *fout;
void input();
void process();
void output();
void rotate(char *ch, int N){
	char temp = ch[0];
	int i;
	for(i=0;i < N-1;i++){
		ch[i] = ch[i+1];
	}
	ch[N-1] = temp;
}
int atoi(char *ch){
	int i, sum = 0;
	int length;
	length= strlen(ch);
	for(i=0;i<=length-1;i++){
		sum = sum * 10 + ch[i]-'0';
	}
	return sum;
}

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
	fscanf(fin,"%d%d", &A, &B);
	count = 0;
}

void process(){
	char ch[50];
	int len, flag = 0;
	int i, j, l, k;
	for(i=A;i < B;i++){
		sprintf(ch ,"%d", i);
		top = 0;
		len = strlen(ch);
		for(j=1;j<= len-1;j++){
		    rotate(ch, len);
			l = atoi(ch);
			if(l > i && l <= B) {
				flag= 0;
				for(k=1;k<=top;k++){
					if(stack[k] == l) flag = -1;
				}
				if(flag == 0){
					top++;
					stack[top] = l;
					count++;
				}
			}
		}
		
	}
}

void output(){
	fprintf(fout, "Case #%d: %d\n", Tcount, count);
}
