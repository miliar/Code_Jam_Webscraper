#include <iostream>
using namespace std;

int data[ 12 ];

int main()
{
    freopen( "b.in" , "r" , stdin );
    freopen( "b.out" , "w" , stdout );
    int case_n;
    long long res = 0;
    cin >> case_n;
    for ( int i = 1 ; i <= case_n ; ++ i )
    {
        int times;
        int group_n;
        int max_n;
        res = 0;
        cin >> times >> max_n >> group_n;
        //       1e8    1e9       1000
        //         
        for ( int j = 0 ; j < group_n ; ++ j )
            cin >> data[ j ];
        int p = 0 ;
        for ( int j = 0 ; j < times ; ++ j )
        {
            int count= 1;
            int temp = data[ p ++ ];
            p %= group_n;
            while ( ( temp + data[ p % group_n ] <= max_n ) && count < group_n  )
            {
                    temp += data[ p % group_n ];
                    p = ( p + 1 ) % group_n;
                    ++ count ;
            }
       //     cout << p << " for p \n";
            res += temp;
          ///  cout << temp << " is the temp\n\n\n\n";
            
         }
        cout << "Case #" << i << ": " << res << "\n";
    }
    return 0;
}
