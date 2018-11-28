/*
 * =====================================================================================
 *
 *       Filename:  recycle.cc
 *
 *    Description:  Solve Recycled Numbers Present @ Link
 *                  http://code.google.com/codejam/contest/1460488/dashboard#s=p2
 *
 *        Version:  1.0
 *        Created:  04/14/2012 11:50:57 AM
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
#include <cmath>  
#include <vector>  
#include <algorithm>

using namespace std;


//===  FUNCTION  ======================================================================
//        Name:  RecycleNumber
// Description:  
//=====================================================================================
typedef vector<unsigned int> uint_vector;

bool RecycleNumber(const unsigned int number, uint_vector &recycled_vector)
{
  //uint_vector recycled_vector;
  unsigned int digits =0;
  //Its a single digit Number.
  //After Recycling it will be same.
  if(number/10 == 0) 
  {
    recycled_vector.push_back(number);
    return true;
  }
  
  unsigned int i = number;
  while ( i != 0)
  {
    digits++;
    i /= 10;
  }

  unsigned int temp;
  unsigned int n = number;
  for ( i = 0; i < digits; i += 1 )
  {
    temp = 0;
    temp = n%10;
    temp = temp*pow(10,digits-1);
    temp += n/10;

    recycled_vector.push_back(temp);
    n=temp;
  }

  //Ensure the Recycled Vector is unique
  sort(recycled_vector.begin(), recycled_vector.end()); 
  recycled_vector.erase(unique(recycled_vector.begin(), recycled_vector.end()), recycled_vector.end()); 

  return true;
}    /* -----  end of function RecycleNumber  ----- */


// ===  FUNCTION  ======================================================================
//         Name:  main
//  Description:  main function
// =====================================================================================
int main ( int argc, char *argv[] )
{
  //1 ≤ T ≤ 100.
  int numTestCase = 0;
  cin >> numTestCase;
  cin.ignore(10,'\n');

  for ( int tc = 1; tc <= numTestCase; tc += 1 )
  {
    unsigned int A,B;
    //Read Each Test Case data: A, B
    cin >> A >> B;
    cin.ignore(10,'\n');

    // Let's say a pair of distinct positive integers (n, m) 
    // is recycled if you can obtain m by moving some digits 
    // from the back of n to the front without changing their 
    // order. For example, (12345, 34512) is a recycled pair 
    // since you can obtain 34512 by moving 345 from the end 
    // of 12345 to the front. Note that n and m must have the 
    // same number of digits (excluding leading zeros) in 
    // order to be a recycled pair.
    //
    // Given integers A and B with the same number of digits, 
    // how many distinct recycled pairs (n, m) are there 
    // with A ≤ n < m ≤ B?
    // 
    // Notice that n < m, therfore n := [A,B) and m := (A,B]
    // Lets calcualte the Total Number of Reclycled Pairs
    unsigned long recycled_pairs = 0;
    for ( unsigned int i = A; i < B; i += 1 )
    {
      unsigned int n = i;
      //Caculate All Possible m's
      uint_vector m_vector;
      if (!RecycleNumber(n,m_vector))
      {
        return EXIT_FAILURE;
      }
      for ( int j = 0; j < m_vector.size(); j += 1 )
      {
        if ( n < m_vector[j] && m_vector[j] <=B ) {
          recycled_pairs++;
        }
      }
    }
      //Display the Output in the required format
    cout << "Case #"<< tc << ": " << recycled_pairs  << endl;
  }

  return EXIT_SUCCESS;
}    // ----------  end of function main  ---------- 

