#include <stdio.h>
#include <string.h>
#include <string>

int data[500];
long long sum = 0;
int T,N;
FILE* input = fopen("C:\\codejam\\data.in","r");
FILE* output = fopen("C:\\codejam\\data.out","w");

int s[20];

bool isGood(){
	int s1=0,s2=0;
	for(int i=0;i<N;i++){
		if(s[i] == 1){
			s1 += data[i];
		}
		if(s[i] == 2){
			s2 += data[i];
		}
	}
	return s1 == s2;
}
bool nextS(){
	int curr = 0;
	while(s[curr] == 2 && curr < N){
		s[curr] = 0;
		curr++;
	}
	if(curr != N){
		s[curr] += 1;
		return true;
	}else{
		return false;
	}
}

int main(){
	fscanf(input,"%d\n",&T);
	for(int t=0;t<T;t++){
		fscanf(input,"%d",&N);
		for(int i=0;i<N;i++){
			fscanf(input,"%d",data+i);
			s[i] = 0;
		}
		s[0] = 1;
		fprintf(output,"Case #%d:",t+1);
		do{
			if(isGood()){
				fprintf(output,"\n");
				for(int i=0;i<N;i++){
					if(s[i] == 1){
						fprintf(output,"%d ",data[i]);
					}
				}
				fprintf(output,"\n");
				for(int i=0;i<N;i++){
					if(s[i] == 2){
						fprintf(output,"%d ",data[i]);
					}
				}
				fprintf(output,"\n");
				goto end_searh;
			}
		}while(nextS());
		fprintf(output," Impossible\n");
end_searh:
		fprintf(output,"");
	}
	fclose(input);
	fclose(output);
	return 0;
}