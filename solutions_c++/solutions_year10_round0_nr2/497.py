% this program use the class BigInteger for big integer, 
%which is included in the package available online: http://mattmccutchen.net/bigint
 
#include<iostream>

#include<iostream>
#include "BigIntegerLibrary.hh"

using namespace std;
const int MAX = 1000;
 
BigInteger div2(BigInteger, BigInteger);
BigInteger div(BigInteger[], int);
BigInteger multiple(BigInteger[], int);

int main() {

     int C;
     int N ;
     BigInteger data[MAX] ;
     BigInteger diff[MAX] ;
     cin >> C;
     string s;
     for (int i = 0; i < C; i++) {


         cin >> N;
         for (int j = 0; j < N; j++) {
             cin >> s;
             data[j] = stringToBigInteger(s);
         }
         for (int j = 0; j < N-1; j++) {
             if (data[j+1] > data[j])  
                 diff[j] = data[j+1] - data[j];
              else diff[j] = data[j] - data[j+1]; 
          } 

        BigInteger T = div(diff, N-1);
    
        BigInteger final, t;
        if ( (data[0]%T).isZero()) {
             t = data[0]/T;
        }
        else
             t = data[0]/T + 1;
                
        final = T * t - data[0];
   
       cout << "Case #" << i+1 << ": ";
        cout << final  << endl;
                
    }

}


BigInteger  multiple(BigInteger data[], int n) {
 
    if (n == 1)
      return data[0];
  
     BigInteger tmp = multiple(data, n-1);
     cout << "tmp" << tmp << endl;
     return tmp / div2(data[n-1], tmp) * data[n-1];

}
BigInteger div2(BigInteger m, BigInteger n) {

 BigInteger tmp;
  if( m > n) {
     tmp = m;
     m = n;
     n = tmp;
  }
  if (m == 0)
       return n;
  else {
       tmp = n%m;
 
       return div2(tmp, m);
  }

}

BigInteger div(BigInteger f[], int n) {

   if ( n == 1)
         return f[0];
   else
        return div2(f[n-1], div(f, n-1));

}
 
