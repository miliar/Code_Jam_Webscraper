// googlerese_translator.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

typedef unordered_map<string, string> StringMap;
int _tmain(int argc, _TCHAR* argv[])
{
   StringMap m;

   m["y"] = "a";
   m["n"] = "b";
   m["f"] = "c";
   m["i"] = "d";
   m["c"] = "e";
   m["w"] = "f";
   m["l"] = "g";
   m["b"] = "h";
   m["k"] = "i";
   m["u"] = "j";
   m["o"] = "k";
   m["m"] = "l";
   m["x"] = "m";
   m["s"] = "n";
   m["e"] = "o";
   m["v"] = "p";
   m["z"] = "q";
   m["p"] = "r";
   m["d"] = "s";
   m["r"] = "t";
   m["j"] = "u";
   m["g"] = "v";
   m["t"] = "w";
   m["h"] = "x";
   m["a"] = "y";
   m["q"] = "z";


   ifstream inputFile( "C:\\Users\\Ross\\A-small-attempt2.in" );
   if ( !inputFile.is_open() )
   {
      cout << "File could not be read, aborting\n";
      return 0;
   }

   vector<string> stringVec;
   string line;
   while ( inputFile.good() )
   {
      getline( inputFile, line );
      if ( line != "" )
         stringVec.push_back( line );
   }

   inputFile.close();

   vector<string> outVec;
   string testString = "";
   string outString = "";
   string temp = "";

   for ( int j = 1; j < stringVec.size(); j++ )
   {
      testString = stringVec[j];
      outString = "";
      for( int i = 0; i < testString.length(); i++ )
      {
         temp = testString[i];
         StringMap::iterator it = m.find( temp );
         if ( it != m.end() )
            outString += it->second;
         else if ( temp == " " )
            outString += temp;
      }

      outVec.push_back( outString );
   }
   
   ofstream outputFile("C:\\Users\\Ross\\A-small-attempt2.out");
   if ( !outputFile.is_open() )
      return 0;

   for ( int i = 0; i < outVec.size(); i++ )
   {
      cout << "Case #" << i + 1 << ": " << outVec[i] << "\n";
      outputFile << "Case #" << i + 1 << ": " << outVec[i] << "\n";
   }

   outputFile.close();

	return 0;
}