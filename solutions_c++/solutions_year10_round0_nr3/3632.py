//---------------------------------------------------------------------------

#include <vcl.h>
#include <stdio.h>
#pragma hdrstop

#include "Unit1.h"
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
void __fastcall TForm1::Button1Click(TObject *Sender)
{
	FILE *fin, *fout;
	char s[300];
	AnsiString tmp,tmp2;
	int R,tracks,max,groups,sum,push, counts;
	fout=fopen("c:\\file.out","at+");
	if ((fin=fopen("c:\\file.in","rt"))==NULL) {
		ShowMessage("in file not found");
		return;
	}
	fgets(s,300,fin);
	sscanf(s,"%d",&R);
	for (int rounds = 0; rounds < R; rounds++) {
		fgets(s,300,fin);
		sscanf(s,"%d %d %d",&tracks, &max, &groups);
		int *group = new int[groups];
		fgets(s,300,fin);
		tmp=s;
		for (int i = 0; i < groups; i++) {
			tmp2="";
			while(true){
				if (tmp[1]==' ' || tmp.Length()<=1) {
					tmp.Delete(1,1);
					break;
				}
				tmp2+=tmp[1];
				tmp.Delete(1,1);
			}
			group[i]=StrToInt(tmp2);
		}
		sum=0;
		for (int i = 0; i < tracks; i++) {
			counts=0;
			for (int h = 0; h < groups; h++) {
				sum+=group[0];
				counts+=group[0];
				push=group[0];
				for (int t = 0; t < groups; t++)
					group[t]=group[t+1];
				group[groups-1]=push;
				if (max-counts<group[0]) break;
			}
		}
		tmp="Case #"+IntToStr(rounds+1)+": "+IntToStr(sum)+"\n";
		fputs(tmp.c_str(),fout);
	}
	fclose(fin);
	fclose(fout);
}
//---------------------------------------------------------------------------
