/*
 * =====================================================================================
 *
 *       Filename:  dance.cc
 *
 *    Description:  Dancing with Googlers @ Link
 *                  http://code.google.com/codejam/contest/1460488/dashboard#s=p1
 *
 *        Version:  1.0
 *        Created:  04/14/2012 06:47:06 AM
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

//0 ≤ ti ≤ 30.
//At least S of the ti values will be between 2 and 28, inclusive.

struct TestCaseData {
  int N; // Number of Googlers Dancing
  int S; // Surprising Triplets (0 ≤ S ≤ N) 
  int p; // Best Result of at least p in Triplets (0 ≤ p ≤ 10)
  int scores[100];
};        /* ----------  end of struct TestCaseData  ---------- */

// ===  FUNCTION  ======================================================================
//         Name:  main
//  Description:  main function
// =====================================================================================
int main ( int argc, char *argv[] )
{
  //1 ≤ T ≤ 100.
  int numTestCase = 0;
  cin >> numTestCase;
  cin.ignore(100,'\n');

  for ( int tc = 1; tc <= numTestCase; tc += 1 )
  {
    int i;
    //Read a Test Case Data
    TestCaseData data;
    cin >> data.N >> data.S >> data.p;
    for ( i = 0; i < data.N; i += 1 )
    {
      cin >> data.scores[i];
    }
    cin.ignore(100,'\n');

    int best_googlers = 0;
    int definitely_surprising = 0;

    for ( i = 0; i < data.N; i += 1 )
    {
      //if score > (data.p*3 -2) ==> NOT Surprising
      //if score = (data.p*3 -2) ==> may be/may be NOT
      //if score < (data.p*3 -2) ==> DEFINITELY Surprising
      //In the border line cases,

      int best_threshold;
      best_threshold = (data.p)*3-4;
      
      int l_threshold = best_threshold;
      int u_threshold = best_threshold + 1;

      if(data.p == 0)
      {
        best_threshold = 0;
      }
      else if(data.p == 1)
      {
        best_threshold = 1;
      }

      if ( data.scores[i] >= best_threshold)
      {
        best_googlers++;
      }
      if ( (data.scores[i] >=2 && data.scores[i] <=28 ) && 
         ((data.scores[i] >= l_threshold) && (data.scores[i] <= u_threshold)) )
      {
        definitely_surprising++;
      }
    }

    if(definitely_surprising > data.S)
    {
      best_googlers -= (definitely_surprising - data.S);
    }

    //Display the Output in the required format
    cout << "Case #"<< tc << ": " << best_googlers  << endl;
  }

  return EXIT_SUCCESS;
}    // ----------  end of function main  ---------- 

