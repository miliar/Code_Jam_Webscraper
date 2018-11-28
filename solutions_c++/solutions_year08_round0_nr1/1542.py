#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main(){
	FILE* in = fopen("A.in","r");
	FILE* out = fopen("A.out","w");
	char Engines[100][100];
	int TestCase = 0, CntEngines, CntQuery;
	fscanf(in, "%d\n", &TestCase);
	for(int i = 0; i < TestCase; i++)
	{	
		int Answer = 0;
		fscanf(in, "%d\n", &CntEngines);
		for(int n = 0; n < CntEngines; n++)
		{
			fgets(&Engines[n][0], 100, in);
		}
		fscanf(in, "%d\n", &CntQuery);
		char* A[1000];
		int Cnt = 0;
		for(int n=0; n < CntQuery; n++){
			char* Query = (char*)malloc(101);		
			fgets(Query,100, in);
			bool f = false;
			for(int k = 0; k < Cnt; k++){
				if(strcmp(A[k],Query)==0){
					f = true;
					break;
				}
			}
			if(!f){
				A[Cnt] = Query;
				Cnt++;
			}
			if(Cnt >= CntEngines){
				Answer++;
				A[0] = A[Cnt-1];
				Cnt = 1;
			}
		}
		fprintf(out, "Case #%d: %d\n", i+1, Answer);
	}
	return 0;
}
