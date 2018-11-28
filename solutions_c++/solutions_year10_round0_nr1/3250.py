#include <iostream>
#include <fstream>


using namespace std;

#define p system("pause")

ifstream iff("in.in");
ofstream off("out.out");

void print_result(bool possible, int c);
unsigned int get_s( int S );
unsigned int get_f( int F ) ;
void calculate( int N , int K , int cases );
void input( int T );

int main(void) {

    int T;

    iff>>T;

    input(T);

    return 0;
}

void input( int T ) {

     int N , K;

     for ( int i = 0 ; i < T ; i ++ ) {

         iff>>N>>K;
         calculate(N,K,i+1);
     }

}

void calculate( int N , int K , int cases ) {

     unsigned int first = get_f(N);
     unsigned int second = get_s(N);

     int rem = K;

     rem -= first;

     if( rem == 0 ) {
         print_result(true,cases);
         return ;
     }

     else if(rem<0) {
          print_result(false,cases);
          return;
     }

     if( rem % second == 0 ) {
         print_result(true,cases);
         return;
     }

     else {
          print_result(false,cases);
          return;
     }


     /*while( rem > 0 ) {
            rem -= second;
     }

     if( rem < 0 ) {
         print_result(false,cases);
         return;
     }

     else {
         print_result(true,cases);
     }*/

     //return;
}

unsigned int get_f( int F ) {

         unsigned int to_ret = (1<<F) - 1;

         return to_ret;
}

unsigned int get_s( int S ) {
         unsigned int to_ret = (1<<S);

         return to_ret;
}

void print_result(bool possible, int c) {
                       if( possible )
                           off<<"Case #"<<c<<": "<<"ON"<<endl;

                       else {
                            off<<"Case #"<<c<<": "<<"OFF"<<endl;
                       }
         //p;
}





