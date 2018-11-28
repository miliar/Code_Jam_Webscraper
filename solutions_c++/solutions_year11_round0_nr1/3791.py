#include <iostream>
using namespace std;

const int num = 12;


char R[num];
int S[num];
int n;

int main()
{
    freopen( "A-large.in", "r", stdin );
    freopen("out", "w", stdout);
    int T;
    cin >> T;
    for( int Case = 1; Case <= T; ++Case ){
         cin >> n;
         int po;
         char c;
         int ocost = 0, bcost = 0;
         int opo = 1, bpo = 1;
         for( int i = 0; i < n; ++i ){
              cin >> c >> po;
              if( c == 'O' ){
                  int tmpcost = (int)abs( po - opo );
                  opo = po;
                  ocost += tmpcost;
                  if( bcost > ocost ) ocost = bcost + 1;   
                  else ocost ++;
              }else{
                  int tmpcost = (int)abs( po - bpo );
                  bpo = po;
                  bcost += tmpcost;
                  if( ocost > bcost ) bcost = ocost + 1;
                  else bcost++;  
              }
         }
         
         cout << "Case #" << Case << ": ";
         cout << max( ocost, bcost ) << endl;
    }
}

