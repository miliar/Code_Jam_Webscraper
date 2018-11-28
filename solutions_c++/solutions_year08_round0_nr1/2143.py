#include <windows.h>
#include <stdio.h>
#include "def.h"
#include "Central.h"

char glbTempName[MAX_SEARCH_NAME]={0};

BOOLEAN DoCase(PCASE_INFORMATION Case){
	FILE* Archivo;
	DWORD Switchs;
	InitSystem(Case->SearchEngines, Case->SearchEngNumber, Case->Queries, Case->QueriesNumber);
	Switchs=CalculateSwitchs();
	Archivo=fopen("output.out", "a+");
	if(!Archivo)
		return FALSE;
	fprintf(Archivo, "Case #%d: %d\n", Case->CaseNumber, Switchs);
	fclose(Archivo);
	return TRUE;
}

int main(){
	DWORD n, i, s, e, q;
	CASE_INFORMATION Case;
	FILE* Archivo;
	Archivo=fopen("output.out", "w+");
	if(!Archivo)
		return FALSE;
	fclose(Archivo);
	Archivo=fopen("input.in", "r");
	if(!Archivo){
		printf("Error =(");
		return 1;
	}
	fscanf(Archivo, "%d", &n);
	for(i=0; i<n; i++){
		memset(&Case, 0, sizeof(CASE_INFORMATION));
		fscanf(Archivo, "%d", &s);
		for(e=0; e<s; e++){
			while(1){ //Lookup until a valid string be found
				fgets(glbTempName, MAX_SEARCH_NAME, Archivo);
				if(glbTempName[0]!='\n')
					break;
			}
			glbTempName[strlen(glbTempName)-1]=0; //Delete de newline char from buffer
			strncpy(Case.SearchEngines[e].Name, glbTempName, MAX_SEARCH_NAME);
			Case.SearchEngines[e].Suspended=FALSE;
		}
		Case.SearchEngNumber=s;
		fscanf(Archivo, "%d", &q);
		for(e=0; e<q; e++){
			while(1){ //Lookup until a valid string be found
				fgets(glbTempName, MAX_SEARCH_NAME, Archivo);
				if(glbTempName[0]!='\n')
					break;
			}
			glbTempName[strlen(glbTempName)-1]=0; //Delete de newline char from buffer
			strncpy(Case.Queries[e].Query, glbTempName, MAX_SEARCH_NAME);
		}
		Case.QueriesNumber=q;
		Case.CaseNumber=i+1;
		DoCase(&Case);
	}
	fclose(Archivo);
	return 0;
}