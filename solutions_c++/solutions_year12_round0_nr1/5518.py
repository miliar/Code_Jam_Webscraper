#include <iostream.h>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
using namespace std;


int main()
{
      unsigned int T, TestCase;
      char c;
      int i, indexval,lenGooglerese;
      ifstream inFile;
      ofstream outFile;
      
      string tempstrGooglerese,strGooglerese, strEnglish, strConversionTable;
      size_t length;
      strConversionTable ="yhesocvxduiglbkrztnwjpfmaq";

      inFile.open("C:\\Users\\Indira Krishnamurthi\\Desktop\\Smallinput.txt");
      outFile.open("C:\\Users\\Indira Krishnamurthi\\Desktop\\Smalloutput.txt");
      
      inFile >> T;
      inFile.get(c);
      for (TestCase=1; TestCase <= T; TestCase++)
      {
          strGooglerese.clear();
          strEnglish.clear();
          do 
          {
          inFile >> tempstrGooglerese ;
          strGooglerese+=tempstrGooglerese;
          inFile.get(c);
          if (c == '\n') break;
          else strGooglerese+=' ';
          } while (true);
          
          lenGooglerese = strGooglerese.length();
          for (i = 0; i <lenGooglerese;i++)
             {
               if (strGooglerese[i] != ' ')
               {
                  indexval = int(strGooglerese[i])-'a';
                    printf("%iThe index is \n", indexval);
                  strEnglish += strConversionTable[indexval];                 
               }
               else
                  strEnglish += ' ';
             }
              outFile  << "Case #" << TestCase << ": " << strEnglish << "\n";
       }
          
      inFile.close();
      outFile.close();
      return 0;

}
