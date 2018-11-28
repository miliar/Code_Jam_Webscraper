#include <iostream>
#include <list>
#include <algorithm>
#include <fstream>

using namespace std;

#define p system("pause")

ifstream iff("aaa.in");
ofstream off("ccc.out");

void print_result(int c);
void merge(list<unsigned long long> & s);
void solve( unsigned long long R, unsigned long long k);
void input( int T );



unsigned long long res = 0;
list <unsigned long long> q;

int main(void) {

    int T;

    iff>>T;

    input(T);

    return 0;
}

void input( int T ) {

     unsigned long long R , k , N, gi;

     for ( int i = 0 ; i < T ; i ++ ) {
         iff>>R>>k>>N;
         cerr<<R<<k<<N<<endl;
         q.clear();
         for ( int j = 0 ; j < N ; j ++ ) {
             iff>>gi;
             q.push_back(gi);
         }

         //cerr<<q.size()<<endl;

         solve(R,k);
         print_result(i+1);
     }
}

void solve( unsigned long long R, unsigned long long k) {
     list<unsigned long long> tmp;
     res = 0;
     unsigned int tot = 0;

     for ( unsigned long long i = 0 ; i < R ; i ++ ) {
         //tmp.clear();

         tot = 0;

         while(true) {
                           unsigned long long v = q.front();
                           tot += q.front();

                           if(tot<=k) {
                                      q.pop_front();
                                      res += v;

                                      tmp.push_back(v);

                                      if(q.empty())
                                        break;
                                      /*if(q.empty()){
                                                    q.push_back(v);
                                                    break;
                                      }
                                      else
                                                       q.push_back(v);
                                      */
                           }

                           else
                                break;
         }

         merge(tmp);
     }
}

void merge(list<unsigned long long> & s) {
     while(!s.empty() ) {
                      q.push_back(s.front());
                      s.pop_front();
                      }
}

void print_result(int c) {
         off<<"Case #"<<c<<": "<<res<<endl;
         //p;
}

