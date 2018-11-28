#include <algorithm>
#include <vector>
#include <iostream>

#include <cmath>

using namespace std;

int main()
{
  int cases_num = 0;

  cin >> cases_num;
  for ( int i = 1; i <= cases_num; ++i )
  {
    int a = 0;
    int b = 0;
    int cnt = 0;
  
    cin >> a;
    cin >> b;

    vector<int> vi;

    for ( int act_num = a; act_num <= b; ++act_num )
    {
      int power = (int) log10( act_num );
      int power_value = (int) pow( double(10), power );
      
      int num = act_num;
      vi.clear();

      for ( int k = 1; k <= power; ++k )
      {
        num = ( num % power_value ) * 10 + ( num / power_value );

        if ( num >= a && 
             num <= b &&
             num > act_num )
        {
          if ( find( vi.begin(), vi.end(), num ) == vi.end() ) 
          {
            cnt++;
            vi.push_back( num );
          }
          
        
          //cout << act_num << "\t" << num << endl;
        } 
      }
    }

    cout << "Case #" << i << ": " << cnt << endl;
  }
}
