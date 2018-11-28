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

//in: A-small_in.in
//

   if ((in = fopen("A-large.in.txt", "rt"))
       == NULL)
   {
      ShowMessage("Cannot open input file");
      return;
   }
   if ((out = fopen("A-large.out", "wt"))
       == NULL)
   {
      ShowMessage("Cannot open output file.");
      return;
   }

int len_word=0;
int numb_words=0;
int numb_samples=0;

 int count_word=0;

   fgets(msg, 100, in);
   sscanf(msg,"%i %i %i", &len_word, &numb_words, &numb_samples);

   Edit1->Text=IntToStr(len_word);
   Edit2->Text=IntToStr(numb_words);
   Edit3->Text=IntToStr(numb_samples);

   for (int i=0; i<=255; ++i)
    {
     table[i]=0;
    }


        for(int i=0; i<=numb_words-1; ++i)
        {
          fgets(alien_words[i], 100, in);
          for(int j=0; j<=len_word-1; ++j)
            {
              table[alien_words[i][j]]=1;
            }

        }


        char msgtmp[252];


        for(int i1=1; i1<=numb_samples; ++i1)
        {
        msg1[0]=0;

//       do{
//           fgets(msgtmp, 250, in);
//          strcat(msg1,msgtmp);
//            }
//       while(msg1[strlen(msg1)-1] != '\n');
           fgets(msg1, 90000, in);



           AnsiString MSG=AnsiString(msg1);
           MSG=MSG.Trim();

           int cur=1;
           count_word=0;

           for(int i=1; i <= len_word;  ++i)
             {
               if(MSG[cur] == ' ')continue;
               if(MSG[cur] != '(')
                 {
                   target_words[i]=AnsiString(MSG[cur]);
                   if(table[MSG[cur]] == 0){count_word=-1;break;}
                   cur++;
                 }
               else
                 {
                  cur++;

                  while(MSG[cur] == ' ')cur++;

                  int cur1=MSG.Pos(")")+1;
                  target_words[i]=MSG.SubString(cur,MSG.Pos(")")-cur);
                  cur=cur1;

                     for(int j=1; j <= target_words[i].Length(); ++j)
                      {
                        if(table[target_words[i][j]] == 0)
                           {
                             target_words[i]=target_words[i].Delete(j,1);
                             j--;
                           }
                      }
                      if(target_words[i].Length() == 0){count_word=-1;break;}
                 }

             MSG=MSG.Delete(1,cur-1);
             cur=1;

             }

                  AnsiString abc;

                  if(count_word == -1)
                          {
                            abc="Case #"+IntToStr(i1)+": 0"+"\n";
                            fputs(abc.c_str(), out);
                          }
                  else
                       {
                        for(int k=0; k < numb_words; k++)
                         {
                           for(int k1=1; k1 <= len_word; ++k1)
                            {
                                if(!strchr(target_words[k1].c_str(),alien_words[k][k1-1]))break;
                                if(k1 == len_word)count_word++;
                            }
                         }
                                abc="Case #"+IntToStr(i1)+": "+count_word+"\n";
                                fputs(abc.c_str(), out);

                        }

            count_word=0;

        }




   fclose(in);
   fclose(out);
   ShowMessage("Success");



}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button2Click(TObject *Sender)
{
Close();        
}
//---------------------------------------------------------------------------

