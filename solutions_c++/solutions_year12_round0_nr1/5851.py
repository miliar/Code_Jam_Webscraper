//---------------------------------------------------------------------------

#include <vcl.h>
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
int i=0,j=0;

for(i=0;i<30;i++)
{
j=0;
AnsiString a=Memo1->Lines->Strings[i];
char *mas=a.c_str();
while(mas[j]!='\0')
        {
           switch(mas[j])
                {
        case 'a': mas[j]='y';break;
        case 'b': mas[j]='h';break;
        case 'c': mas[j]='e';break;
        case 'd': mas[j]='s';break;
        case 'e': mas[j]='o';break;
        case 'f': mas[j]='c';break;
        case 'g': mas[j]='v';break;
        case 'h': mas[j]='x';break;
        case 'i': mas[j]='d';break;
        case 'j': mas[j]='u';break;
        case 'k': mas[j]='i';break;
        case 'l': mas[j]='g';break;
        case 'm': mas[j]='l';break;
        case 'n': mas[j]='b';break;
        case 'o': mas[j]='k';break;
        case 'p': mas[j]='r';break;
        case 'q': mas[j]='z';break;
        case 'r': mas[j]='t';break;
        case 's': mas[j]='n';break;
        case 't': mas[j]='w';break;
        case 'u': mas[j]='j';break;
        case 'v': mas[j]='p';break;
        case 'w': mas[j]='f';break;
        case 'x': mas[j]='m';break;
        case 'y': mas[j]='a';break;
        case 'z': mas[j]='q';break;

        }
        j++;
        }

AnsiString b="Case #";
Label1->Caption=i+1;
AnsiString c=b+Label1->Caption+": ";
Memo2->Lines->Add(c+AnsiString(mas));
}


}
//---------------------------------------------------------------------------

