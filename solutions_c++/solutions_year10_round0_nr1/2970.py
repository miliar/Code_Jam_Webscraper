//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop
#include <stdio.h>
#include <Math.h>

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
FILE *F;
FILE *F2;
String st;
int k,n;
int count;


F = fopen("A-large.in", "r");
F2 = fopen("A-large.out", "r+");
if(F == NULL){
        ShowMessage("Õ≈“ ‘¿…À¿");
}
else{
        fscanf(F, "%i", &count);
        for(int i=1; i<=count; i++){
                fscanf(F, "%i%i", &n, &k);
                n = pow(2,n);
                if( (k+1)%n ==0 && k!=0){
                        fputs(("Case #" + IntToStr(i) + ": ON\n").c_str(), F2);
                }
                else {
                        fputs(("Case #" + IntToStr(i) + ": OFF\n").c_str(), F2);
                }
        }
        fclose(F);
        fclose(F2);
}
}
//---------------------------------------------------------------------------
 