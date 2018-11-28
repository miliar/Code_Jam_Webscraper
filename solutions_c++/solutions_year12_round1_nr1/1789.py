#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <map>
#include <set>
#include <limits>
#include <cstring>

using namespace std;

const double eps = 10e-7;

#define bitset(var,pos) ((var) & (1<<(pos)))
#define clearbit(var,pos) (var & (~(1<<(pos)) ))


const char *int2bin (    int x){
    char * b = new char [8];
    b[0] = '\0';

    int z;
    for (z = 256; z > 0; z >>= 1)
    {
        strcat(b, ((x & z) == z) ? "1" : "0");
    }

    return b;
}




int backspace(int val, int bs ) {
    for( int i=0; i<bs; ++i) {
        val=clearbit(val,i);
    }
    return val;
}


int main()
{

   int T = 0, A, B;
   scanf("%d", &T);
   for( int t=1; t<=T; ++t) {
       scanf("%d %d\n",&A, &B);
       float p[B];
       for( int i=0; i<A; ++i) {
           scanf("%f",&p[i]);
       }
       int cases = (1<<A);
       float probab[cases];
       for ( int i=0; i<cases;++i) probab[i]=1.0;



       double min_expected =numeric_limits<float>::infinity() , expected=0;
       for ( int i=0; i<cases;++i) {
           for( int j=0; j< A; ++j) {
               probab[i]*=(double) (bitset(i,j) ? p[A-1-j] : 1- p[A-1-j]);
           }
//           printf("p[%s]=%.2f\n",int2bin(i),probab[i]);
       }
           //keep typing
           int keystrokes=0;
           for ( int i=0; i<cases;++i) {
               //sum keystrokes
               keystrokes = (i < cases-1) ? B-A+1 + B +1   : B-A+1  ;
               expected+= probab[i]*((double)keystrokes);
           }
           min_expected = min ( min_expected, expected );

           //backspaces
           for( int j =1; j<=A; ++j) {
               expected=0;
               for ( int i=0; i<cases;++i) {
//                   printf("%d %d [%s] [%s]\n", j,i,int2bin(backspace(cases-1,j)),int2bin(backspace(i,j)));
                   //keystrokes if j-th char is bad
                   if ( backspace(cases-1,j) == backspace(i,j))
                       keystrokes = B-A + 2*j + 1;
                   //poprawiono = B-A + 2*j + 1
                   else
                   //nie poprawiono = B - A + 2*j + 2 + B
                       keystrokes =  B - A + 2*j + 2 + B;
                   expected+= probab[i]*((double)keystrokes);
               }
               min_expected = min ( min_expected, expected );
           }
           expected=0;
           //press enter
           for ( int i=0; i<cases;++i) {
               expected+= probab[i]*((double)(B+2));
           }
           min_expected = min ( min_expected, expected );

       printf("Case #%d: %.6lf\n", t, min_expected);

   }

    return 0;
}

