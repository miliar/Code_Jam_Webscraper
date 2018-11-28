/*
 * =====================================================================================
 *
 *       Filename:  speak.cc
 *
 *    Description:  The code solves the problem given @ Google Code Jam 2012
 *                  http://code.google.com/codejam/contest/1460488/dashboard
 *
 *        Version:  1.0
 *        Created:  04/14/2012 05:26:54 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Sushil Kumar Yadav (sky), sushil.iitk@gmail.com
 *        Company:  
 *
 * =====================================================================================
 */


#include <cstdlib>
#include <fstream>
#include <iomanip>   
#include <iostream>  

using namespace std;

//  After Analyzing the Output/Input Encoding examples, following encryption is done.
//  Googlese: abcdefghijklmnopqrstuvwxyz
//  English : yhesocvxduiglbkrztnwjpfmaq
const string googlese = "abcdefghijklmnopqrstuvwxyz";
const string english  = "yhesocvxduiglbkrztnwjpfmaq";
// ===  FUNCTION  ======================================================================
//         Name:  main
//  Description:  main function
// =====================================================================================
int main ( int argc, char *argv[] )
{
  int numTestCase = 0;
  cin >> numTestCase;
  cin.ignore(100,'\n');

  for ( int tc = 1; tc <= numTestCase; tc += 1 )
  {
    string g;
    getline (cin,g);
    for ( unsigned int i = 0; i < g.length(); i += 1 )
    {
      if ( g[i] == ' ') {
        continue;
      }
      g[i] = english[g[i]-'a'] ;
    }
    cout  << "Case #"<< tc << ": " << g << endl;
  }

  return EXIT_SUCCESS;
}    // ----------  end of function main  ---------- 

