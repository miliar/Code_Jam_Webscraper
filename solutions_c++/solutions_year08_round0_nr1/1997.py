#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int N,S,Q;
struct engine{
	char names[102];
	int first_occurence;
};
struct engine engines[102];
char queries[1002][102];

void set_first(char *name,int x){
	int k;
	for(k=0;k<S;k++){
		if(strcmp(name,engines[k].names)==0){
			if(engines[k].first_occurence==-1)
				engines[k].first_occurence=x;
			return;
		}
	}
}

int find_first(char *name,int start){
	int k;
	for(k=start;k<Q;k++){
		if(strcmp(name,queries[k])==0)
			return k;
	}
	return -1;
}

int main(){
	ifstream fin("A-small.in");
	FILE *fout=fopen("A-small.out","w");
	int i,j;
	
	fin>>N;
	fin.ignore();
	for(i=0;i<N;i++){
		int count=0;
		fin>>S;
		fin.ignore();
		for(j=0;j<S;j++){
			fin.getline(engines[j].names,150);
			engines[j].first_occurence=-1;
		}
		fin>>Q;
		fin.ignore();
		for(j=0;j<Q;j++){
			fin.getline(queries[j],150);
			set_first(queries[j],j);
		}
		int max=0;
		for(j=0;j<S;j++){
			if(engines[j].first_occurence==-1){
				fprintf(fout,"Case #%d: 0\n",i+1);
				goto end_loop;
			}
			if(engines[j].first_occurence>max){
				max=engines[j].first_occurence;
			}
			engines[j].first_occurence=-1;
		}
		count++;
		while(max<=Q-S){
			for(j=0;j<S;j++){
				engines[j].first_occurence=find_first(engines[j].names,max);
			}
			for(j=0;j<S;j++){
				if(engines[j].first_occurence==-1){
					fprintf(fout,"Case #%d: %d\n",i+1,count);
					goto end_loop;
				}
				if(engines[j].first_occurence>max){
					max=engines[j].first_occurence;
				}
				engines[j].first_occurence=-1;
			}
			count++;
		}
		fprintf(fout,"Case #%d: %d\n",i+1,count);
end_loop:	continue;
	}
	return 0;
}