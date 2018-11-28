#ifndef CONFIG_H
#define CONFIG_H

#include <iostream>
#include <fstream>
#include <cstdlib>

#define BUFFER_SIZE 1024

#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "ouput.txt"

using namespace std;

struct Map
{
   Map() : height( 0 ), width( 0 ), distance( 0 ) {}
   Map(int h, int w, int d) : height( h ), width( w ), distance( d )
   {
      map = new char*[h*w];
      for ( int i = 0; i < h*w; ++i )
      {
         map[i] = 0;
      }
   }
   ~Map()
   {
      if ( height && width && map )
      {
         for ( int i = 0; i < height*width; ++i )
         {
            if ( map[i] )
            {
               delete map[i];
               map[i] = 0;
            }
         }
      }
   }
   void addLine( int lineNum, char* line )
   {
      map[lineNum] = line;
   }
   int height;
   int width;
   int distance;
   char** map;
};

struct Cases
{
   Cases() : numTestCases( 0 ) {}
   ~Cases()
   {
      if ( numTestCases && testCase->map )
      {
         delete [] testCase->map;
      }
   }

   int numTestCases;
   Map* testCase;
};

ifstream* openFileForInput( char* file )
{
   ifstream* ifs = new ifstream;

   ifs->open( file, ios_base::in );

   if ( !ifs->is_open() )
   {
      cout << "Failed to open " << file << endl;
      return NULL;
   }

   return ifs;
}

ofstream* openFileForOutput( char* file )
{
   ofstream* ofs = new ofstream;

   ofs->open( file, ios_base::out );

   if ( !ofs->is_open() )
   {
      cout << "Failed to open " << file << endl;
      return NULL;
   }

   return ofs;
}

Cases readFile( ifstream*& ifs )
{
   Cases* c = new Cases;

   char line[1024];

   ifs->getline( line, BUFFER_SIZE-1 );

   c->numTestCases = atoi( line );

   if ( c->numTestCases > 0 )
   {
      c->testCase = new Map[c->numTestCases];
      for ( int i = 0; i < c->numTestCases; ++i )
      {
         char* newLine = new char[BUFFER_SIZE];
         ifs->getline( newLine, BUFFER_SIZE-1 );

         char* item;
         item = strtok( newLine, " " );
         int h = atoi( item );
         item = strtok( NULL, " " );
         int w = atoi( item );
         item = strtok( NULL, " " );
         int d = atoi( item );

         delete [] newLine;

         c->testCase[i] = Map( h, w, d );
         for ( int j = 0; j < h; ++j )
         {
            newLine = new char[BUFFER_SIZE];
            ifs->getline( newLine, BUFFER_SIZE-1 );
            c->testCase[i].addLine( j, newLine );
         }
      }
   }
   return *c;
}

void prepareTestCase( ofstream*& ofs, int caseNum )
{
   char tmp[12] = {0};
   _itoa_s( caseNum, tmp, 11, 10 );
   ofs->write( "Case #", 6 );
   ofs->write( tmp, strlen(tmp) );
   ofs->write( ": ", 2 );
}

void writeTestCase( ofstream*& ofs, int caseNum, char* caseData )
{
   char tmp[12] = {0};
   _itoa_s( caseNum, tmp, 11, 10 );
   ofs->write( "Case #", 6 );
   ofs->write( tmp, strlen(tmp) );
   ofs->write( ": ", 2 );
   ofs->write( caseData, strlen( caseData ) );
   ofs->put('\n');
}

void closeInputFile( ifstream*& ifs )
{
   if ( !ifs ) return;
   ifs->close();
   delete ifs;
   ifs = 0;
}
void closeOutputFile( ofstream*& ofs )
{
   if ( !ofs ) return;
   ofs->close();
   delete ofs;
   ofs = 0;
}

#endif
