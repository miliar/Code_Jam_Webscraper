//---------------------------------------------------------------------------

#include <vcl.h>
#include <stdio.h>
#pragma hdrstop

#include "UMain.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
	: TForm(Owner)
{
}
//---------------------------------------------------------------------------
bool Lamp(int N, int K){
	bool *Snapper = new bool[N];
	for (int i = 0; i < N; i++)
		Snapper[i] = false;
	for (int i = 0; i < K; i++) {
		for (int j = N-1; j > 0; j--) {
			bool f=true;
			for (int z = 0; z < j; z++)
				if (!Snapper[z]) f=false;
			if (f) Snapper[j]=!Snapper[j];
		}
		Snapper[0]=!Snapper[0];
	}
	bool light=true;
	for (int i = 0; i < N; i++)
		if (!Snapper[i]) light=false;
	return light;
}
void __fastcall TForm1::Button1Click(TObject *Sender)
{
	FILE *f,*fout;
	char s[100];
	int T,N,K;
	if ((f=fopen("c:\\file.in","rt"))==NULL){
		ShowMessage("cannot open file");
		return;
	}
	fgets(s,100,f);
	sscanf(s,"%d",&T);
	AnsiString tmp;
	fout=fopen("c:\\file.out","at+");
	int cas=0;
	for (int k=0; k<T; k++){
		cas++;
		fgets(s,100,f);
		if (sscanf(s,"%d %d",&N, &K)==2){
			if (Lamp(N,K))
				tmp="Case #"+IntToStr(cas)+": ON\n";
			else tmp="Case #"+IntToStr(cas)+": OFF\n";
			fputs(tmp.c_str(),fout);
		}
	}
	fclose(f);
	fclose(fout);
}
//---------------------------------------------------------------------------
