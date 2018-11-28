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

extern "C" {
#include <sys/types.h>
#include <limits.h>
#include <inttypes.h>
#include <stdint.h>
}

using namespace std;

#define sd_err std::cerr << __FILE__ << " : " << __LINE__  << " : " << __func__ << " :: "   

// Vectors 

typedef vector<int8_t> vi8_t;
typedef vector<int16_t> vi16_t;
typedef vector<int32_t> vi32_t;
typedef vector<int64_t> vi64_t;
typedef vector<u_int8_t> vui8_t;
typedef vector<u_int16_t> vui16_t;
typedef vector<u_int32_t> vui32_t;
typedef vector<u_int64_t> vui64_t;
typedef vector<float> vf_t;
typedef vector<string> vs_t;

// Maps
typedef map<int8_t,string> mi8s_t;
typedef map<int16_t,string> mi16s_t;
typedef map<int32_t,string> mi32s_t;
typedef map<int64_t,string> mi64s_t;
typedef map<u_int8_t,string> mui8s_t;
typedef map<u_int16_t,string> mui16s_t;
typedef map<u_int32_t,string> mui32s_t;
typedef map<u_int64_t,string> mui64s_t;
typedef map<float,string> mfs_t;
typedef map<double,string> mds_t;

typedef map<string,string> mss_t;

typedef map<string,int8_t> msi8_t;
typedef map<string,int16_t> msi16_t;
typedef map<string,int32_t> msi32_t;
typedef map<string,int64_t> msi64_t;
typedef map<string,u_int8_t> msui8_t;
typedef map<string,u_int16_t> msui16_t;
typedef map<string,u_int32_t> msui32_t;
typedef map<string,u_int64_t> msui64_t;
typedef map<string,float> msf_t;
typedef map<string,double> msd_t;

#define SZ(x) (u_int32_t)(x.size())
#define F0(i,n) for(int64_t i=0;i<n;i++)
#define F1(i,n) for(int64_t i=1;i<=n;i++)
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()


#endif



int main()
{

    int32_t N;
	cin >> N;
	for( int32_t i = 0 ; i < N ; i++ )
	{
      uint64_t P,K,L;
	  cin >> P; // max number of letters on key
	  cin >> K; // number of keys available
      cin >> L; // mumber of letters in alphabet

      vui64_t arr;
	  uint64_t temp;

	  for ( uint64_t j = 0 ; j < L ; j++ )
	  {
		  cin >> temp;
          arr.pb(temp);

	  }


	   sort( rall(arr) );

	   uint64_t mult = 0;
	   long long unsigned int sum = 0;

       for ( uint64_t k = 0 ; k < L ; k++ )
	   {

		   if ( ( k % K ) == 0 )
		   {
			   mult++;

		   } 

		   sum += ( arr[k] * mult  );

	   }


		cout << "Case #" << i+1 << ": " << sum << endl;
	}



}


