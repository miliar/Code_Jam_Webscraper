#include <iostream>
#include <vector>

using namespace std;

int B , O, Bt, Ot, bt;
char wh;

void DO_B ( int x )
{
     Bt += 1 + abs ( B - x );
     B = x;
     
     Bt = max ( Bt , Ot + 1 );
}

void DO_O ( int x )
{
     Ot += 1 + abs ( O - x );
     O = x;
     
     Ot = max ( Bt + 1 , Ot );
}   

void SOLVE(int tst)
{
     Bt = 0;
     Ot = 0;
     B = 1;
     O = 1;
     
     int n;
     
     cin >> n;
     
     for ( int i = 0; i < n; i++ )
     {
         cin >> wh >> bt;
         
         if ( wh == 'B' )
            DO_B ( bt );
         else DO_O ( bt );
         
     }
     
     cout << "Case #" << tst << ": " << max ( Bt , Ot ) << endl;
}
     

int main()
{
    int n;
    
    cin >> n;
    
    for ( int i = 0; i < n; i++ )
        SOLVE(i+1);
        
    return 0;
}
