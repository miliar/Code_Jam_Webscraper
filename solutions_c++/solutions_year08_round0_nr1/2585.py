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
   int i,j,k,d,m,p;   AnsiString aFileNameLocal; char* cFileNameLocal;
   cFileNameLocal = new char [150];  AnsiString aTemp;  char cTemp;

   FILE *datafile;
//  set up the path and file name
   aFileNameLocal = (AnsiString) "C:\\Google Test\\input.in";
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
      iCases = StrToInt ( aTemp);
// get all cases
      for ( k = 0 ; k < iCases ; k++)
      {
// get number of search engines
         aTemp ="";
         for ( i = 0 ; i < 1000 ; i++ )
         {
            cTemp = getc(datafile);
            if ( (AnsiString)cTemp == "\n" ) break;
            aTemp = aTemp + (AnsiString)cTemp;
         }
         iSearchEngines[k] = StrToInt ( aTemp);
//
         for ( j = 0 ; j < iSearchEngines[k] ; j++ )
         {
// get search engine names
            aTemp ="";
            for ( i = 0 ; i < 1000 ; i++ )
            {
               cTemp = getc(datafile);
               if ( (AnsiString)cTemp == "\n" ) break;
               aTemp = aTemp + (AnsiString)cTemp;
            }
            aSearchEngine[k][j] = aTemp;
         }
// get number of queries
         aTemp ="";
         for ( i = 0 ; i < 1000 ; i++ )
         {
            cTemp = getc(datafile);
            if ( (AnsiString)cTemp == "\n" ) break;
            aTemp = aTemp + (AnsiString)cTemp;
         }
         iQueries[k] = StrToInt ( aTemp);
// get search engine names
         for (d = 0 ; d < iQueries[k] ; d++)
         {
            aTemp ="";
            for ( i = 0 ; i < 1000 ; i++ )
            {
               cTemp = getc(datafile);
               if ( (AnsiString)cTemp == "\n" ) break;
               aTemp = aTemp + (AnsiString)cTemp;
            }
            aQueries[k][d] = aTemp;
         }
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
      for ( i = 1 ; i <= iCases ; i++ )
      {
         aAnswers[i] = "Case #" + IntToStr(i) + ": " + IntToStr(iSwitches[i-1]) + "\n";
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
   int iCount[150];  int iSelect;         int iPos;     int iLast;
//
   for ( i = 0; i < iCases ; i++ )
   {
      iSwitches[i] = 0;
      for ( j = 0 ; j < iSearchEngines[i] ; j++ )
      {
         iFreq = 0;      iFir = -1;     iSec = -1;
         aTemp = aSearchEngine[i][j];
         for ( k = 0 ; k < iQueries[i] ; k++ )
         {
            iPosition[j][k] = -1;
            if ( aQueries[i][k] == aTemp )
            {
               iFreq++;
               iPosition[j][k] = 9;
            }
         }
         if ( iFreq == 0 ) break;
      }
      if ( iFreq == 0 ) continue;

// find latest possible switch
      iSelect = 0;    iPos = 0;
      for ( n = 0 ; n <10000 ; n++ )
      {
         for ( k = 0 ; k < iSearchEngines[i] ; k++ )
         {
            iCount[k] = -1;
            for (m = iPos ; m < iQueries[i] ; m++ )
            {
               if ( iPosition[k][m] > 0 )
               {
                  iCount[k] = m;
                  break;
               }
            }
            if ( iCount[k] < 0 )
            {
               iSelect = -1;
               break;
            }
         }
         iLast = -1;
         for ( p = 0 ; p < iSearchEngines[i] ; p++ )
         {
            if ( iCount[p] >= iLast )
            {
               iLast = iCount[p];
            }
         }
         if ( iSelect == 0 ) iSwitches[i]++;

         iPos = iLast;
      }
   }
}
//---------------------------------------------------------------------------

