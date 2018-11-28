#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>

using namespace std;

/* 
 * runme:
 *   g++ -o filename.o filename.cpp
 *   ./filename.o A-example.in
 *
 * runme vim:
 *   :w | !g++ -o %.o % ; ./%.o A-example.in
 *                     && instead ?
 *
 * where A-example.in could be: [ABCD]-(example|small|large).in
 */

/*
 * store one test case, both problem and solution
 */
typedef struct testcase_s {
   char board[4][4];
   int status;
} testcase;

/*
 * Process one test case, read input and fill in output within struct.
 */
void solve(testcase &tc)
{
   tc.status = 3;
   // printf(".");
   int nfull = 0;
   int nupleft = 0;
   char pupleft = tc.board[0][0];
   int ndnleft = 0;
   char pdnleft = tc.board[0][3];
   bool pT = false;
   for( int i = 0; i < 4; ++i )
   {
      int nhorz = 0;
      int nvert = 0;
      char phorz = tc.board[i][0];
      char pvert = tc.board[0][i];
      for( int j = 0; j < 4; ++j )
      {
         char shorz = tc.board[i][j];
         char svert = tc.board[j][i];
         if( shorz != '.' && (shorz == phorz || shorz == 'T' || phorz == 'T') )
            ++nhorz;
         if( svert != '.' && (svert == pvert || svert == 'T' || phorz == 'T') )
            ++nvert;
         if( tc.board[i][j] != '.' )
            ++nfull;
         if( phorz == 'T' || phorz == '.' )
            phorz = shorz;
         if( pvert == 'T' || pvert == '.' )
            pvert = svert;
      }

      char supleft = tc.board[i][i];
      char sdnleft = tc.board[i][3-i];

      if( pdnleft == 'T' )
         pT = true;
      
      if( supleft != '.' && (supleft == pupleft || supleft == 'T' || pupleft == 'T') )
         ++nupleft;
      if( sdnleft != '.' && (sdnleft == pdnleft || sdnleft == 'T' || pdnleft == 'T') )
         ++ndnleft;
      if( pupleft == 'T' || pupleft == '.' )
         pupleft = supleft;
      if( pdnleft == 'T' || pdnleft == '.' )
         pdnleft = sdnleft;

      if( (nhorz == 4 && phorz == 'O') || (nvert == 4 && pvert == 'O') )
         tc.status = 0;
      if( (nhorz == 4 && phorz == 'X') || (nvert == 4 && pvert == 'X') )
         tc.status = 1;

//      if( pT )
//         printf("pT, s=%c, i=%d, n=%d\n", sdnleft, i, ndnleft);      
   }
   if( (nupleft == 4 && pupleft == 'O') || (ndnleft == 4 && pdnleft == 'O') )
      tc.status = 0;
   if( (nupleft == 4 && pupleft == 'X') || (ndnleft == 4 && pdnleft == 'X') )
      tc.status = 1;
   if( nfull == 16 && tc.status == 3)
      tc.status = 2;
}

/*
 * Read in one test case from passed in file pointer.
 */
void readtestcase(testcase &tc, FILE *fp)
{
   for( int i = 0; i < 4; ++i )
   {
      fscanf(fp, "%s ", (char*)&tc.board[i]);
   }
   fscanf(fp, " ");
}

/*
 * Write out one test case solution to passed in file pointer.
 */
void writetestcase(testcase &tc, FILE *fp)
{
   const char *message = NULL;
   switch( tc.status )
   {
      case 0: message = "O won"; break;
      case 1: message = "X won"; break;
      case 2: message = "Draw"; break;
      default: message = "Game has not completed"; break;
   }
   fprintf(fp, "%s", message);
}

/*
 * Process command line argument (input file), read input and write output.
 */
int main(int argc, char **argv)
{
   if( argc != 2 )
   {
      printf("argc != 1\n");
      return 1;
   }

   const char *infilename = argv[1];
   char outfilename[256] = {0};
   const char *endname = strstr(infilename, ".in");
   int namelen = endname == NULL ? strlen(infilename) : endname - infilename;
   if( namelen > sizeof(outfilename) - 5 )
      namelen = sizeof(outfilename) - 5;
   memcpy(outfilename, infilename, namelen);
   strcpy(outfilename + namelen, ".out");

   testcase arrCases[100] = {0};
   int nNumCases;

   FILE *fpInput = fopen(infilename, "r");
   if( NULL == fpInput )
   {
      printf("file '%s' not found\n", infilename);
      return 2;
   }
   try {
      // read in first line.  parse to single int
      char szNumCases[256] = {0};
      if( NULL == fgets(szNumCases, sizeof(szNumCases), fpInput) )
      // if( 1 > fscanf(fpInput, "%d[\n]", &nNumCases) )
      {
         printf("test case count not found at top of file\n");
         throw std::exception();
      }
      nNumCases = atoi(szNumCases);

      for( int iCase = 0; iCase < nNumCases; ++iCase )
      {
         readtestcase(arrCases[iCase], fpInput);
      }
   } catch (std::exception &ex) {
      printf("exception during file read\n");
      fclose(fpInput);
      return 3;
   }
   fclose(fpInput);

   for( int iCase = 0; iCase < nNumCases; ++iCase )
   {
      // solve(arrCases[iCase]);  // solve before writing to output file.
   }

   FILE *fpOutput = fopen(outfilename, "w");
   if( NULL == fpOutput )
   {
      printf("can't write file '%s'\n", outfilename);
      return 4;
   }
   for( int iCase = 0; iCase < nNumCases; ++iCase )
   {
      solve(arrCases[iCase]); // solve as file is written.  
      fprintf(fpOutput, "Case #%d: ", 1 + iCase);
      writetestcase(arrCases[iCase], fpOutput);
      fprintf(fpOutput, "\n"); 
//      fprintf(fpOutput, "Case #%d: %s\n", 1 + iCase, arrCases[iCase].szOut);
      fflush(fpOutput);
   }
   fclose(fpOutput);

   return 0;
}
