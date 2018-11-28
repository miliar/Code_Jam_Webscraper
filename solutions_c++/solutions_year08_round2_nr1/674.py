#ifndef _SD_MACROS_H
#define _SD_MACROS_H

// Include files 
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <string>
#include <vector>
#include <cerrno>
#include <cmath>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <map>

using namespace std;


#define sd_err std::cerr << __FILE__ << " : " << __LINE__  << " : " << __func__ << " :: "   


#endif


int main()
{

	int N;
    cin >> N;
    
	vector <long long int> X;
	vector <long long int> Y;

	long long int n,A,B,C,D,M,x0,y0;

	for ( int i = 0 ; i < N  ; i++ )
	{
		cin >> n;
		cin >> A;
		cin >> B;
		cin >> C;
		cin >> D;
		cin >> x0;
		cin >> y0;
		cin >> M;

		X.clear();
		Y.clear();

		X.push_back(x0);
		Y.push_back(y0);

		long long int tempx = x0;
		long long int tempy = y0;

		for ( long long int j = 1 ; j <= n - 1 ; j++ )
		{

			tempx = ( A * tempx + B ) % M;
			tempy = ( C * tempy + D ) % M;
			X.push_back(tempx);
			Y.push_back(tempy);

		}

//        for (  int i = 0 ; i < n ; i++ )
//		{
//			cout << X[i] << " " << Y[i] << endl;
//		}

		register long long int a1,b1,a2,b2,a3,b3;

		long long int count = 0;

		for ( register long long int k = 0 ; k < n ; k++ )
		{
		   a1 = X[k];
	       b1 = Y[k];


		   for ( register long long int l = 0 ; ( k < n ) && ( l != k ) ; l++ )
		   {

			   a2 = X[l];
			   b2 = Y[l];


			   for ( register long long int m = 0 ; ( m < n ) && ( m != k ) && ( m != l ) ; m++ )
			   {

				   a3 = X[m];
				   b3 = Y[m];

				   //cout << a1 << " " <<  b1 << endl;
				   //cout << a2 << " " << b2 << endl;
				   //cout << a3 << " " << b3 << endl;


				   if ( ( ( a1 + a2 + a3 ) % 3 == 0 ) && ( ( b1 + b2 + b3 ) % 3 == 0 ) )
						   {
							   count++;
						   }  

			   }



		   }


	    }	   



     cout << "Case #" << i+1 <<": " << count << endl;

	}

	return 0;

}
