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
   aTran[1] ="a";    aTran[2] ="b";   aTran[3] ="c";    aTran[4] ="d";
   aTran[5] ="e";    aTran[6] ="f";   aTran[7] ="g";    aTran[8] ="h";
   aTran[9] ="i";    aTran[10] ="j";   aTran[11] ="k";    aTran[12] ="l";
   aTran[13] ="m";    aTran[14] ="n";   aTran[15] ="o";    aTran[16] ="p";
   aTran[17] ="q";    aTran[18] ="r";   aTran[19] ="s";    aTran[20] ="t";
   aTran[21] ="u";    aTran[22] ="v";   aTran[23] ="w";    aTran[24] ="x";
   aTran[25] ="y";    aTran[26] ="z";
   aEng[1] ="y";    aEng[2] ="h";   aEng[3] ="e";    aEng[4] ="s";
   aEng[5] ="o";    aEng[6] ="c";   aEng[7] ="v";    aEng[8] ="x";
   aEng[9] ="d";    aEng[10] ="u";   aEng[11] ="i";    aEng[12] ="g";
   aEng[13] ="l";    aEng[14] ="b";   aEng[15] ="k";    aEng[16] ="r";
   aEng[17] ="q";    aEng[18] ="t";   aEng[19] ="n";    aEng[20] ="w";
   aEng[21] ="j";    aEng[22] ="p";   aEng[23] ="f";    aEng[24] ="m";
   aEng[25] ="a";    aEng[26] ="z";
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Button1Click(TObject *Sender)
{
   int i,j,k,d,m,p;   AnsiString aFileNameLocal; char* cFileNameLocal;
   cFileNameLocal = new char [150];  AnsiString aTemp;  char cTemp;   int iii;
   AnsiString aTTT;
   FILE *datafile;
//  set up the path and file name
   aFileNameLocal = (AnsiString) "E:\\Google Test\\A-small.txt";
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
// get number of letters in case
         aTemp ="";
         for ( i = 0 ; i < 1000 ; i++ )
         {
            cTemp = getc(datafile);
            if ( (AnsiString)cTemp == "\n" ) break;
            for (iii = 1 ; iii < 27 ; iii++ )
            {
                if ( AnsiString ( cTemp ) == aTran[iii] )   aTTT = aEng[iii];
            }
                if  ( AnsiString ( cTemp ) == " " ) aTTT = " ";


            aTemp = aTemp + aTTT;
            
         }
         aK[k] =  aTemp;
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
   aFileNameLocal = (AnsiString) "E:\\Google Test\\output.txt";
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
      for ( i = 0 ; i < iT ; i++ )
      {
         aAnswers[i] = "Case #" + IntToStr(i) + ": " + aK[i] + "\n";
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
   n = 1;
   for ( i = 1; i < 1000000 ; i++ )
   {
      if ( n == i )
      {
         if ( iD[i] == 0 )
         {
            iD[i] = i;
            n++;
            break;
         }
         else
         {

         }
      }
   }
}
//---------------------------------------------------------------------------

