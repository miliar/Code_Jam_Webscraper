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
//---------------------------------------------------------------------------void __fastcall TForm1::Button1Click(TObject *Sender)

int __fastcall TForm1::outputData(void)
{
char aaa[5];
aaa[1]=' ';
aaa[2]=0;

AnsiString abc="Case #"+IntToStr(inum_samples)+": \n";
fputs(abc.c_str(), out);

       for(int y=0; y < Y_axis; ++y)
          {
            for(int x=0; x < X_axis; ++x)
               {
                   aaa[0]=targetMap[y][x];
                   AnsiString ddd=aaa;
                   fputs(abc.c_str(), out);
               }
            fputs("\n", out);
          }
       return 1;
}

void __fastcall  TForm1::changeBasin(int oldBasin,int newBasin)
{
       for(int y=0; y < Y_axis; ++y)
            for(int x=0; x < X_axis; ++x)
               {
                 if(targetMap[y][x] == oldBasin)
                   {
                        targetMap[y][x]=newBasin;
                   }
               }
      return;
}


int __fastcall TForm1::searchNext(void)
{
       for(int y=0; y < Y_axis; ++y)
            for(int x=0; x < X_axis; ++x)
               {
                 if(targetMap[y][x] == 0)
                   {
                       curY=y;
                       curX=x;
                       return 0;
                   }
               }
      return -1;
}

void __fastcall TForm1::Button1Click(TObject *Sender)
{

//in: A-small_in.in
//

   if ((in = fopen("A-small.in.txt", "rt"))
       == NULL)
   {
      ShowMessage("Cannot open input file");
      return;
   }
   if ((out = fopen("A-small.out", "wt"))
       == NULL)
   {
      ShowMessage("Cannot open output file.");
      return;
   }

num_samples=0;
Y_axis=0;
X_axis=0;

 int count_word=0;

   fgets(msg, 100, in);
   sscanf(msg,"%i", &num_samples);


   for(inum_samples=1; inum_samples <= num_samples; ++inum_samples)
     {
        fgets(msg, 100, in);
        sscanf(msg,"%i %i", &Y_axis, &X_axis);


        Edit1->Text=IntToStr(num_samples);
        Edit2->Text=IntToStr(Y_axis);
        Edit3->Text=IntToStr(X_axis);


       curBasin='a';
       curY=0;
       curX=0;

       lastY=0;
       lastX=0;

       nextY=0;
       nextX=0;

       for(int y=0; y < Y_axis; ++y)
            for(int x=0; x < X_axis; ++x)
               {
                 sourceMap[y][x]=0;
               }

       for(int y=0; y < Y_axis; ++y)
         {
                fgets(msg1, 1000, in);
                int x=0;



                 for(int dl=0; dl<strlen(msg1); ++dl)
                  {
                    if(msg1[dl] != ' ')
                      {
                        sourceMap[y][x]=msg1[dl]-0x30;
                        x++;
                        if(x==X_axis)break;
                      }
                  }
         }

       for(int y=0; y < Y_axis; ++y)
            for(int x=0; x < X_axis; ++x)
               {
                 targetMap[y][x]=0;
               }




        targetMap[curY][curX]=curBasin;
        nextY=curY;
        nextX=curX;

     while(true)
       {

        int level=sourceMap[curY][curX];

        if(curY > 0)
         {
          if(level > sourceMap[curY-1][curX])
           {
             nextY=curY-1;
             nextX=curX;
             level=sourceMap[curY-1][curX];
           }
         }


        if(curX > 0)
         {
          if(level > sourceMap[curY][curX-1])
           {
             nextY=curY;
             nextX=curX-1;
             level=sourceMap[curY][curX-1];
           }
         }

        if(curX < X_axis-1)
         {
          if(level > sourceMap[curY][curX+1])
           {
             nextY=curY;
             nextX=curX+1;
             level=sourceMap[curY][curX+1];
           }
         }


        if(curY < Y_axis-1)
         {
          if(level > sourceMap[curY+1][curX])
           {
             nextY=curY+1;
             nextX=curX;
             level=sourceMap[curY+1][curX];
           }
         }




        if(level >= sourceMap[curY][curX] || targetMap[curY][curX] == targetMap[nextY][nextX])
          {
           if(searchNext() == -1)
             {
              outputData();
              break;
             }
           curBasin++;
           targetMap[curY][curX]=curBasin;
           continue;
          }
         else
          {
            if(targetMap[nextY][nextX] == 0)
             {
               targetMap[nextY][nextX]=curBasin;
               curY=nextY;
               curX=nextX;
               continue;
             }
             else
             {
               changeBasin(targetMap[curY][curX],targetMap[nextY][nextX]);
               if(searchNext() == -1)
                {
                 outputData();
                 break;
                }
                targetMap[curY][curX]=curBasin;
                continue;
             }
          }


        }


     }
/*

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



*/
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
