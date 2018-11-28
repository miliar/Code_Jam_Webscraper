#include <stdio.h>
#include <stdlib.h>

int T;
int D, I, M, N;
int a[300];
int answer;
int d[300][300];

int abs(int a){
	if(a>0)
		return a;
	else
		return -a;
}

int dif(int val1, int val2){
	int temp = abs(val1-val2);

	if(temp==0)
		return 0;
	else if(M==0)
		return N*D;
	else if(temp%M==0)
		return temp/M-1;
	else
		return temp/M;
}

int main(){
	FILE *fin = fopen("input.txt","r");
	FILE *fout = fopen("output.txt","w");

	fscanf(fin,"%d",&T);
	for(int k=0;k<T;k++){
		fscanf(fin,"%d%d%d%d",&D,&I,&M,&N);
		for(int i=1;i<=N;i++)
			fscanf(fin,"%d",&a[i]);

		answer=N*D;
		for(int i=0;i<=255;i++)
			d[1][i]=abs(a[1]-i);

		for(int ind1=2;ind1<=N;ind1++){
			for(int val1=0;val1<=255;val1++){
				d[ind1][val1]=N*D;
				for(int ind2=1; ind2<ind1; ind2++){
					for(int val2=0;val2<=255;val2++){
						if(!(M==0 && val1!=val2)){
							if(d[ind1][val1] > d[ind2][val2] + D*(ind1-ind2-1) + dif(val1,val2)*I + abs(val1-a[ind1]))
								d[ind1][val1] = d[ind2][val2] + D*(ind1-ind2-1) + dif(val1,val2)*I+ abs(val1-a[ind1]);
						}
					}
				}
			}
		}

		for(int i=1;i<=N;i++){
			for(int j=0;j<=255;j++){
				if(answer>d[i][j]+(N-i)*D)
					answer=d[i][j]+(N-i)*D;
			}
		}

		fprintf(fout,"Case #%d: %d\n",k+1, answer);
	}

	fclose(fin);
	fclose(fout);

	return 0;
}