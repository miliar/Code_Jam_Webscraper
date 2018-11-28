/* This is my Google Code Jam 2010.
 *
 * All code in this file was written by me, unless otherwise noted. I hereby
 * grant permission to copy, modify and reuse my code for any purpose.
 *  
 * Walaa Usama [BlackCode23]  <walaa_23@msn.com>   May 2010
 */

#include "stdafx.h"
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <map>
#include <string>
#include <cmath>
#define rep(i,m) for(int i=0;i<m;i++)
#define rep2(i,x,m) for(int i=x;i<m;i++)
const double PI = 2*acos(0.0);
using namespace std;

//Public Declarations
int cases;
vector<long> N;
vector<long> K;
long bin2dec(long len)   
{
  long  b, k, m, n;
  long  sum = 0;
 
  for(k = 0; k <= len; k++) 
  {
    for(b = 1, m = len; m > k; m--) 
    {
      b *= 2;
    }
    sum = sum + 1 * b;
  }
  return(sum);
}
void dec2bin(long decimal, char *binary)
{
  int  k = 0, n = 0;
  int  neg_flag = 0;
  int  remain;
  int  old_decimal;  // for test
  char temp[80];
 
  // take care of negative input
  if (decimal < 0)
  {      
    decimal = -decimal;
    neg_flag = 1;
  }
  do 
  {
    old_decimal = decimal;   // for test
    remain    = decimal % 2;
    decimal   = decimal / 2;
    temp[k++] = remain + '0';
  } while (decimal > 0);
 
  if (neg_flag)
    temp[k++] = '-';       // add - sign
  else
    temp[k++] = ' ';       // space
 
  // reverse the spelling
  while (k >= 0)
    binary[k] = temp[--k];
 
  binary[n-1] = 0;         // end with NULL
}
void ReadInputs()
{
	freopen( "A-small.out" , "w" , stdout );
    freopen( "A-small.in" , "r" , stdin );
	scanf( "%d\n" ,&cases);
	rep(i, cases)
	{
		long n, k;
		scanf( "%d%d\n" , &n, &k);
		N.push_back(n);
		K.push_back(k);
	}
}

int main()
{
	ReadInputs();
	rep(i, cases)
	{	
		char binary[80] = {0};
		char flag = '1';
		dec2bin(K[i], binary);
		rep(j, N[i])
		{
			flag &= binary[j];
		}
		if(flag == '1')
		{
			printf("Case #%d: %s\n",i+1,"ON");
		}
		else
		{
			printf("Case #%d: %s\n",i+1,"OFF");
		}
	}
	//rep(i, cases)
	//{		
	//	long NB = bin2dec(N[i]-1);
	//	if((K[i] / NB)*NB + ((K[i] / NB)-1) == K[i])
	//	{
	//		printf("Case #%d: %s\n",i+1,"ON");
	//	}
	//	else
	//	{
	//		printf("Case #%d: %s\n",i+1,"OFF");
	//	}
	//}
    return 0;
}


