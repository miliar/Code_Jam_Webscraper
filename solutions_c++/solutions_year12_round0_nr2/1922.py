// Dancing.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
FILE *fin,*fout;
int T,N,S,P;

enum EnumMode {
	initMode =0,
	normalMode = 1,
	surpriseMode = 2
} modeType;
class CData {
public:
	CData();
	int number;
	int resultDiv;
	int resultMod;
	int maxNormal;
	int maxSurprise;
	EnumMode mode;
	void ChangeModeToSurprise();
	int getMax();
};

void CData::ChangeModeToSurprise() {
	if (mode==normalMode) {
		this->mode = surpriseMode;
		if (this->resultMod==0)
			this->maxSurprise = this->resultDiv+1;
		else if (this->resultMod==2)
			this->maxSurprise = this->resultDiv+2;
	}
}
int CData::getMax() {
	if (mode==normalMode)
		return this->maxNormal;
	else if (mode==surpriseMode)
		return this->maxSurprise;
}
CData::CData() {
	this->number = 0;
	this->resultDiv = 0;
	this->resultMod = 0;
	this->maxNormal = 0;
	this->maxSurprise =0 ;
	this->mode = initMode;
}

CData *data[200];
void process(int testNumber) {
	for (int i=1;i<=N;i++) {
		data[i]->resultDiv = (int)data[i]->number / 3;
		data[i]->resultMod = data[i]->number % 3;
		data[i]->mode = normalMode;

		if (data[i]->resultMod==0) {
			data[i]->maxNormal = data[i]->resultDiv;
		}
		else if (data[i]->resultMod==1) {
			data[i]->maxNormal = data[i]->resultDiv+1;
		}
		else if (data[i]->resultMod==2) {
			data[i]->maxNormal = data[i]->resultDiv+1;
		}
	}
	int count=0;

	// process surprise
	for (int i=1;i<=N;i++) {
		if (data[i]->number<=0) 
			continue;

		if (data[i]->resultMod==0 || data[i]->resultMod==2) {
			if (data[i]->maxNormal < P && data[i]->maxNormal+1 >= P) {
				if (S) {
					data[i]->ChangeModeToSurprise();
					S--;
				}
			}
		}
		if (S==0)
			break;
	}

	for (int i=1;i<=N;i++) {
		if (data[i]->getMax()>=P)
			count++;
	}
	fprintf(fout,"Case #%d: %d\n",testNumber,count);


}
int _tmain(int argc, _TCHAR* argv[])
{
	fin = fopen("Dancing.in", "r");
	fout = fopen("Dancing.out", "w");

	fscanf(fin,"%d\n",&T);

	for (int t=1;t<=T;t++) {
		fscanf(fin,"%d %d %d ",&N,&S,&P);
		for (int n=1;n<=N;n++) {
			data[n] = new CData();
			fscanf(fin,"%d",&data[n]->number);
		}
		process(t);

		for (int n=1;n<=N;n++) {
			delete (data[n]);
		}
	}

	fclose(fin);
	fclose(fout);
	return 0;
}

