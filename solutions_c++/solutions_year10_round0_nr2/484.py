#include <cstdio>
#include <string>
#include <algorithm>
#define MAX 1005

using namespace std;

/* Courtesy:: zobayer.blogspot.com (for the Bigint code)*/
struct Bigint {
    string a;
    int sign;

    Bigint() {}
    Bigint( string b ) { (*this) = b; }
    int size() { return a.size(); }
    Bigint inverseSign() { sign *= -1; return (*this); }
    Bigint normalize( int newSign ) {
        sign = newSign;
        for( int i = a.size() - 1; i > 0 && a[i] == '0'; i-- ) a.erase(a.begin() + i);
        if( a.size() == 1 && a[0] == '0' ) sign = 1;
        return (*this);
    }
    void operator = ( string b ) {
        a = b[0] == '-' ? b.substr(1) : b;
        reverse( a.begin(), a.end() );
        this->normalize( b[0] == '-' ? -1 : 1 );
    }
    bool operator < ( const Bigint &b ) const {
        if( a.size() != b.a.size() ) return a.size() < b.a.size();
        for( int i = a.size() - 1; i >= 0; i-- ) if( a[i] != b.a[i] ) return a[i] < b.a[i];
        return false;
    }
    Bigint operator + ( Bigint b ) {
        if( sign != b.sign ) return (*this) - b.inverseSign();
        Bigint c;
        for( int i = 0, carry = 0; i < (int)a.size() || i < (int)b.size() || carry; i++ ) {
            carry += (i < (int)a.size() ? a[i] - 48 : 0) + (i < (int)b.a.size() ? b.a[i] - 48 : 0);
            c.a += (carry % 10 + 48);
            carry /= 10;
        }
        return c.normalize(sign);
    }
    Bigint operator - ( Bigint b ) {
        if( sign != b.sign ) return (*this) + b.inverseSign();
        if( (*this) < b ) return (b - (*this)).inverseSign();
        Bigint c;
        for( int i = 0, borrow = 0; i < (int)a.size(); i++ ) {
            borrow = a[i] - borrow - (i < b.size() ? b.a[i] : 48);
            c.a += borrow >= 0 ? borrow + 48 : borrow + 58;
            borrow = borrow >= 0 ? 0 : 1;
        }
        return c.normalize(sign);
    }
    Bigint operator * ( Bigint b ) {
        Bigint c("0");
        for( int i = 0, k = a[i]; i < (int)a.size(); i++, k = a[i] ) {
            while(k-- - 48) c = c + b;
            b.a.insert(b.a.begin(), '0');
        }
        return c.normalize(sign * b.sign);
    }
    Bigint operator / ( Bigint b ) {
        if( b.size() == 1 && b.a[0] == '0' ) b.a[0] /= ( b.a[0] - 48 ) ;
        Bigint c("0"), d;
        for( int j = 0; j < (int)a.size(); j++ ) d.a += "0";
        int dSign = sign * b.sign; b.sign = 1;
        for( int i = a.size() - 1; i >= 0; i-- ) {
            c.a.insert( c.a.begin(), '0');
            c = c + a.substr( i, 1 );
            while( !( c < b ) ) c = c - b, d.a[i]++;
        }
        return d.normalize(dSign);
    }
    Bigint operator % ( Bigint b ) {
        if( b.size() == 1 && b.a[0] == '0' ) b.a[0] /= ( b.a[0] - 48 ) ;
        Bigint c("0");
        int cSign = sign * b.sign; b.sign = 1;
        for( int i = a.size() - 1; i >= 0; i-- ) {
            c.a.insert( c.a.begin(), '0');
            c = c + a.substr( i, 1 );
            while( !( c < b ) ) c = c - b;
        }
        return c.normalize(cSign);
    }
    void print() {
        if( sign == -1 ) putchar('-');
        for( int i = a.size() - 1; i >= 0; i-- ) putchar(a[i]);
    }
};


inline Bigint gcd(Bigint a, Bigint b)
{
   Bigint t;
   Bigint silly = Bigint("0");
   while (silly < b) {

      t = b;
      b = a%b;
      a = t;
   }
   return a;
}

int main()
{
   int kases, N, max_dif;
   int i, j, k;
   Bigint bigi[MAX], differ[MAX];
   Bigint silly = Bigint("1");
   Bigint dummy, rem, ans;
   char str[100];
   scanf("%d", &kases);
   for (i = 1; i <= kases; i++) {
      scanf("%d", &N);
      for (j = 0; j < N; j++) {
         scanf("%s", str);
         bigi[j] = Bigint(str);
      }

      // Implementing a bubble sort on the input
      for (k = 0; k < N-1; k++) {
         for (j = N-2; j >= k; j--) {
            if (bigi[j+1] < bigi[j]) {
               dummy = bigi[j];
               bigi[j] = bigi[j+1];
               bigi[j+1] = dummy;
            }
         }
      }
      
      for (j = 0, k = 0; k < N-1; j++, k++) {
         differ[j] = bigi[k+1]-bigi[k];
         if (differ[j] < silly) j--;
      }
      max_dif = j;

      Bigint min = differ[0];
      for (j = 0; j < max_dif; j++) {
         if (differ[j] < min) 
            min = differ[j];
      }
      
      // finding the gcd
      for (j = 0; j < max_dif; j++)
         min = gcd(min, differ[j]);

      rem = bigi[0]%min;
      
      ans = min-rem;
      printf("Case #%d: ", i);
      if (rem < silly)
         printf("0\n");
      else {
         ans.print();
         printf("\n");
      }
   }
   return 0;
}
