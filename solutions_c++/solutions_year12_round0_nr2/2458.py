#include <iostream>

using namespace std;

int main()
{
  int cases_num         = 0;
  int dancers_num       = 0;
  int surp_triplets_num = 0;
  int best_result       = 0;
  int triplet_sum       = 0;

  cin >> cases_num ;
  for ( int i = 1; i <= cases_num; ++i )
  {
    int possible          = 0;
    int possible_surp     = 0;
    int result            = 0;

    cin >> dancers_num;
    cin >> surp_triplets_num;
    cin >> best_result;
    for ( int j = 0; j < dancers_num; ++j )
    {
      cin >> triplet_sum;
      if ( (3*best_result-2 ) <= triplet_sum ) 
      { 
        possible++;
      } 
      else if ( (3*best_result-4 ) <= triplet_sum ) 
      { 
        if ( triplet_sum > 1 ) { 
          possible++;
          possible_surp++;
        }
      }
    }

    result = possible;
    if ( surp_triplets_num < possible_surp ) 
    {
      result -= ( possible_surp - surp_triplets_num ); 
    }

    cout << "Case #" << i << ": " << result << endl;
  }
}
