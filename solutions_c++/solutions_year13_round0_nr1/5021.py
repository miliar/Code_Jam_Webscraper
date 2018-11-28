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
   iNumber = 1;
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Button1Click(TObject *Sender)
{
   int i,j,k,d,m,p,r,s,t;   AnsiString aFileNameLocal; char* cFileNameLocal;
   cFileNameLocal = new char [150];  AnsiString aTemp;  char cTemp;

   FILE *datafile;
//  set up the path and file name
   aFileNameLocal = (AnsiString) "C:\\Google Test\\test.txt";
   StrPCopy( cFileNameLocal, aFileNameLocal );
// import the data
   if ( ( datafile = fopen(cFileNameLocal,"r+") ) == NULL )
   {
      MessageBox(0, " Cannot open the data file", "Error Message  1" , 0 );
      delete [] cFileNameLocal;
      return;
   }
   else
   {
// get the data file
//
// get number of cases
      aTemp ="";
      for ( i = 0 ; i < 1000 ; i++ )
      {
         cTemp = getc(datafile);
         if ( (AnsiString)cTemp == "\n" ) break;
         aTemp = aTemp + (AnsiString)cTemp;
      }
      iT = StrToInt ( aTemp);
// get all cases
      for ( k = 0 ; k < iT ; k++)
      {
// get line
         aTemp ="";
         for ( i = 0 ; i < 4 ; i++ )
         {
            for ( j = 0 ; j < 4 ; j++ )
            {
               cTemp = getc(datafile);
               if ( (AnsiString)cTemp == "\n" ) break;
               aBoard[k][i][j] = (AnsiString)cTemp;
            }
            cTemp = getc(datafile);
         }
         cTemp = getc(datafile);
      }
    }
//
   fclose (datafile);
   delete [] cFileNameLocal;
}
//---------------------------------------------------------------------------
// create output file
void __fastcall TForm1::Button2Click(TObject *Sender)
{
   int i,j,k,d,m,p;   AnsiString aFileNameLocal; char* cFileNameLocal;
   cFileNameLocal = new char [150];  AnsiString aTemp;  char* cTemp;
   int iB[10000]; int iD[10000]; int iF[10000];
   FILE *datafile;               cTemp = new char [150];
//  set up the path and file name
   aFileNameLocal = (AnsiString) "C:\\Google Test\\output.txt";
   StrPCopy( cFileNameLocal, aFileNameLocal );
// set up the data
   if ( ( datafile = fopen(cFileNameLocal,"w+") ) == NULL )
   {
      MessageBox(0, " Cannot open the data file", "Error Message  1" , 0 );
      delete [] cFileNameLocal;
      return;
   }
   else
   {
// write the output file
      for ( i = 1 ; i <= iT ; i++ )
      {
//   win x
         if ( iAns[i - 1 ] == 1 )
         {
            aAnswers[i] = "Case #" + IntToStr(i) + ": " + "X won" + "\n";
         }
//   win o
         if ( iAns[i - 1 ] == 2 )
         {
            aAnswers[i] = "Case #" + IntToStr(i) + ": " + "O won" + "\n";
         }
//   draw
         if ( iAns[i - 1 ] == 3 )
         {
            aAnswers[i] = "Case #" + IntToStr(i) + ": " + "Draw" + "\n";
         }
// game not complete
         if ( iAns[i - 1 ] == 4 )
         {
            aAnswers[i] = "Case #" + IntToStr(i) + ": " + "Game has not completed" + "\n";
         }

         StrPCopy(cTemp, aAnswers[i]);
         fwrite ( cTemp, 1, aAnswers[i].Length(), datafile );
      }   
   } 
   fclose (datafile);
   delete [] cFileNameLocal;
}
//---------------------------------------------------------------------------
//
void __fastcall TForm1::Button3Click(TObject *Sender)
{
   int i,j,k,l,m,n,p,s,t,u,v;    AnsiString aTemp;   int iFreq;  int iFir;   int iSec;
   int iCount[150];  int iSelect;         int iRow;     int iCol;       int iIncomplete;
   int iA1, iA2, iA3, iA4, iA5, iA6, iA7, iA8, iA9, iA0;
//
   for ( i = 0; i < iT ; i++ )
   {
//   clear the markers
      for ( k = 0 ; k < 4 ; k++ )
      {
         for ( m = 0 ; m < 4 ; m++ )
         {
            iX[k][m] = 0;
            iO[k][m] = 0;
         }
      }
      iAns[i] = 0;
//   find values
      iIncomplete = 0;
      for ( k = 0 ; k < 4 ; k++ )
      {
         for ( m = 0 ; m < 4 ; m++ )
         {
            if ( aBoard[i][k][m] == "X" ) iX[k][m] = 1;
            if ( aBoard[i][k][m] == "O" ) iO[k][m] = 1;
            if ( aBoard[i][k][m] == "T" )
            {
               iX[k][m] = 1;
               iO[k][m] = 1;
            }
            if ( aBoard[i][k][m] == "." ) iIncomplete++;
         }
      }
//
      iA1 = 0;   iA2 = 0;   iA3 = 0;   iA4 = 0;   iA5 = 0;   iA6 = 0;   iA7 = 0;
      iA8 = 0;   iA9 = 0;   iA0 = 0;
//   check for X
      for ( p = 0 ; p < 4 ; p++ )
      {
         iA1 = iA1 + iX[0][p];
         iA2 = iA2 + iX[1][p];
         iA3 = iA3 + iX[2][p];
         iA4 = iA4 + iX[3][p];
         iA5 = iA5 + iX[p][0];
         iA6 = iA6 + iX[p][1];
         iA7 = iA7 + iX[p][2];
         iA8 = iA8 + iX[p][3];
      }
         iA0 = iX[0][0] + iX[1][1] + iX[2][2] + iX[3][3];
         iA9 = iX[3][0] + iX[2][1] + iX[1][2] + iX[0][3];
      if ( iA0 == 4 || iA1 == 4 || iA2 == 4 || iA3 == 4 || iA4 == 4 ) iAns[i] = 1;
      if ( iA5 == 4 || iA6 == 4 || iA7 == 4 || iA8 == 4 || iA9 == 4 ) iAns[i] = 1;
      if ( iA0 == 4 ) iAns[i] = 1;
//
      iA1 = 0;   iA2 = 0;   iA3 = 0;   iA4 = 0;   iA5 = 0;   iA6 = 0;   iA7 = 0;
      iA8 = 0;   iA9 = 0;   iA0 = 0;
//   check for O
      for ( p = 0 ; p < 4 ; p++ )
      {
         iA1 = iA1 + iO[0][p];
         iA2 = iA2 + iO[1][p];
         iA3 = iA3 + iO[2][p];
         iA4 = iA4 + iO[3][p];
         iA5 = iA5 + iO[p][0];
         iA6 = iA6 + iO[p][1];
         iA7 = iA7 + iO[p][2];
         iA8 = iA8 + iO[p][3];
      }
         iA0 = iO[0][0] + iO[1][1] + iO[2][2] + iO[3][3];
         iA9 = iO[3][0] + iO[2][1] + iO[1][2] + iO[0][3];
      if ( iA0 == 4 || iA1 == 4 || iA2 == 4 || iA3 == 4 || iA4 == 4 ) iAns[i] = 2;
      if ( iA5 == 4 || iA6 == 4 || iA7 == 4 || iA8 == 4 || iA9 == 4 ) iAns[i] = 2;
      if ( iA0 == 4 ) iAns[i] = 2;
      if ( iAns[i] == 0 && iIncomplete > 0 )
      {
         iAns[i] = 4;
      }
      if ( iAns[i] == 0 )
      {
         iAns[i] = 3;
      }

   }
}
//---------------------------------------------------------------------------

