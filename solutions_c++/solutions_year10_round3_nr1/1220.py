//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
#include "stdio.h"
#include "math.h"
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
FILE *F;
FILE *F2;
String st;
int a[1001], b[1001];
int aa, bb;
int caseNumber;
int provodNumber;
int count;
F = fopen("A-small-practice.in", "r");
F2 = fopen("A-small-practice.out", "r+");

fscanf(F, "%i", &caseNumber);
for(int j=1; j<=caseNumber; j++){
        count = 0;
        fscanf(F, "%i", &provodNumber);
        for(int i=1; i<=provodNumber;i++){
                fscanf(F, "%i%i", &aa, &bb);
                a[i] = aa;
                b[i] = bb;
        }

        for(int i =1; i<provodNumber;i++){
                for(int k = i+1; k<=provodNumber; k++){
                        if((a[i]-a[k])*(b[i]-b[k]) < 0) count++;
                }
        }

        ShowMessage(IntToStr(count));



        //fputs(("Case #" + IntToStr(j) + ": " + IntToStr(count)+ "\n").c_str(), F2);
}
fclose(F);
fclose(F2);

}
//---------------------------------------------------------------------------
 