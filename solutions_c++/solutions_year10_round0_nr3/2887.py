//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop
#include "stdio.h"
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

int r,k,n;
int cases;
int *arr;
int money;
int iter;
int current_money;
        F = fopen("C-small-attempt0.in", "r");
        F2 = fopen("C-small-attempt0.out", "r+");
        fscanf(F, "%i", &cases);
        for(int cas = 1; cas<=cases; cas++){
        fscanf(F, "%i%i%i", &r,&k,&n);
        arr = new int[n+1];
        for(int i=1;i<=n;i++){
                fscanf(F, "%i", &arr[i]);
        }

        /*for(int i=1; i<=n;i++){
               ShowMessage(IntToStr(i) + ":" + IntToStr(arr[i]));
        }  */

        money = 0;
        iter = 1;
        int iter2 = 0;
        for(int qw = 1; qw<= r;qw++){
                current_money = 0;
                iter2 = 0;
                while(current_money+arr[iter]<=k && iter2<n){
                        current_money+=arr[iter];
                        iter++;
                        iter2++;
                        if(iter>n){ iter = 1;}
                }
                money += current_money;
                current_money = 0;
        }
        //ShowMessage(IntToStr(money));
        fputs(("Case #" + IntToStr(cas) + ": " + IntToStr(money) +"\n").c_str(), F2);
        }
        fclose(F);
        fclose(F2);
}
//---------------------------------------------------------------------------
